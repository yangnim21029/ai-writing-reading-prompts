# 文學風格模仿：範文提示、微調與人類評審的比較

這篇研究讓語言模型和人類作者使用相同的範文、風格描述與內容要求，模仿指定作家的敘事風格。研究分別測試了直接提供範文的 prompting，以及用作家作品微調模型。

論文為 *Can Good Writing Be Generative? Expert-Level AI Writing Emerges through Fine-Tuning on High-Quality Books*，作者是 Tuhin Chakrabarty（石溪大學）與 Paramveer S. Dhillon（密西根大學）。首次提交於 2026 年 1 月 26 日，本頁依據 arXiv:2601.18353v1。

## 人類作者和模型收到什麼材料

研究招募 28 位人類作者，其中 27 位正在就讀或已完成 MFA，另一位具有英文博士背景。他們從 50 位作家中選擇模仿對象，依指定內容寫出 200–450 個英文字的片段。每位作家由三位參與者模仿，共取得 150 份人類作品。任務已指定情節與內容，評估的是作者如何用文字呈現這些內容。

每份 prompt 包含 20 段作品節錄、研究者整理的風格特徵、待寫情節與字數要求。GPT-4o、Claude 3.5 Sonnet、Gemini 1.5 Pro 在 in-context prompting 條件中收到與人類相同的材料，沒有接受額外訓練。模型透過當次輸入中的例子模仿風格。

另一個條件選取其中 30 位作家，以其作品分別微調 GPT-4o。這會改變模型參數，所需資料和操作也與貼上 prompt 不同。論文標題中的專家層級表現來自這個條件。任務與兩種模型條件詳見原文第 3.1 節。

## 一般讀者與專家的評審結果

28 位專家評審與 131 位一般讀者參與盲評。寫作品質評估呈現同一內容的人類與 AI 版本；風格相似度評估另外提供原作者的作品作為參照。評審不知道版本的作者身分，每組作品由三位專家和五位一般讀者評閱，各群體再依多數決決定偏好。參與寫作的專家不評自己的作品。

下表是寫作品質的 AI 配對勝率，來自附錄 A.2。勝率表示評審偏好 AI 版本的比例。

| 模型條件 | 一般讀者的 AI 勝率 | 專家評審的 AI 勝率 |
|---|---:|---:|
| GPT-4o，僅使用 prompt | 66% | 12% |
| Claude 3.5 Sonnet，僅使用 prompt | 56% | 30% |
| Gemini 1.5 Pro，僅使用 prompt | 44.9% | 10% |
| GPT-4o，另行微調 | 68.9% | 62.2% |

一般讀者較常偏好 GPT-4o 與 Claude 的 prompting 版本，專家則較常偏好人類作者。GPT-4o 微調後，在專家評審中的勝率為 62.2%；把這個數字當成公開 prompt 的效果，會混淆兩種實驗條件。微調只涵蓋 30 位作家，兩組結果的任務範圍也不同。

本研究評估文學寫作品質與風格相似度，沒有測量讀者理解、文字簡化或改寫後的語意保留。模仿某位作家的句式、敘事聲音和細節選擇，是否能讓特定讀者讀得更懂，需要另行評估。

## Prompt 的內容與填入方式

作者公開了 50 位作家的完整 prompt，每份都含 20 段範文及指定寫作內容。以 Virginia Woolf 的檔案為例，風格說明包含意識流，情節指定 Clarissa Dalloway 出門買花，並從當下感受轉入回憶，最後要求寫出 270 個英文字的片段。研究中的模仿任務因此同時受範文、風格描述、情節與篇幅限制。

下方是本庫依這個結構另行撰寫的填空模板，檔名標記為 `adapted`。它保留「範文、風格、內容、字數」四部分，未轉載原始文學節錄，也未作為獨立條件接受論文的成效檢驗。作者實際使用的 50 份完整檔案，可由頁尾的官方 prompt 目錄開啟。

| 欄位 | 要填入的內容 |
|---|---|
| `{sample_1}` 至 `{sample_20}` | 同一寫作風格的 20 段範文；中間省略標記要換成第 3–19 段實際內容 |
| `{style_features}` | 要模仿的風格特徵，例如句式、敘述視角、語氣與細節選擇 |
| `{content_brief}` | 新片段必須呈現的人物、事件與情節 |
| `{word_count}` | 要求的英文單字數 |

```text
Study the following 20 writing samples for their style and narrative voice.

[WRITING SAMPLES]
Sample 1: {sample_1}
Sample 2: {sample_2}
... supply all samples through Sample 20 ...
Sample 20: {sample_20}

[STYLE FEATURES]
{style_features}

[REQUIRED CONTENT]
{content_brief}

Write a passage of {word_count} words that presents the required content using the style and narrative voice demonstrated by the samples and described in the style features.
```

使用時先準備範文與待寫情節，再替換各欄位。範文負責示範文字如何寫，內容要求則指定這次要寫什麼。換成自己的範文或中文材料後，便改變了原研究的輸入條件；本庫目前沒有為這份改編模板製作與短 prompt 的產出對照。

## 論文與原始檔案

- [論文 PDF](paper.pdf)：本庫保存的 arXiv:2601.18353v1。
- [arXiv 全文與附錄](https://arxiv.org/html/2601.18353v1)：第 3 節交代寫作與評審任務，附錄 A.2 列出各模型的分項結果。
- [50 位作家的官方 prompt 目錄](upstream-prompts.md)：連至作者公開的完整檔案，包含文學節錄、風格描述與內容要求。

論文採 CC BY 4.0。上方改編模板另存於 `prompts/style-imitation.adapted.en.txt`；文學節錄保留於上游。作者歸屬與檔案來源記錄於 repository 根目錄的 `ATTRIBUTION.md` 和 `sources.json`。更新日期：2026-11-13。
