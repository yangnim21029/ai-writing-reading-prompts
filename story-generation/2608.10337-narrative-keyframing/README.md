# Narrative Keyframing for Generative Creative Writing

Chao Zhang、Abe Davis<br>
康乃爾大學<br>
首次提交：2026-08-11 · 收錄版本：arXiv:2608.10337v1

[論文 PDF](paper.pdf) · [HTML 全文](https://arxiv.org/html/2608.10337v1) · [原始 Prompts 附錄](https://arxiv.org/html/2608.10337v1#A1) · [回到目錄](../../README.md)

## 以角色狀態控制故事生成

Narrative Keyframing 讓作者指定角色在不同劇情段落中的狀態，包括外在特徵（physiology）、心理特徵（psychology）與社會關係（sociology）。這些設定構成 character keyframes。系統依角色狀態生成第一人稱敘述，再從敘述中擷取能支持角色特質的文字細節，供第三人稱故事生成與修訂使用。

Prompt 在這個方法中分別負責角色設定、視角生成、證據擷取與敘事整合。先生成的第一人稱敘述是後續寫作的材料；使用者可以選擇特質與文本細節，決定哪些內容進入故事。[系統設計](https://arxiv.org/html/2608.10337v1#S5)

## 與一般大綱擴寫的比較

技術評估採用 20 個寫作題目，每題生成五份大綱，共得到 100 組故事。兩個條件使用相同的 GPT-4.1 和大綱：實驗條件執行 Narrative Keyframing 流程，對照條件以一般 prompt 擴寫大綱。這個設計比較的是生成方法。

作者另從中隨機抽取 30 組故事，請三位具專業寫作經驗的評審盲評。每組由三人多數決判斷，結果如下。[評估方法](https://arxiv.org/html/2608.10337v1#S6.SS1.SSS1)

| 評估面向 | 多數評審偏好 Narrative Keyframing 的組數 |
|---|---:|
| 整體故事品質 | 25／30（83.3%） |
| 角色刻畫豐富度 | 29／30（96.7%） |

評審常指出，多步驟流程帶入較具體的動作、外貌與心理細節；部分評語則偏好對照故事較簡潔的句子與節奏。增加角色細節的效果因此應與閱讀流暢度一起考察。這項比較未納入人類獨立創作的故事。[結果與評語](https://arxiv.org/html/2608.10337v1#S6.SS1.SSS2)

## Prompt 檔案與流程位置

八份檔案擷取自附錄 A。英文原文、條件分支與變數均保留，只移除網頁排版。

| Prompt | 在方法中的作用 | 原文位置 |
|---|---|---|
| [外在特徵建議](prompts/01-physiology.en.txt) | 依大綱、當前劇情與已有特質，提出外貌、衣著或肢體表現 | [A.1](https://arxiv.org/html/2608.10337v1#A1.SS1) |
| [心理特徵建議](prompts/02-psychology.en.txt) | 提出情緒、動機、信念等角色設定 | [A.2](https://arxiv.org/html/2608.10337v1#A1.SS2) |
| [社會特徵建議](prompts/03-sociology.en.txt) | 提出角色的社會位置、關係與互動特徵 | [A.3](https://arxiv.org/html/2608.10337v1#A1.SS3) |
| [推定中間段落的角色特質](prompts/04-character-interpolation.en.txt) | 從當前敘述擷取特質，必要時參考相鄰段落的角色設定，並附文字證據 | [A.4](https://arxiv.org/html/2608.10337v1#A1.SS4) |
| [第一人稱視角生成](prompts/05-first-person.en.txt) | 依劇情與角色設定撰寫該角色的敘述，限制為最多 200 個英文字 | [A.5](https://arxiv.org/html/2608.10337v1#A1.SS5) |
| [擷取角色特質的文本證據](prompts/06-evidence.en.txt) | 找出能支持指定特質的逐字引文 | [A.6](https://arxiv.org/html/2608.10337v1#A1.SS6) |
| [生成第三人稱故事](prompts/07-third-person-1.en.txt) | 依大綱、主要角色與幕次展開故事 | [A.7](https://arxiv.org/html/2608.10337v1#A1.SS7) |
| [整合選定的角色細節](prompts/07-third-person-2.en.txt) | 將選定細節寫入原故事，保留劇情、事件次序與第三人稱敘述 | [A.7](https://arxiv.org/html/2608.10337v1#A1.SS7) |

原文中的 `If...` 描述介面依資料有無採用的條件分支。改用時需依實際輸入選擇段落，填入 `<full_outline>`、`<current_plot>`、`<character_name>` 等變數。部分模板要求回傳符合外部 JSON schema 的資料，而這些摘錄未完整附上 schema；若要重建程式流程，還需要補齊輸出結構與各步驟間的資料傳遞。

論文與附錄 prompts 採 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。作者歸屬與擷取紀錄見 [ATTRIBUTION](../../ATTRIBUTION.md) 與 [sources.json](../../sources.json)。整理日期：2026-11-13。
