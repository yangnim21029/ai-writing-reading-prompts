# 角色與故事生成

**Narrative Keyframing for Generative Creative Writing**

作者：Chao Zhang；Abe Davis

機構：康乃爾大學

arXiv：2608.10337v1 · 首次提交：2026-08-11

[PDF](paper.pdf) · [arXiv](https://arxiv.org/abs/2608.10337) · [HTML 全文](https://arxiv.org/html/2608.10337v1) · [回到總目錄](../../README.md)

## 用途與證據

把劇情、角色特質和視角分成可控制的步驟，再生成第三人稱故事。人類評審較偏好多步驟流程產出的故事；比較對象也是 AI。

**比較對象：** 多步驟 AI 流程 vs. 一般大綱 AI 流程

**使用方式：** 按附錄 A 的順序選用角色特質、特質插值、第一人稱視角、證據擷取、第三人稱故事與細節整合。先填好各模板的尖括號欄位。

**研究範圍：** 這是相互連接的生成流程。部分模板要求外部 JSON schema，附錄摘錄未完整提供 schema，執行時需補上；不能只貼一段就宣稱重現整套方法。

[結果定位](https://arxiv.org/html/2608.10337v1#S6.SS1)

## Prompts

英文原文檔可直接開啟。從論文 HTML 擷取的模板僅整理排版；改編模板另有標記。

| 檔案 | 類型 | 來源 |
|---|---|---|
| [01-physiology.en.txt](prompts/01-physiology.en.txt) | 原始任務模板 | [原始位置](https://arxiv.org/html/2608.10337v1#A1.SS1) |
| [02-psychology.en.txt](prompts/02-psychology.en.txt) | 原始任務模板 | [原始位置](https://arxiv.org/html/2608.10337v1#A1.SS2) |
| [03-sociology.en.txt](prompts/03-sociology.en.txt) | 原始任務模板 | [原始位置](https://arxiv.org/html/2608.10337v1#A1.SS3) |
| [04-character-interpolation.en.txt](prompts/04-character-interpolation.en.txt) | 原始任務模板 | [原始位置](https://arxiv.org/html/2608.10337v1#A1.SS4) |
| [05-first-person.en.txt](prompts/05-first-person.en.txt) | 原始任務模板 | [原始位置](https://arxiv.org/html/2608.10337v1#A1.SS5) |
| [06-evidence.en.txt](prompts/06-evidence.en.txt) | 原始任務模板 | [原始位置](https://arxiv.org/html/2608.10337v1#A1.SS6) |
| [07-third-person-1.en.txt](prompts/07-third-person-1.en.txt) | 原始任務模板 | [原始位置](https://arxiv.org/html/2608.10337v1#A1.SS7) |
| [07-third-person-2.en.txt](prompts/07-third-person-2.en.txt) | 原始任務模板 | [原始位置](https://arxiv.org/html/2608.10337v1#A1.SS7) |

## 來源與授權

論文 PDF：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，保留原始檔案。原始 prompt 與資料依各來源授權；詳細歸屬見 [ATTRIBUTION](../../ATTRIBUTION.md)。

整理日期：2026-11-13。
