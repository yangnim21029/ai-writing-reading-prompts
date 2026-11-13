# 論文 Prompt 與短 Prompt 的產出對照

同一份 200–300 字的中文素材，分別使用研究公開的 prompt 與 AI 另外生成的短 prompt，觀察產出內容、修改方式與文字組織的差異。三種任務各執行兩輪，每輪包含兩個條件，共保留 12 份完整產出。

這些是本庫實際呼叫模型產生的示範，與原論文的實驗結果分開呈現。每一頁並排呈現兩邊全文，並附上實際使用的 prompt 與呼叫紀錄，供讀者自行比較。

## 三組對照

| 任務 | 素材字數 | 論文條件使用的模板 |
|---|---:|---|
| [清晰度修訂](clarity/) | 232 | From Planning to Revision，附錄 C.3.2 |
| [角色第一人稱敘事](narrative/) | 225 | Narrative Keyframing，附錄 A.5 |
| [詩歌細讀](close-reading/) | 235 | What Does AI Do for Cultural Interpretation? 的任務指示 |

## 比較方式

三份素材皆為本次示範撰寫的虛構文本。素材中的中文字數分別為 232、225、235，計數不含標點與空白。短 prompt 由 Gemini 在未接觸論文模板的另一個請求中產生，要求寫出有用、日常可使用的指令，限制為最多 35 個英文單字；實際為 26、29、28 個英文單字。[短 prompt 的生成紀錄](baseline-generation/)

每個條件以獨立、無對話歷史的 API 請求執行。兩邊使用相同素材、共用指示與請求設定，並要求繁體中文及 200–300 字的輸出。敘事案例的兩組都使用同一個 JSON 欄位。第一輪的 seed 為 20261113，第二輪為 20261114；所有成功輸出完整保留，沒有人工改寫或挑選較好的作品。

論文模板原本以英文寫成，本次填入中文素材並共同指定中文輸出。敘事案例只使用 Narrative Keyframing 附錄 A.5，並未重建整個多步驟流程；細讀案例也未重做原研究的真人閱讀實驗。各頁說明模板的填入方式與必要調整。

兩種 prompt 在格式、任務分解與約束上有所不同，這組示範並非只改變提示詞長度的實驗。三份素材、每種條件兩次生成，能呈現具體差異，尚不足以估計普遍勝率或宣稱重現論文成效。

## 模型與執行紀錄

請求使用的模型名稱是 `gemini-3.5-flash`，但服務端在全部 13 次成功呼叫中，包含短 prompt 的生成，皆回傳 `gemini-3.6-flash`。因此這批產出的實際模型依回傳紀錄標為 Gemini 3.6 Flash。

| 欄位 | 本次紀錄 |
|---|---|
| 執行日期 | 2026-11-13 |
| API | Gemini `generateContent` |
| 回傳模型 | `gemini-3.6-flash` |
| 每次候選回覆數 | 1 |
| 輸出 token 上限 | 8192 |
| 請求的 temperature / topP | 0.7 / 0.95；不視為有效抽樣控制，說明如下 |
| 工具與外部檢索 | 未使用 |
| 結果選取 | 每個條件的第一份成功完成回覆 |
| 服務錯誤 | 敘事第二輪的論文條件遇到一次 HTTP 503，以相同輸入和 seed 重試 |

[官方 API 文件](https://aistudio.google.com/api-reference/generate-content)說明，Gemini 3.6 Flash 起會忽略 temperature 與 topP。請求檔保留送出的值，但本庫不將它們當成已生效的控制量；相同 seed 也不保證日後能取得逐字相同的回覆。

每次呼叫保存 `request.json`、`response.json`、`output.txt` 與 `metadata.json`。回覆檔保留最後回答、模型版本、token 用量等欄位，未保存 API 憑證、內部思考文字或不透明的 thought signature。敘事頁面展示 JSON 的 `narration` 內容，原始 JSON 同時保留。

[逐次字數與 Token 紀錄](metrics.csv) · [完整設定](protocol.json) · [檔案雜湊](manifest.json) · [執行程式](../scripts/run_examples.py)

## 重新執行

在環境變數 `GEMINI_API_KEY` 已設定的環境中，從 repository 根目錄執行：

```bash
python3 scripts/run_examples.py replay --output-dir examples-rerun
```

程式會讀取已保存的 12 份請求，將新結果寫入另一個資料夾。原本的產出不會被覆寫。這會再次呼叫模型 API；後續的服務路由與模型版本可能與本次不同，應依新回覆的 metadata 核對。

[回到文獻目錄](../README.md)
