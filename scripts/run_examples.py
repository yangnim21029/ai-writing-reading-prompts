#!/usr/bin/env python3
"""Run independent, recorded prompt demonstrations with the Gemini REST API."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / 'examples'
MODEL = 'gemini-3.5-flash'
GENERATION = {'temperature': 0.7, 'topP': 0.95, 'maxOutputTokens': 8192, 'candidateCount': 1}
COMMON = '請用繁體中文完成任務。回答以 200–300 個中文字為目標，不計標點與空白；這是輸出篇幅的共同要求。不要加上額外的開場白或結語。素材為虛構的示範文本。'

CASES = {
 'clarity': {
  'title': '清晰度修訂',
  'task': 'Review the supplied draft for clarity and suggest improvements.',
  'source': 'writing-revision/2604.11009-planning-to-revision/prompts/06-writing-clarity.en.txt',
  'paper': 'https://arxiv.org/html/2604.11009v2#A3.SS3.SSS2',
  'material': '本館上學期試辦延長夜間開放，原先希望讓白天無法到館的學生也能使用空間，但後來的調查發現，表示滿意的人主要是原本就常來的學生，因此這項措施對新使用者的幫助可能沒有預期多。問卷共有八十人回覆，其中六十人曾在晚上使用圖書館，不過這不表示晚上到館的人有四分之三都滿意，因為兩個問題的回答並不一樣。館員認為繼續辦理有其必要，但如果沒有增加人力，延長的部分會影響原來工作，所以建議先保留每週兩天，再觀察一學期。這個安排並不是否定學生的需求，而是在目前條件下，讓服務能夠持續，同時也需要把沒有來的人為何沒來弄清楚。',
  'changes': 'Replaced {draft} with the shared Chinese material. Original clarity instructions retained. Added the same Chinese language and length instruction to both conditions.'
 },
 'narrative': {
  'title': '角色第一人稱敘事',
  'task': 'Turn the supplied plot into a first-person narrative from Lin An (林安).',
  'source': 'story-generation/2608.10337-narrative-keyframing/prompts/05-first-person.en.txt',
  'paper': 'https://arxiv.org/html/2608.10337v1#A1.SS5',
  'material': '林安回到父親留下的舊書店，準備在傍晚把鑰匙交給新店主。她已經簽好轉讓文件，也答應姐姐不再拖延。整理櫃檯時，她找到一本被雨水泡皺的帳簿，最後一頁記著幾位欠款讀者的名字，旁邊卻都寫了「已還」。她認得其中一位是每天坐在門口看書、很少買書的老人。姐姐打電話來問她是否出發，她只說還有一個抽屜沒清完。五點的鐘聲響起，新店主在玻璃門外等候。林安沒有撕掉文件，也沒有決定留下書店。她把帳簿收進自己的帆布袋，關掉櫃檯的燈，走過父親從前坐著的位置，才把鑰匙交出去。雨仍在下，門口那張留給讀者的椅子已經被搬到騎樓深處。',
  'changes': 'Filled the full-story, target-plot and narrator variables; selected the no-character-keyframe branch; omitted absent custom instructions. Added an explicit JSON output schema, shared by both conditions. Tested only Appendix A.5, not the full Narrative Keyframing pipeline.'
 },
 'close-reading': {
  'title': '詩歌細讀',
  'task': 'Analyze the supplied poem, explaining its meaning and use of language.',
  'source': 'close-reading/2603.06855-poem-interpretation/prompts/close-reading-task.en.txt',
  'paper': 'https://github.com/xxxxbrandieeee/close-reading-interface/blob/main/close-reading/src/pageInfo.ts',
  'material': '末班車開走以後\n母親仍把門口的燈留著\n她說不是等誰\n只是巷子太暗\n\n我在電話這頭答應\n下次回去會早一點\n窗外另一座城市的車聲\n把那個下次推得更遠\n\n她問我有沒有吃飯\n我說吃了\n桌上那碗還沒拆封的麵\n慢慢失去熱氣\n\n通話結束前\n她又說燈泡最近不太亮\n我想起小時候走過巷口\n總能先看見那一小塊黃\n再看見她站在門裡\n手上拿著忘了收起的雨傘\n\n現在我把手機翻過來\n房間忽然安靜得像一條巷子\n我沒有訂票\n也沒有把燈關掉\n只是把那碗麵放進鍋裡\n等水重新沸騰\n\n樓下有人拖著行李經過\n輪子一格一格碰著路面\n我聽到聲音漸漸走遠\n才發現自己一直站在門邊',
  'changes': 'Original task wording retained, including UI textbox references. Appended the same original Chinese poem. Common instructions map the UI textboxes to normal text output for both conditions.'
 }
}

def write_json(path, data):
 path.parent.mkdir(parents=True, exist_ok=True)
 path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def cjk_count(text):
 return len(re.findall(r'[\u3400-\u9fff]', text))

def extract_text(response):
 candidates=response.get('candidates',[])
 if not candidates:
  raise RuntimeError('API returned no candidate; inspect saved response')
 return ''.join(p.get('text','') for p in candidates[0].get('content',{}).get('parts',[]) if not p.get('thought')).strip()

def request_body(prompt, system, seed, json_mode=False):
 config={**GENERATION, 'seed':seed}
 if json_mode: config['responseMimeType']='application/json'
 body={'contents':[{'role':'user','parts':[{'text':prompt}]}], 'generationConfig':config}
 if system: body['systemInstruction']={'parts':[{'text':system}]}
 return body

def call_api(body, destination):
 destination.mkdir(parents=True,exist_ok=True)
 if (destination/'response.json').exists():
  raise RuntimeError('Refusing to replace a recorded result: '+str(destination))
 write_json(destination/'request.json',body)
 start=time.monotonic()
 start_time=datetime.now(timezone.utc).isoformat()
 key=os.environ.get('GEMINI_API_KEY')
 if not key: raise RuntimeError('Set GEMINI_API_KEY in the environment; never write it into the repository')
 req=urllib.request.Request('https://generativelanguage.googleapis.com/v1beta/models/'+MODEL+':generateContent', data=json.dumps(body).encode(), headers={'Content-Type':'application/json','x-goog-api-key':key}, method='POST')
 try:
  with urllib.request.urlopen(req,timeout=180) as response:
   data=json.load(response)
 except urllib.error.HTTPError as e:
  error={'http_status':e.code,'body':e.read().decode(errors='replace')}
  write_json(destination/'error.json',error)
  raise RuntimeError('Generation failed with HTTP '+str(e.code)) from None
 # API headers and credentials are never stored. Only returned final text and usage metadata are published.
 candidates=data.get('candidates',[])
 for candidate in candidates:
  parts=candidate.get('content',{}).get('parts',[])
  candidate.setdefault('content',{})['parts']=[{'text':p['text']} for p in parts if not p.get('thought') and 'text' in p]
 write_json(destination/'response.json',data)
 text=extract_text(data)
 (destination/'output.txt').write_text(text+'\n',encoding='utf-8')
 meta={'requested_model':MODEL,'returned_model_version':data.get('modelVersion'),'started_at_utc':start_time,'elapsed_seconds':round(time.monotonic()-start,3),'generation_config':body['generationConfig'],'usage':data.get('usageMetadata',{}),'finish_reason':candidates[0].get('finishReason'),'output_cjk_characters':cjk_count(text),'request_sha256':hashlib.sha256((destination/'request.json').read_bytes()).hexdigest(),'output_sha256':hashlib.sha256((text+'\n').encode()).hexdigest()}
 if (destination/'error.json').exists():
  meta['prior_http_error']=json.loads((destination/'error.json').read_text()).get('http_status')
 write_json(destination/'metadata.json',meta)
 if not text or meta['finish_reason']!='STOP':
  raise RuntimeError('Incomplete generation; saved without rewriting: '+str(destination))
 return text,meta

def prepare():
 EXAMPLES.mkdir(exist_ok=True)
 for key,case in CASES.items():
  material=case['material'];count=cjk_count(material)
  if not 200<=count<=300:raise RuntimeError(key+' material length is '+str(count)+' CJK characters')
  folder=EXAMPLES/key;folder.mkdir(exist_ok=True)
  (folder/'material.zh-TW.txt').write_text(material+'\n',encoding='utf-8')
  source=(ROOT/case['source']).read_text().strip()
  common=COMMON
  if key=='clarity':
   detailed=source.replace('{draft}',material)
  elif key=='narrative':
   detailed=source.replace('<plot[0]>\n<plot[1]>\n<…>',material).replace('<targeting_plot>',material).replace('<charactor_name>','林安')
   detailed=detailed.split('If a character keyframe with traits exist for this plot:')[0]+'Character traits: (none provided)'
   common+=' 回傳 JSON 物件，唯一欄位為 narration，內容是故事正文；字數限制適用於故事正文。'
  else:
   detailed=source+'\n\nPoem:\n'+material
   common+=' 若任務提到左右文字框，請依序以一般文字呈現對應內容。'
  (folder/'paper-prompt.txt').write_text(detailed+'\n',encoding='utf-8')
  (folder/'common-instructions.txt').write_text(common+'\n',encoding='utf-8')
  write_json(folder/'case.json',{k:v for k,v in case.items() if k!='material'}|{'material_cjk_characters':count,'source_template_sha256':hashlib.sha256((ROOT/case['source']).read_bytes()).hexdigest()})
  print(json.dumps({'case':key,'material_cjk_characters':count,'material_nonwhitespace_characters':len(re.sub(r'\s','',material))},ensure_ascii=False),flush=True)
 write_json(EXAMPLES/'protocol.json',{'model':MODEL,'generation':GENERATION,'replicate_seeds':[20261113,20261114],'cases':list(CASES),'conditions':['short','paper'],'calls_per_case':4,'system_instruction':COMMON,'language':'zh-TW','material_authorship':'Original fictional materials written for this demonstration','selection':'First completed generation for each prespecified condition and replicate; all recorded outputs retained','evaluation':'Full outputs for readers to compare; lengths and API token usage only. No editorial quality ratings or comparative interpretations.','paper_reproduction':False,'documentation':'https://aistudio.google.com/api-reference/generate-content/generate-content'})

def make_baselines():
 tasks={k:c['task'] for k,c in CASES.items()}
 prompt='Write one concise, competent English prompt for each of the following three tasks. Each prompt must be no more than 35 English words. It should be a useful everyday request, not an intentionally weak baseline. The source material will be appended separately. Language, output length and any output format are supplied separately, so do not specify them. You are not given any research prompts. Return only a JSON object whose keys are clarity, narrative and close-reading and whose values are the three prompt strings.\n\n'+json.dumps(tasks,ensure_ascii=False)
 text,meta=call_api(request_body(prompt,None,20261112,True),EXAMPLES/'baseline-generation')
 values=json.loads(text)
 if set(values)!=set(CASES):raise RuntimeError('Unexpected baseline keys')
 for key,value in values.items():
  if not isinstance(value,str) or len(value.split())>35:raise RuntimeError('Baseline exceeds predefined length')
  (EXAMPLES/key/'short-instruction.txt').write_text(value+'\n',encoding='utf-8')
  material=(EXAMPLES/key/'material.zh-TW.txt').read_text().strip()
  (EXAMPLES/key/'short-prompt.txt').write_text(value+'\n\nSource material:\n'+material+'\n',encoding='utf-8')
  print(json.dumps({'case':key,'short_prompt':value,'instruction_words':len(value.split())},ensure_ascii=False),flush=True)

def run():
 jobs=[]
 for replicate,seed in enumerate([20261113,20261114],1):
  for key in CASES:
   for condition in (['short','paper'] if replicate==1 else ['paper','short']):
    folder=EXAMPLES/key
    target=folder/('run-'+str(replicate))/condition
    if (target/'response.json').exists():
     print('SKIP existing '+str(target.relative_to(ROOT)),flush=True);continue
    prompt=(folder/(condition+'-prompt.txt')).read_text().strip()
    common=(folder/'common-instructions.txt').read_text().strip()
    jobs.append((key,replicate,condition,request_body(prompt,common,seed,key=='narrative'),target))
 with ThreadPoolExecutor(max_workers=3) as pool:
  futures={pool.submit(call_api,body,target):(key,replicate,condition) for key,replicate,condition,body,target in jobs}
  failures=[]
  for future in as_completed(futures):
   key,replicate,condition=futures[future]
   try:
    _,meta=future.result()
    print(json.dumps({'case':key,'replicate':replicate,'condition':condition,**meta},ensure_ascii=False),flush=True)
   except Exception as e:
    failures.append((key,replicate,condition,str(e)))
    print(json.dumps({'failed':failures[-1]},ensure_ascii=False),flush=True)
  if failures:raise RuntimeError(str(failures))

def replay():
 original=ROOT/'examples'
 if EXAMPLES.resolve()==original.resolve():
  raise RuntimeError('Use --output-dir with a new folder to preserve the published results')
 for request in sorted(original.glob('*/run-*/*/request.json')):
  target=EXAMPLES/request.parent.relative_to(original)
  if (target/'response.json').exists():continue
  _,meta=call_api(json.loads(request.read_text()),target)
  print(json.dumps({'case':str(target),'returned_model_version':meta['returned_model_version'],'output_cjk_characters':meta['output_cjk_characters']},ensure_ascii=False),flush=True)

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('action',choices=['prepare','baselines','run','replay'])
 parser.add_argument('--output-dir',default='examples',help='Directory relative to the repository root')
 args=parser.parse_args()
 EXAMPLES=ROOT/args.output_dir
 {'prepare':prepare,'baselines':make_baselines,'run':run,'replay':replay}[args.action]()
