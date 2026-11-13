# From Planning to Revision: How AI Writing Support at Different Stages Alters Ownership

Katy Ilonka Gero、Tao Long、Carly Schnitzler、Paramveer S. Dhillon<br>
雪梨大學、哥倫比亞大學、約翰霍普金斯大學、密西根大學<br>
首次提交：2026-04-13 · 收錄版本：arXiv:2604.11009v2

[論文 PDF](paper.pdf) · [HTML 全文](https://arxiv.org/html/2604.11009v2) · [原始 Prompts 附錄](https://arxiv.org/html/2604.11009v2#A3) · [回到目錄](../../README.md)

## AI 介入寫作階段的實驗

這項研究探討 AI 在何時介入寫作，會如何影響文章品質，以及作者對文章的心理所有權（psychological ownership）。研究者以「我覺得這篇文章真正屬於我」等作答衡量後者，將它與文章品質分開分析。

最終樣本包含 253 位參與者，隨機分配至四組。所有人都完成規劃、起草與修訂；AI 支援只出現在指定階段。規劃組可以向 GPT-4o 索取論點與大綱，起草組先自己寫大綱，再取得 AI 初稿並自行修訂，修訂組則先自行完成初稿，再使用校對、清晰度與論證工具。對照組全程不使用 AI。[實驗條件](https://arxiv.org/html/2604.11009v2#S3.SS3)

文章依論證品質、連貫性、詞彙與文法評分，總指標為三項分數的平均，範圍 0–9。研究先由英文教師評閱部分文章，再以其中的樣本校準獨立的 o4-mini 評分程序，並在保留樣本上檢查一致性。下表是控制題目、文章字數與作答時間後的調整平均數。[評分方法](https://arxiv.org/html/2604.11009v2#S4.SS1)

| 實驗條件 | 調整後品質分數 |
|---|---:|
| 無 AI | 5.69 |
| AI 協助規劃 | 5.85 |
| AI 依大綱起草 | 7.27 |
| AI 提供修訂建議 | 5.79 |

三種 AI 條件的平均分數比無 AI 高 0.62 分；起草組比另外兩種 AI 條件的平均高 1.45 分，兩項預先規劃的比較皆為 p < .001。起草組也出現最大的心理所有權下降。研究因此同時呈現了品質提升與作者主觀歸屬感之間的取捨。[結果 §5.4](https://arxiv.org/html/2604.11009v2#S5.SS4)

## 各份 Prompt 在實驗中的作用

七份檔案擷取自附錄 C，保留英文措辭與變數，只移除 HTML 排版。它們對應不同實驗條件，並非要求依序執行的七個步驟。

| Prompt | 輸入與任務 | 原文位置 |
|---|---|---|
| [提出三種論點](prompts/01-thesis-ideas.en.txt) | 根據 `{promptText}` 提出支持、反對與較細緻的替代立場 | [C.1.1](https://arxiv.org/html/2604.11009v2#A3.SS1.SSS1) |
| [追加論點](prompts/02-more-thesis-ideas.en.txt) | 根據題目與 `{existingIdeas}` 提出一個不重複的新論點 | [C.1.2](https://arxiv.org/html/2604.11009v2#A3.SS1.SSS2) |
| [建立大綱](prompts/03-outline.en.txt) | 依題目及 `{idea}` 組織論證結構 | [C.1.3](https://arxiv.org/html/2604.11009v2#A3.SS1.SSS3) |
| [依大綱起草](prompts/04-draft.en.txt) | 依 `{promptText}` 與 `{outline}` 生成約 300 個英文字的初稿 | [C.2.1](https://arxiv.org/html/2604.11009v2#A3.SS2.SSS1) |
| [校對文法與標點](prompts/05-proofreading.en.txt) | 從 `{draft}` 指出 2–3 處較重要的錯誤，提供替換文字 | [C.3.1](https://arxiv.org/html/2604.11009v2#A3.SS3.SSS1) |
| [修訂不清楚的片段](prompts/06-writing-clarity.en.txt) | 引用 2–3 處不清楚的原文，說明問題並提供更清楚的替換文字 | [C.3.2](https://arxiv.org/html/2604.11009v2#A3.SS3.SSS2) |
| [改善論證](prompts/07-argument-improvement.en.txt) | 指出論證弱點；需要補充內容時，提供新增文字與插入位置 | [C.3.3](https://arxiv.org/html/2604.11009v2#A3.SS3.SSS3) |

清晰度模板要求逐字引用待改片段，是為了讓研究介面能定位並替換原文。這項輸出規則本身並不等於語意保留的評估：研究沒有另行測量修改後是否完整保留作者原意。修訂組也同時擁有三種工具，因此不能從組別結果推算某一份模板的獨立效果。

改用時可替換模板中的變數；若改變語言、文章長度或模型，便改變了原研究條件。論文的寫作任務為 200–300 個英文字的議論文，原始起草 prompt 要求約 300 個英文字。

論文與附錄 prompts 採 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)。作者歸屬與擷取紀錄見 [ATTRIBUTION](../../ATTRIBUTION.md) 與 [sources.json](../../sources.json)。整理日期：2026-11-13。
