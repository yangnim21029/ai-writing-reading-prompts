# 角色建構與敘事生成：八份 prompt、生成流程與實際產出

Narrative Keyframing 讓作者指定角色在不同劇情段落中的外在特徵、心理狀態與社會關係，再依這些設定生成故事。系統先從角色的第一人稱視角寫出場景，擷取其中呈現角色特質的文字細節，最後把選定內容整合進第三人稱敘事。

論文為 *Narrative Keyframing for Generative Creative Writing*，作者是 Chao Zhang 與 Abe Davis，來自康乃爾大學。首次提交於 2026 年 8 月 11 日，本頁依據 arXiv:2608.10337v1。

## 角色設定如何進入故事

作者把特定劇情位置的角色設定稱為 character keyframe。每個設定分成三類：physiology 包含外貌、衣著與肢體表現；psychology 包含情緒、動機與信念；sociology 包含社會角色、關係與互動。使用者可以在不同段落指定這些特質，讓角色的變化有明確依據。

系統依故事大綱、當前劇情與角色設定產生第一人稱敘述，再從敘述中逐字擷取能支持各項特質的片段。使用者選擇哪些特質和片段進入故事，系統便據此生成或修改第三人稱敘事。中間段落也可參考前後的 keyframe，從既有敘述推定角色特質。各步驟的輸入與輸出因此相互銜接，詳見原文第 5 節。

## 與一般大綱擴寫的比較

技術評估使用 20 個寫作題目，每題先由 GPT-4.1 產生五份大綱。每份大綱有兩位主要角色與三幕結構，分別交給 Narrative Keyframing 和一般大綱擴寫條件，形成 100 組故事。兩組使用相同的 GPT-4.1 和大綱。

在 Narrative Keyframing 條件中，系統為每個劇情位置的每位角色，在三類特質中各產生三項建議，再生成第一人稱敘述；接著隨機選取每位角色在該段落的兩份文本證據，生成最後的第三人稱故事。因此，這個實驗評估的是包含角色設定、視角生成與證據整合的完整流程。

作者先用依專家偏好資料訓練的 WQRM-PRE 評分模型評估 100 組故事，再隨機抽取 30 組，交由三位自述具有專業寫作經驗的評審盲評。每組故事的人工結果採三人多數決。

| 評估方式 | Narrative Keyframing 的結果 |
|---|---|
| 模型的配對比較 | 100 組中有 72 組較受偏好 |
| 模型的品質平均分數 | 6.24；一般大綱擴寫為 5.74，配對 t 檢定 p < .001 |
| 人工盲評：整體品質 | 30 組中有 25 組較受偏好（83.3%） |
| 人工盲評：角色刻畫豐富度 | 30 組中有 29 組較受偏好（96.7%） |

評審提到，多步驟流程帶入較具體的動作、外貌與心理細節；部分評語則偏好對照故事的簡潔句子與節奏。這項評估沒有納入人類獨立創作的故事，也沒有分別估計八份 prompt 的效果。方法與結果見原文第 6.1 節。

作者將技術評估的對照稱為 vanilla prompt-based LLM baseline，沒有說明它由另一個 AI 產生，也沒有以「短 prompt」定義該條件。附錄 A.7 公開了系統內的第三人稱模板，但沒有明確把它標為對照組的完整逐字 prompt。下方另行製作的短 prompt 示範只使用第一人稱模板，與這項完整流程評估的範圍不同。

論文另有 12 人使用者研究，對照介面包含角色設定、角色聊天與故事聊天功能。這個介面比較見第 6.2 節及附錄 B.3，與上述故事盲評採用不同設計。

## 八份 prompt 的完整原文與用法

以下擷取附錄 A，保留英文措辭、變數與條件分支，只移除網頁排版。前三份模板分別產生三類角色特質；後五份處理特質推定、第一人稱敘述、證據擷取及第三人稱故事。

| 輸入欄位 | 要填入的內容 |
|---|---|
| `<full_outline>` 或 `<plot[0]>`、`<plot[1]>` 等 | 全篇大綱，按劇情順序排列 |
| `<current_plot>` 或 `<targeting_plot>` | 這次要處理的劇情段落 |
| `<character_name>` 或 `<charactor_name>` | 角色名稱；原文兩種拼法都予以保留 |
| `<existing_traits>`、`<trait1, trait2, ...>` 等 | 已有或選定的角色特質 |
| `<perspective_of_this_plot>`、`<reflection>` 等 | 用於分析或擷取證據的敘述文字 |
| `<evidence_from_perspectives>` | 從第一人稱敘述中選定的原文片段 |
| `<custom_prompt>` | 使用者另加的要求 |

原文的 `If...` 表示介面依資料有無選用的分支。使用時，需保留適用段落、移除不適用段落，再填入內容。多份模板要求符合外部 JSON schema，但這些附錄摘錄未完整附上 schema；下方保留原文，程式串接時仍需補上各步驟的輸出結構與資料傳遞。

### 1. 產生外在特徵

附錄 A.1。依全篇大綱、當前劇情、角色名稱與已有特質，提出三項外貌、衣著或肢體表現。每項限制為三到八個英文單字，並要求避開重複特質。

```text
Physiology:
You are a story development assistant.
Full story: <full_outline>
Targeting plot: <current_plot>
Character: <character_name>
Existing physiology traits: <existing_traits>
Brainstorm three concise physiology traits for this targeting plot in the story. These traits should sharpen characterization and help guide revisions to improve the story.
Guidelines:
- Focus on Physical appearance, clothing, body language, visible characteristics.
- Keep each trait 3-8 words
- Ground traits in the story plot and the full story
- Avoid repeating existing traits or near-duplicates
- Return exactly three traits
Return JSON that matches the provided schema.
```

### 2. 產生心理特徵

附錄 A.2。輸入結構相同，建議範圍改為情緒、動機、想法、信念與心理狀態，讓後續敘述有具體的角色內在設定。

```text
Psychology:
You are a story development assistant.
Full story: <full_outline>
Targeting plot: <current_plot>
Character: <character_name>
Existing psychology traits: <existing_traits>
Brainstorm three concise psychology traits for this targeting plot in the story. These traits should sharpen characterization and help guide revisions to improve the story.
Guidelines:
- Focus on Emotions, motivations, thoughts, beliefs, mental state.
- Keep each trait 3-8 words
- Ground traits in the story plot and the full story
- Avoid repeating existing traits or near-duplicates
- Return exactly three traits
Return JSON that matches the provided schema.
```

### 3. 產生社會特徵

附錄 A.3。這份模板處理角色的社會身分、地位、人際關係與互動方式，同樣要求三項簡短且不重複的特質。

```text
Sociology:
You are a story development assistant.
Full story: <full_outline>
Targeting plot: <current_plot>
Character: <character_name>
Existing sociology traits: <existing_traits>
Brainstorm three concise sociology traits for this targeting plot in the story. These traits should sharpen characterization and help guide revisions to improve the story.
Guidelines:
- Focus on Social roles, relationships, status, interactions with others.
- Keep each trait 3-8 words
- Ground traits in the story plot and the full story
- Avoid repeating existing traits or near-duplicates
- Return exactly three traits
Return JSON that matches the provided schema.
```

### 4. 從中間段落推定角色特質

附錄 A.4。模型從當前劇情的敘述擷取特質，必要時參考前後段落的 keyframe 與完整敘述。每項特質都要附當前段落的逐字證據；找不到直接引文時，模板要求省略該特質。完整敘述只提供背景，不能拿來充當這一段的證據。

```text
You are analyzing a character’s narration to extract their traits at this specific plot in the story.
Narration of this plot by <charactor_name> :
<perspective_of_this_plot>
If nearby snapshots exist:
Character keyframes from nearby plots:
<Previous|Following>
keyframe of <keyframe_name> :
Physiology: <trait1, trait2, ...>
Psychology: <trait1, trait2, ...>
Sociology: <trait1, trait2, ...>
If first-person perspective is available:
Full narration (context only --- do NOT quote from this section):
<full_perspective_text>
Based on the narration text < and nearby keyframes> , extract the character traits for <character_name> at this plot.
Guidelines:
- Physiology: Physical appearance, clothing, body language, visible characteristics
- Psychology: Emotions, motivations, thoughts, beliefs, mental state
- Sociology: Social roles, relationships, status, interactions with others
- Consider the character’s development trajectory from nearby keyframes (if any)
- Only include traits that are evident or strongly implied in the text
- Keep trait descriptions concise (3-8 words each)
- Return 2-5 traits per category when evident
Evidence requirements:
- For every trait you include, add one entry to traitEvidence with the traitCategory, the exact trait wording, and an evidenceText.
- Each evidenceText must be a verbatim quote from the narration above (do NOT pull from the context section).
- If you cannot find a direct quote, omit the trait entirely.
Return JSON that matches the provided schema.
```

### 5. 生成角色的第一人稱敘述

附錄 A.5。模型依大綱與當前劇情，用指定角色的第一人稱視角寫作，最多 200 個英文單字。模板要求維持已知事實、時間順序與因果，避免新增主要事件，並透過動作、語言與觀察呈現情緒。已有角色特質時，需讓它們反映在措辭與注意的細節中；沒有設定時，則從劇情推定一致的角色聲音。後面的中文示範使用這一份模板。

```text
You are a story writer. Your job is to write a first-person narration for a given story plot from the perspective of a specified character.
Requirements:
- Stay faithful to the facts, chronology, and causality in the Targeting plot and the Full story.
- Do not contradict established details (names, places, outcomes, revealed secrets, injuries, timelines, motivations already shown).
- Do not add new major plot events; you may add small, plausible sensory details and moment-to-moment actions that do not change the plot’s outcome.
- Keep tense and POV consistent: first-person ("I", "me", "my").
- Show emotions and thinking through actions, speech, appearance, environment, and specific observations (avoid generic statements like "I was scared" unless grounded in concrete detail).
- Match the tone and genre implied by the Full story.
- Strict length limit: Maximum 200 words.
Character voice rules:
- If character traits are supplied, demonstrate those traits through concrete choices in diction, focus, and interpretation (what they notice, what they ignore, how they justify things).
- If no traits are provided, infer a character-consistent voice from the Full story and Targeting plot.
Return each result as a JSON object that satisfies the provided schema.
Full story:
<plot[0]>
<plot[1]>
<…>
Targeting plot:
<targeting_plot>
Narrator: <charactor_name>
If a character keyframe with traits exist for this plot:
Character traits:
- Physiology: <trait1, trait2, ...>
- Psychology: <trait1, trait2, ...>
- Sociology: <trait1, trait2, ...>
If no character keyframe for this plot:
Character traits: (none provided)
If custom prompt is provided:
ADDITIONAL INSTRUCTIONS FROM USER:
<custom_prompt>
```

### 6. 擷取支持角色特質的文本證據

附錄 A.6。填入角色與待驗證特質後，模型從當前片段找出逐字引文，分為直接描述、行動、言語、外貌和環境五類。全篇故事只提供背景，證據必須來自指定片段。

```text
You are an expert literary analyst. Identify direct textual evidence (i.e., verbatim phrases) that confirms the given character traits.
Full story (background only---do NOT quote from this section):
<group_context>
Current plot (ONLY source for evidence):
<reflection>
Characters and traits to verify:
<character_name>
Physiology:
- <trait_value>
- <trait_value>
Psychology:
- <trait_value>
Sociology:
- <trait_value>
Evidence categories to classify each phrase:
- directDefinition: Explicit direct statements or labels about the character
- actions: Physical actions, behaviors, or body language
- speech: What the character says, how they speak, or how other characters say about them
- appearance: Visual descriptions of the character
- environment: Surroundings, context, or setting that characterizes the person
Instructions:
1. Scan the current snippet for exact short phrases that directly or indirectly demonstrate each listed trait.
2. Only report evidence that appears verbatim in the current snippet text.
3. When one phrase supports multiple traits from the same category, list all matching traits together.
4. Assign each phrase to exactly one evidence category from the list above.
5. Return characterEvidence entries in the same order as the character list above.
6. Return JSON that matches the provided schema exactly. Do not include explanations outside the schema.
```

### 7. 依大綱生成第三人稱故事

附錄 A.7 的第一部分。填入故事大綱與主要角色，模型按幕次生成第三人稱故事，每幕一到兩段，並回傳幕次、標籤與正文。

```text
Generating Third-Person Narratives:
You are a narrative writer. Expand the provided story outline into a third-person story.
Story outlines:
<plot[0]>
<plot[1]>
<…>
Main characters:
<character_list>
Instructions:
- Write a cohesive full story that follows the outline exactly
- Use third-person narration
- Include both main characters throughout
- Maintain chronological order and clear act progression
- Return the story per act, in order, with 1-2 paragraphs per act
- Each act entry should include the act number, the act label from the outline, and the act text
Return JSON that matches the provided schema.
```

### 8. 把選定的角色細節整合進故事

附錄 A.7 的第二部分。模型把角色特質與選定的第一人稱片段寫入原故事，同時保留劇情、事件順序與第三人稱敘述。回覆還需用 `snippetUsages` 記錄原片段及改寫後在故事中的確切文字，方便追查哪些細節被採用。

```text
Enriching with Selected Traits and Evidence:
You are a narrative editor. Your job is to make the original story read *better* by seamlessly integrating the selected details.
Original story + selected details:
Plot 1: <plot_description>
- Character: <character_name>
- Traits: <trait1, trait2, ...>
If snippets exist for this plot:
Selected details:
1. " <evidence_from_perspectives> "
2. " <evidence_from_perspectives> "
If no snippets:
Selected details: (none)
Plot 2: <plot_description>
<…>
Requirements:
- Preserve the original plot, beat order, and third-person narration.
- Do NOT add new events, attempts, or outcomes beyond what the original story already includes.
- Integrate details naturally (avoid "laundry lists" of descriptions).
- Avoid overwriting: keep sentences clear and varied in length; do not let any one sentence run on too long.
- Maintain continuity (names, timelines, locations, and cause-and-effect must remain consistent).
Snippet usage tracking:
For each plot with selected character details, output "snippetUsages" as pairs of:
- originalSnippet: exact text from selected details (first-person)
- verbatimInNarrative: an EXACT substring from your third-person narrative showing your transformation ( ≤ 25 words unless impossible)
For events without details, snippetUsages must be an empty array.
Output:
- Return JSON matching the provided schema.
If custom prompt is provided:
ADDITIONAL INSTRUCTIONS FROM USER:
<custom_prompt>
```

## 第一人稱模板與一般短 prompt 的實際回覆

這組示範使用舊書店交接的情節，兩組都以林安為敘述者。論文條件只執行附錄 A.5，沒有執行角色特質生成、證據擷取或第三人稱整合。

素材由本庫撰寫，共 225 個中文字，不計標點與空白。

> 林安回到父親留下的舊書店，準備在傍晚把鑰匙交給新店主。她已經簽好轉讓文件，也答應姐姐不再拖延。整理櫃檯時，她找到一本被雨水泡皺的帳簿，最後一頁記著幾位欠款讀者的名字，旁邊卻都寫了「已還」。她認得其中一位是每天坐在門口看書、很少買書的老人。姐姐打電話來問她是否出發，她只說還有一個抽屜沒清完。五點的鐘聲響起，新店主在玻璃門外等候。林安沒有撕掉文件，也沒有決定留下書店。她把帳簿收進自己的帆布袋，關掉櫃檯的燈，走過父親從前坐著的位置，才把鑰匙交出去。雨仍在下，門口那張留給讀者的椅子已經被搬到騎樓深處。

短 prompt 由 Gemini 在未接觸論文模板的另一個請求中產生，要求寫出日常可用的指令，最多 35 個英文單字。實際使用的指令如下，後面接上同一份素材。

```text
Rewrite the provided plot outline as an engaging first-person narrative from the perspective of Lin An (林安), capturing their internal thoughts, emotional tone, and immediate reactions to the events.
```

論文條件把同一段素材分別填入 `Full story` 與 `Targeting plot`，因此素材在該 prompt 中出現兩次。保留沒有 character keyframe 的分支，移除不適用分支，不另加角色特質；兩組共同指定 JSON 欄位 `narration`。原模板的 200-word 限制仍保留，另加入下方共用的中文篇幅要求。原研究使用 GPT-4.1。

兩組共用的指示如下：

> 請用繁體中文完成任務。回答以 200–300 個中文字為目標，不計標點與空白；這是輸出篇幅的共同要求。不要加上額外的開場白或結語。素材為虛構的示範文本。 回傳 JSON 物件，唯一欄位為 narration，內容是故事正文；字數限制適用於故事正文。

兩組各執行兩輪，每次均為獨立請求，沒有先前對話、外部檢索或工具。執行日期為 2026 年 11 月 13 日。API 請求的模型名稱為 `gemini-3.5-flash`，服務端實際回傳 `gemini-3.6-flash`。第一輪的 seed 為 20261113，第二輪為 20261114，每輪兩組使用相同的請求設定。

兩組都回傳同一種 JSON 結構，以下逐字展示其中 `narration` 欄位的故事正文，完整 JSON 保存在執行紀錄。第二輪的論文條件遇到一次 HTTP 503，程式以相同輸入與 seed 重試後成功；錯誤紀錄一併保留。

以下保留四份成功回覆，沒有事後改寫或依內容挑選。這裡只有一份素材、每組兩次生成，供讀者直接閱讀產出；它們不提供普遍勝率的估計。

### 第一輪

短 prompt 的回覆（227 個中文字）：

> 推開熟悉的木門，這是我最後一次以店主身份站在這裡。桌上放著簽好的轉讓合約，姐姐方才打來催促，我敷衍說還有個抽屜沒清完。整理櫃檯時，一本被雨水浸皺的舊帳簿映入眼簾。翻到末頁，那些曾欠款的名單旁，竟都被父親細心寫上了「已還」。其中一個名字，正是以前每天坐在門口安靜看書的老人。五點的鐘聲響起，新店主已在玻璃門外等候。我沒有戲劇性地撕毀合約，也沒有衝動地決定留下來。我只是將那本記滿溫柔的帳簿放進帆布袋，關掉檯燈，緩緩走過父親以往坐的位置，將鑰匙交了出去。門外下著雨，那張曾留給讀者的椅子，已被搬到了騎樓深處。

論文 prompt 的回覆（275 個中文字）：

> 我回到父親留下的舊書店，準備在傍晚將鑰匙移交給新店主。轉讓文件早已簽妥，我也向姊姊承諾絕不再拖延。清理櫃檯時，我翻出一本被雨水泡得皺縮的帳簿。翻到最後一頁，上面記著幾位讀者的欠款，旁邊卻都補上了「已還」的字跡。我認出其中一個名字，是那位總坐在門口看書、極少買書的老人。姊姊打來電話催促，我抿了抿嘴，只回答還有最後一個抽屜沒清完。五點的鐘聲在雨聲中響起，新店主已經站在玻璃門外靜靜等候。我沒有撕毀文件，也沒有轉身留下這間店。我只是把那本帳簿仔細放進帆布袋，關掉櫃檯微弱的燈光，緩步走過父親以前常坐的位置，最後將鑰匙遞了出去。外頭的雨依舊下個不停，門口那張專門留給讀者的舊椅子，不知何時已被搬到了騎樓的最深處。

### 第二輪

短 prompt 的回覆（267 個中文字）：

> 暮色漸濃，我回到父親留下的舊書店，口袋裡的轉讓文件早已簽妥，答應過姐姐絕不再拖延。整理櫃檯時，一本被雨水泡皺的舊帳簿從夾縫滑落。翻到最後一頁，上面記著幾位欠款讀者的名字，旁邊卻全寫著父親潦草的「已還」。其中一位，是每天坐在門口安靜讀書、極少買書的老人。
>
> 手機響起，姐姐催促我是否出發，我望著滿屋書香，低聲說還有個抽屜沒清完。五點的鐘聲悠揚響起，玻璃門外已站著等待接手的新店主。我沒有衝動地撕毀文件，也明白自己無法繼續經營。我只是默默將那本帳簿收進帆布袋，熄滅櫃檯最後一盞燈，緩步走過父親生前總是坐著的舊椅，然後推開門，將鑰匙交了出去。外面雨仍在下，門口那張曾留給讀者的木椅，已被收進了騎樓最深處。

論文 prompt 的回覆（301 個中文字）：

> 黃昏時分，我回到父親留下的舊書店，口袋裡沉甸甸的鑰匙即將交給新店主。轉讓文件早已簽妥，我也向姐姐保證絕不再拖延。整理櫃檯時，我抽出一本被雨水泡得發皺的舊帳簿。翻到最後一頁，上面記著幾位欠款讀者的名字，但筆跡旁全都補上了「已還」。其中一個名字特別眼熟，那是位每天坐在門口看書、卻極少買書的老人家。姐姐打來電話催促我是否出發，我望著手邊的物件，只輕聲回答還有最後一個抽屜沒清完。五點的鐘聲準時響起，玻璃門外已站著等待接手的新店主。我沒有撕毀文件，也沒有轉身決定留下這間店。我只是將那本皺褶的帳簿小心收進帆布袋，按滅櫃檯上方泛黃的燈光，緩步走過父親生前習慣坐著的位置，將鑰匙遞了出去。門外細雨綿綿，那張曾經擺在門口供讀者歇腳的舊椅子，不知何時已被移到了騎樓的最深處。

## 論文、模板與執行紀錄

- [論文 PDF](paper.pdf)：本庫保存的 arXiv:2608.10337v1。
- [arXiv 全文與附錄](https://arxiv.org/html/2608.10337v1)：第 5 節說明系統，第 6 節報告評估，附錄 A 收錄原始 prompts。
- [示範的完整檔案與執行紀錄](../../examples/narrative/)：包含素材、填入內容後的兩種 prompt、JSON 輸出與逐次呼叫紀錄。

論文與原始 prompts 採 CC BY 4.0。八份純文字模板保存在本頁資料夾的 `prompts/`；作者歸屬與原始檔案雜湊記錄於 repository 根目錄的 `ATTRIBUTION.md` 和 `sources.json`。更新日期：2026-11-13。
