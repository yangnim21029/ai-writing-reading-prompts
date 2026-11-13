# What Does AI Do for Cultural Interpretation? A Randomized Experiment on Close Reading Poems with Exposure to AI Interpretation

Jiayin Zhi、Hoyt Long、Richard Jean So、Mina Lee<br>
芝加哥大學、杜克大學<br>
首次提交：2026-03-06 · 收錄版本：arXiv:2603.06855v1

[論文 PDF](paper.pdf) · [HTML 全文](https://arxiv.org/html/2603.06855v1) · [研究介面程式](https://github.com/xxxxbrandieeee/close-reading-interface) · [回到目錄](../../README.md)

## AI 解讀如何影響讀者的文本分析

研究採隨機實驗，最終納入 400 位參與者。每位參與者閱讀三首詩，並被分配至無 AI 解讀、單份 AI 解讀或三份 AI 解讀的條件。研究測量其後完成的詩歌分析，以及主觀閱讀體驗。

單份解讀由 GPT-4o 依與參與者完全相同的任務指示產生；多份解讀則要求模型提出三種不同分析，指出不同文本特徵並解釋其效果。研究人員先以相同評分規準檢查 AI 解讀，再將內容放入實驗介面，因此參與者接觸的是預先準備的閱讀材料。[AI 材料製作](https://arxiv.org/html/2603.06855v1#S3.SS1.SSS5)

兩位受訓評分者從三個面向評估參與者的回答：文本特徵辨認是否正確、詮釋是否深入，以及表達是否清楚連貫。後兩項皆採 1–5 分量尺。相較於無 AI 組，單份 AI 解讀組的詮釋品質增加 0.865 分，寫作品質增加 1.035 分，兩項皆為 p < .001。[評分方法](https://arxiv.org/html/2603.06855v1#S3.SS2.SSS1)；[效果估計](https://arxiv.org/html/2603.06855v1#S4.SS1.SSS1)

這些分數反映讀者閱讀 AI 解讀之後的表現。它們不等於 AI 單獨作答勝過人類的比例，也無法直接套用到未經檢查的即時聊天回覆。

## 細讀任務的 Prompt

[close-reading-task.en.txt](prompts/close-reading-task.en.txt) 擷取自研究介面 `pageInfo.ts` 的 `page5_1.left_top_instruction`。檔案移除 HTML 標籤，保留原始任務文字，包括左右文字框的作答指示。

這份 prompt 要求分析者選取三類文本特徵。各類都須先指出具體例子，再以 2–3 句話解釋其作用。

| 分析對象 | 任務要求 |
|---|---|
| 特殊用字或片語 | 找出顯著、刻意或不尋常的語言使用 |
| 詩人的聲音或視角 | 找出能呈現詩人立場或自我表現的詩句 |
| 詩歌形式與風格 | 分析重複、節奏、押韻、聲音或視覺排列等特徵 |

作答需要短引文或明確的文本位置，並說明該特徵為何突出、詩人可能為何採用它，以及預期對讀者產生什麼效果。這使 prompt 的任務從一般的內容摘要轉向有文本依據的詮釋。

論文 §3.1.5 明確說明，單份 AI 解讀使用與參與者相同的任務指示；本庫依這項方法記述收錄上述指示。若將它移到一般聊天介面，需一併提供詩文，並調整「左右文字框」的輸出要求。本庫未收錄完整的多份解讀生成與審核流程。

論文採 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)；上述介面程式與擷取指示採 [MIT](prompts/LICENSE-MIT.txt)。作者歸屬見 [ATTRIBUTION](../../ATTRIBUTION.md)。整理日期：2026-11-13。
