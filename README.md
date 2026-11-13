# AI Writing and Reading Prompts

2026 年寫作與閱讀研究的論文與公開 prompt 合集。依用途整理 5 篇 arXiv 論文，提供 PDF、可複製的英文模板、真實使用者提示紀錄，以及繁體中文導讀。

## 目錄

- [寫作規劃與局部修訂](#寫作規劃與局部修訂)
- [範文與風格模仿](#範文與風格模仿)
- [角色與故事生成](#角色與故事生成)
- [詩歌細讀與解釋](#詩歌細讀與解釋)
- [人機共寫與多輪修改](#人機共寫與多輪修改)
- [使用方式](#使用方式)
- [來源與授權](#來源與授權)

## 快速選擇

| 想做的事 | 從這裡開始 |
|---|---|
| 找出不清楚的句子 | [清晰度修改 prompt](writing-revision/2604.11009-planning-to-revision/prompts/06-writing-clarity.en.txt) |
| 校對、擬大綱、寫初稿 | [寫作階段模板](writing-revision/2604.11009-planning-to-revision/) |
| 讓文字參考指定範文的風格 | [風格模仿方法與模板](style-imitation/2601.18353-good-writing/) |
| 設計角色成長與故事視角 | [Narrative Keyframing](story-generation/2608.10337-narrative-keyframing/) |
| 讀詩、引用文字並解釋效果 | [詩歌細讀指示](close-reading/2603.06855-poem-interpretation/prompts/close-reading-task.en.txt) |
| 看別人如何多輪修改故事或商品文案 | [使用者 prompt 紀錄](human-ai-cowriting/2604.03529-incentives/) |

## 寫作規劃與局部修訂

**[From Planning to Revision: How AI Writing Support at Different Stages Alters Ownership](writing-revision/2604.11009-planning-to-revision/)** · 雪梨大學、哥倫比亞大學、約翰霍普金斯大學、密西根大學 · 2026-04-13

把 AI 放在規劃、起草或修訂階段，研究寫作品質與心理所有權。起草組的品質增益最大；不能把這個結果當成每個修訂 prompt 都有效的證明。

[Paper](https://arxiv.org/abs/2604.11009) · [PDF](writing-revision/2604.11009-planning-to-revision/paper.pdf) · [Prompts](writing-revision/2604.11009-planning-to-revision/prompts/) · [使用說明](writing-revision/2604.11009-planning-to-revision/README.md)

## 範文與風格模仿

**[Can Good Writing Be Generative? Expert-Level AI Writing Emerges through Fine-Tuning on High-Quality Books](style-imitation/2601.18353-good-writing/)** · 密西根大學、石溪大學 · 2026-01-26

比較 20 段範文的 in-context prompting 與作家作品微調。只用 prompt 時，一般讀者對部分模型有較高偏好，專家整體仍偏好人類；專家偏好 AI 的主要優勢來自另外微調。

[Paper](https://arxiv.org/abs/2601.18353) · [PDF](style-imitation/2601.18353-good-writing/paper.pdf) · [Prompts](style-imitation/2601.18353-good-writing/prompts/) · [使用說明](style-imitation/2601.18353-good-writing/README.md)

## 角色與故事生成

**[Narrative Keyframing for Generative Creative Writing](story-generation/2608.10337-narrative-keyframing/)** · 康乃爾大學 · 2026-08-11

把劇情、角色特質和視角分成可控制的步驟，再生成第三人稱故事。人類評審較偏好多步驟流程產出的故事；比較對象也是 AI。

[Paper](https://arxiv.org/abs/2608.10337) · [PDF](story-generation/2608.10337-narrative-keyframing/paper.pdf) · [Prompts](story-generation/2608.10337-narrative-keyframing/prompts/) · [使用說明](story-generation/2608.10337-narrative-keyframing/README.md)

## 詩歌細讀與解釋

**[What Does AI Do for Cultural Interpretation? A Randomized Experiment on Close Reading Poems with Exposure to AI Interpretation](close-reading/2603.06855-poem-interpretation/)** · 芝加哥大學、杜克大學 · 2026-03-06

讀者先看預先生成的 AI 詩歌解讀，再自行分析文本。研究觀察到詮釋與寫作品質改善；它評估的是 AI 協助讀者的效果。

[Paper](https://arxiv.org/abs/2603.06855) · [PDF](close-reading/2603.06855-poem-interpretation/paper.pdf) · [Prompts](close-reading/2603.06855-poem-interpretation/prompts/) · [使用說明](close-reading/2603.06855-poem-interpretation/README.md)

## 人機共寫與多輪修改

**[Incentives Shape How Humans Co-Create with Generative AI](human-ai-cowriting/2604.03529-incentives/)** · 麻省理工學院 · 2026-04-04

短故事和商品簡介實驗公開參與者的實際提示紀錄。作者描述 AI 協助的技術品質較高，同時觀察到作品同質化；沒有單一標準寫作 prompt。

[Paper](https://arxiv.org/abs/2604.03529) · [PDF](human-ai-cowriting/2604.03529-incentives/paper.pdf) · [Prompts](human-ai-cowriting/2604.03529-incentives/prompts/) · [使用說明](human-ai-cowriting/2604.03529-incentives/README.md)

## 使用方式

1. 依用途選論文，打開該篇的 `prompts/`。檔名有 `adapted` 的是整理者改編；其餘來源和類型見各篇 README。
2. 將 `{draft}`、`{outline}` 或 `<character_name>` 等欄位替換為自己的內容；多步驟方法需按流程提供前一步輸出。
3. 閱讀各篇的比較對象與研究範圍。人機協作增益、AI 流程比較、一般讀者偏好及微調結果，不能合併成「只貼 prompt 就勝過人類」。

[CSV 清單](catalog.csv) · [JSON 清單](catalog.json) · [逐檔來源紀錄](sources.json) · [額外的中文局部修改模板](templates/)

## 目錄結構

```text
writing-revision/       規劃、起草與修訂
style-imitation/        20 段範文、風格說明與指定內容
story-generation/      角色特質、視角與敘事生成
close-reading/         詩歌細讀與文本解釋
human-ai-cowriting/     使用者提示紀錄與品質評分
templates/             另外整理的中文實用模板
```

每個論文資料夾包含 `README.md`、`paper.pdf` 與 `prompts/`。

## 來源與授權

論文、研究模板與資料保留各自的原始授權和作者歸屬，詳見 [ATTRIBUTION](ATTRIBUTION.md)。其中 From Planning to Revision 採 CC BY-NC-SA 4.0；詩歌細讀介面程式採 MIT。作家風格原始 prompts 的完整文學節錄保留於上游，這裡提供目錄與改編模板。

本合集整理與註解使用 AI 輔助，並依來源核對。版本固定為所列的 arXiv v1／v2；收錄範圍為本次選出的五篇，並非完整年度文獻回顧。

整理日期：2026-11-13。
