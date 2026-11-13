# Can Good Writing Be Generative? Expert-Level AI Writing Emerges through Fine-Tuning on High-Quality Books

Tuhin Chakrabarty、Paramveer S. Dhillon<br>
石溪大學、密西根大學<br>
首次提交：2026-01-26 · 收錄版本：arXiv:2601.18353v1

[論文 PDF](paper.pdf) · [HTML 全文](https://arxiv.org/html/2601.18353v1) · [作者 GitHub](https://github.com/tuhinjubcse/GoodWritingBeGenerative) · [回到目錄](../../README.md)

## 風格模仿任務與兩種模型條件

研究招募 28 位人類作者，其中 27 位正在就讀或已完成 MFA，另一位具有英文博士背景。作者與語言模型依指定內容，模仿 50 位作家的敘事風格，寫出 200–450 個英文字的片段。這項任務已經指定情節與內容，評估重點在文字如何呈現這些內容。

In-context prompting 條件提供 20 段範文、風格特徵、待寫內容與字數要求。人類作者與 GPT-4o、Claude 3.5 Sonnet、Gemini 1.5 Pro 收到相同的寫作材料。模型在這個條件中沒有接受額外訓練。另一個 fine-tuning 條件則選取其中 30 位作家，以其作品分別微調 GPT-4o。[寫作任務與模型條件](https://arxiv.org/html/2601.18353v1#S3.SS1)

28 位專家評審與 131 位一般讀者參與盲評，分別判斷寫作品質與風格相似度。每組人類與 AI 作品由三位專家、五位一般讀者評閱，再分別依多數決決定偏好；作者不評自己的作品。[評估設計](https://arxiv.org/html/2601.18353v1#S3.SS2.SSS2)

## 寫作品質的評審結果

下列百分比是各評審群體對 AI 作品的配對勝率，反映偏好判斷，並非文章正確率。

| 模型條件 | 一般讀者的 AI 勝率 | 專家評審的 AI 勝率 |
|---|---:|---:|
| GPT-4o，僅使用 prompt | 66% | 12% |
| Claude 3.5 Sonnet，僅使用 prompt | 56% | 30% |
| GPT-4o，另行微調 | 68.9% | 62.2% |

表中節錄與 prompt 使用及微調差異直接相關的結果；Gemini 1.5 Pro 與其他分項見[附錄 A.2](https://arxiv.org/html/2601.18353v1#A1.SS2)。僅使用 prompt 的條件中，兩類評審對作品品質的判斷差異很大。論文標題中的專家層級表現涉及微調結果，不能由公開的寫作 prompt 單獨重現。

這篇研究沒有把閱讀理解、文字簡化或改寫後的語意保留列為成效指標。若要評估風格模仿能否改善可讀性，仍需要另外設定讀者、文本與評量方式。

## 公開 Prompt 與本庫收錄方式

[官方 Prompt 目錄](upstream-prompts.md)列出 50 位作家的原始檔。每份檔案包含 20 段作品節錄、作者風格說明、指定情節與寫作要求。以 [Virginia Woolf 的原始檔](https://github.com/tuhinjubcse/GoodWritingBeGenerative/blob/main/Writing_Prompts/Virginia_Woolf.txt)為例，研究提供意識流等風格描述，以及 Clarissa Dalloway 出門買花、由當下感受轉入回憶的情節，最後要求寫出 270 個英文字的片段。

本庫的[英文填空模板](prompts/style-imitation.adapted.en.txt)保留「範文—風格—內容—字數」的結構，由整理者另行撰寫，並以 `adapted` 標記。它未包含原始文學節錄，也不是原作者的完整實驗 prompt。需要檢查研究實際如何安排範文與內容時，應使用上述官方檔案。

論文採 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。完整文學節錄保留於上游；作者歸屬與本庫改編內容見 [ATTRIBUTION](../../ATTRIBUTION.md)。整理日期：2026-11-13。
