# 寫作規劃、起草與修訂：七份研究提示詞與實際產出

這篇研究把 AI 支援放在規劃、起草或修訂其中一個階段，觀察文章品質與寫作者對文章的歸屬感如何改變。研究者公開了七份 prompt，涵蓋提出論點、建立大綱、依大綱起草，以及針對文法、清晰度和論證提供修改建議。下文收錄全部原文，並用同一段中文素材展示清晰度 prompt 與一般短 prompt 的完整回覆。

論文為 *From Planning to Revision: How AI Writing Support at Different Stages Alters Ownership*。作者是 Katy Ilonka Gero（雪梨大學）、Tao Long（哥倫比亞大學）、Carly Schnitzler（約翰霍普金斯大學）與 Paramveer S. Dhillon（密西根大學）。首次提交於 2026 年 4 月 13 日，本頁依據 arXiv:2604.11009v2，版本日期為 2026 年 6 月 11 日。

## 研究怎麼做，結果如何

研究者透過 Prolific 招募居住於美國、英國或澳洲、能使用英文的成年人，請他們完成短篇議論文。任務說明要求 200–300 個英文字，流程依序為規劃、起草與修訂。研究者隨機分配 AI 支援條件，排除違反實驗規定的提交後，分析 253 位參與者的資料。

四組都經過相同的寫作階段。規劃組可以請 GPT-4o 提出論點與大綱，之後自行寫作和修訂；起草組先自己寫大綱，再取得一份 AI 初稿，最後自行修訂；修訂組先自行完成大綱與初稿，再使用校對、清晰度和論證工具。對照組全程自行寫作。這些功能以 prompt 呼叫 GPT-4o，使用下方模板不需要先訓練或微調模型。

研究分別評估文章品質與心理所有權（psychological ownership）。品質採用改編自 IELTS 的評分規準，涵蓋論證、連貫與銜接、詞彙與文法三項，總分為三項平均，範圍 0–9。英文教師先評閱 50 篇文章；研究者用其中 30 篇校準 o4-mini 評分程序，再以另外 20 篇檢查一致性。心理所有權則由參與者回答「我覺得這篇文章真正屬於我」，以 1–7 分量尺衡量。

| 實驗條件 | 人數 | 文章品質（0–9） | 心理所有權（1–7） |
|---|---:|---:|---:|
| 全程自行寫作 | 60 | 5.69 | 6.74 |
| AI 協助規劃 | 66 | 5.85 | 6.30 |
| AI 依大綱起草 | 66 | 7.27 | 4.29 |
| AI 提供修訂建議 | 61 | 5.79 | 5.57 |

表內為調整後平均數。品質分數控制了寫作題目、文章字數與作答時間；心理所有權分數控制了寫作題目。三種 AI 條件的平均品質比對照組高 0.62 分，起草組比規劃與修訂兩組的平均高 1.45 分，兩項預先規劃的比較皆為 p < .001。規劃與修訂兩組的品質差異未達統計顯著。心理所有權的方向相反：起草組比規劃與修訂兩組的平均低 1.65 分，p < .001。研究設計、評分和結果分別見原文第 3 節、第 4.1 節及第 5 節。

這些數字來自有時間限制的英文議論文任務。起草組只能取得一次 AI 初稿，規劃與修訂組則可反覆索取論點或修訂建議，因此各組也存在互動方式上的差異。作者在第 8 節指出，這類題目與評分規準可能偏重模型擅長的文字流暢度；專業寫作、個人敘事或需要查證資料的文章，仍須另外研究。

修訂組同時擁有三種工具，研究沒有分別估計每份修訂 prompt 的獨立效果，也沒有另行評估修改是否完整保留作者原意。下方的清晰度模板要求逐字引用原文，目的是讓介面找到可以替換的位置。

## 七份 prompt 的完整原文與用法

以下英文內容取自附錄 C，保留原始措辭、格式要求與變數，只移除論文的 HTML 排版。七份模板分屬不同階段，可以依手上的工作選用。原實驗中的每位參與者只會取得分配到的那一組工具。

使用時，複製需要的模板，把大括號連同其中的變數名稱換成實際內容。變數的對應如下。

| 變數 | 要填入的內容 |
|---|---|
| `{promptText}` | 議論文題目或寫作要求 |
| `{existingIdeas}` | 已經產生的論點，供模型避開重複內容 |
| `{idea}` | 選定的主要論點 |
| `{outline}` | 文章大綱 |
| `{draft}` | 要檢查的文章全文 |

規劃和起草模板以約 300 個英文字的議論文為前提；原文中的 `words` 也是英文單字數。若改成中文、長篇文章或其他模型，這些設定需要自行調整。下方保留英文原文，方便辨認哪些要求來自論文。

### 1. 提出三種論點

附錄 C.1.1。填入題目後，模型需提出支持、反對與較細緻的替代立場，各用 10–15 個英文單字表達。輸出只列出論點，不加開場說明，也不標示哪一項是支持或反對。原介面用這份模板提供第一批構想。

```text
I am planning to write a 300 word argumentative essay on the topic: {promptText}.
Please give me 3 distinct thesis ideas for this essay:
- The first should argue in favor of the topic (pro position)
- The second should argue against the topic (con position)
- The third should be a nuanced or alternative perspective

Each idea must be extremely concise (10-15 words maximum) and make a clear argument.

Format your response with bullet points.

Do not include any additional explanation text before or after the bullet points.
Do not indicate which ideas are pro or con.
```

### 2. 再提出一個不同的論點

附錄 C.1.2。需要更多構想時，填入相同題目及先前已產生的論點。模板要求避開重複或相近內容，一次只回傳一個 10–15 個英文單字的論點。

```text
Generate a single interesting thesis statement for a 300-word argumentative essay on the topic: {promptText}.
The statement must be extremely concise (10-15 words maximum) and make a clear argument.

Here are the existing ideas that have already been generated (DO NOT repeat these or anything similar):
{existingIdeas}

Provide ONLY the thesis statement with no additional text, introduction, or explanation.
```

### 3. 把選定的論點整理成大綱

附錄 C.1.3。填入題目和選定的論點，要求模型安排引言、兩到三個主要論點及結論。大綱最多 20 行，每個主要論點不超過 15 個英文單字，使用單層條列。

```text
Create a very concise outline for a 300-word argumentative essay on this topic: {promptText}
The main thesis/idea is: {idea}

The outline must be extremely brief (no more than 20 lines total) with minimal formatting:
- One short introduction point
- 2-3 main points (no more than 15 words each)
- One short conclusion point

Use simple bullet points only. No sub-bullets or complex formatting.
```

### 4. 依大綱寫出完整初稿

附錄 C.2.1。填入題目與大綱，模型便依大綱寫出約 300 個英文字的文章。原研究的起草組先自行完成大綱，再使用這份模板生成初稿；之後由參與者修訂。

```text
Please write a complete draft essay based on this outline and prompt.

Prompt: {promptText}

Outline:
{outline}

Please create a well-structured essay of approximately 300 words that follows this outline.
```

### 5. 校對拼字、文法與標點

附錄 C.3.1。填入文章全文，模型需找出兩到三處較重要的錯誤，逐項引用原文、簡述問題，並提供可直接替換的文字。若建議刪除，`Fix` 回傳空字串；沒有錯誤時，回傳 `No issues found`。引用必須與原文完全相同，供研究介面定位。

```text
Please briefly review the following essay for the most critical typos, grammatical mistakes, and punctuation issues:

{draft}

Identify only 2-3 of the most important issues. For each issue:
1. Number the issue (Issue 1, Issue 2, etc.)
2. Quote the problematic phrase EXACTLY as it appears in the text (keep it under 10 words), using "double quotes".
3. Very briefly explain the problem in 5-10 words.
4. Suggest a concise fix. The Fix must be a direct replacement for the quoted text, with no instructions, options, or meta-comments. If the fix is to delete the text, return an empty string.

Format as:
### Issue 1
> "problematic text"
>
> **Issue**: Brief explanation
>
> **Fix**: "corrected version"

Be extremely concise. Only identify actual errors.
The quoted "problematic text" must appear EXACTLY as written in the original text - copy and paste the exact words, do not paraphrase or modify. This is critical for the tool to work properly.
If there are no issues, return "No issues found".
```

### 6. 修改表達不清楚的片段

附錄 C.3.2。這份模板把檢查目標改為清晰度，要求選出兩到三處最不清楚的片段。每一項都要附原文、問題說明與可直接替換的文字，並限制引用與說明的長度。後面的中文示範使用這份原文，只替換 `{draft}`，另加兩組共用的語言與篇幅要求。

```text
Please briefly review the following essay for the most unclear passages:

{draft}

Identify only 2-3 of the most problematic passages. For each issue:
1. Number the issue (Issue 1, Issue 2, etc.)
2. Quote the unclear phrase EXACTLY as it appears in the text (keep it under 10 words), using "double quotes".
3. Very briefly explain the clarity issue in 5-10 words.
4. Suggest a clearer alternative. The Fix must be a direct replacement for the quoted text, with no instructions, options, or meta-comments. If the fix is to delete the text, return an empty string.

Format as:
### Issue 1
> "unclear text"
>
> **Issue**: Brief explanation
>
> **Fix**: "clearer version"

Be extremely concise. Focus only on clarity issues.
The quoted "unclear text" must appear EXACTLY as written in the original text - copy and paste the exact words, do not paraphrase or modify. This is critical for the tool to work properly.
```

### 7. 指出論證弱點，提供補強內容

附錄 C.3.3。模型需引用與問題相關的原文，說明論證弱點，並給出具體建議。若建議涉及新增內容，還要提供兩到六個英文單字的按鈕標籤、一到三句新增文字，以及插入位置。位置可以指定段落，也可以引用完整句子，表示新增內容應接在哪一句之後。這些欄位配合原研究的編輯介面；直接在聊天工具中使用時，也會出現在回覆裡。

```text
Please briefly review the following essay for the most significant argument weaknesses:

{draft}

Identify only 2-3 of the most important argument issues. For each issue:
1. Number the issue (Issue 1, Issue 2, etc.)
2. Quote the relevant text that indicates approximately where the problem is (keep it under 15 words), using "double quotes". Quote a phrase EXACTLY as it appears in the text - copy and paste the exact words, do not paraphrase or modify.
3. Very briefly describe the argument weakness.
4. Provide a specific, actionable suggestion with concrete examples or specific steps.
5. If your suggestion involves adding new content, provide:
- **Addition label**: a short (2-6 words) summary for a button label, e.g., ’add examples and case studies’, ’add limitations’, or ’add concrete examples’.
- **Addition text**: the exact text to add (1-3 sentences).
- **Insertion point**: a clear description of where to insert it. Use one of these formats:
* ’After the sentence: "COMPLETE_SENTENCE"’ - quote the ENTIRE sentence exactly as it appears in the text, from capital letter to period/question mark/exclamation mark
* ’After paragraph X’ - where X is the paragraph number (1, 2, 3, etc.)
If your suggestion does not involve adding new content, leave these fields blank.

Format as:
### Issue 1
> "relevant text for improvement"
>
> **Issue**: Brief description of the argument weakness
>
> **Suggestion**: Specific, actionable advice with concrete examples or steps
>
> **Addition label**: add concrete examples
>
> **Addition text**: For instance, recent studies have shown that...
>
> **Insertion point**: After the sentence: "The argument lacks supporting evidence."

Be extremely concise. Focus only on argument quality and logic. For suggestions, provide specific examples, steps, or concrete details rather than general advice. The quoted text must appear EXACTLY as written in the original text - this is critical for the tool to work properly.

IMPORTANT: When using "After the sentence:" format, you MUST quote the COMPLETE sentence exactly as it appears in the text, from the first capital letter to the final punctuation mark. Do not truncate or abbreviate the sentence.
```

## 清晰度 prompt 與一般短 prompt 的實際回覆

以下由本庫於 2026 年 11 月 13 日另行呼叫模型產生，使用一段虛構的圖書館試辦報告。素材共有 232 個中文字，計數不含標點與空白。

> 本館上學期試辦延長夜間開放，原先希望讓白天無法到館的學生也能使用空間，但後來的調查發現，表示滿意的人主要是原本就常來的學生，因此這項措施對新使用者的幫助可能沒有預期多。問卷共有八十人回覆，其中六十人曾在晚上使用圖書館，不過這不表示晚上到館的人有四分之三都滿意，因為兩個問題的回答並不一樣。館員認為繼續辦理有其必要，但如果沒有增加人力，延長的部分會影響原來工作，所以建議先保留每週兩天，再觀察一學期。這個安排並不是否定學生的需求，而是在目前條件下，讓服務能夠持續，同時也需要把沒有來的人為何沒來弄清楚。

短 prompt 由 Gemini 在未接觸論文模板的另一個請求中產生，要求寫出日常可用的修訂指令，最多 35 個英文單字。實際使用的指令如下，後面接上同一份素材。

```text
Identify vague phrasing, logical gaps, and awkward structure in the attached text. Provide specific revision suggestions to enhance readability, flow, and overall precision of the message.
```

論文條件使用上方第 6 份模板，把 `{draft}` 換成這份素材。兩組另外加入完全相同的指示：

> 請用繁體中文完成任務。回答以 200–300 個中文字為目標，不計標點與空白；這是輸出篇幅的共同要求。不要加上額外的開場白或結語。素材為虛構的示範文本。

兩組各執行兩輪，每次均為獨立請求，沒有先前對話、外部檢索或工具。API 請求的模型名稱為 `gemini-3.5-flash`，服務端實際回傳 `gemini-3.6-flash`；原論文使用的模型則為 GPT-4o。第一輪的 seed 為 20261113，第二輪為 20261114，每輪兩組使用相同的請求設定。

以下收錄四份完整回覆，沒有修改文字或依內容挑選結果，也沒有把建議另行套回原文。這裡只使用一份素材、每組生成兩次，供讀者直接閱讀產出；要估計哪種 prompt 更有效，仍需要更多素材與評估。

### 第一輪

短 prompt 的回覆（242 個中文字）：

> 原文主要問題如下：
> 一、**邏輯與語意模糊**：將「滿意者多為常客」逕自推論為「對新使用者幫助有限」缺乏因果必然性；問卷數據說明混亂，用「兩個問題回答不同」解釋四分之三的滿意度，語意含糊且邏輯斷裂。
> 二、**結構與語氣不佳**：從問卷分析轉折至人力限制與每週開放兩天的決策過於生硬；結尾「弄清楚」過於口語，缺乏公文專業感。
>
> 修改建議：
> 一、**精準呈現統計**：區分「使用頻率」與「滿意度」問題，說明兩者差異，避免數據解讀混淆。
> 二、**重構邏輯順序**：先陳述調查結果，再說明人力困境，最後導出保留每週兩天的折衷方案。
> 三、**修飾專業用語**：將結尾調整為「進一步調查未到館者的潛在需求」，提升行文精準度與流暢度。

論文 prompt 的回覆（199 個中文字）：

> ### Issue 1
> > "因為兩個問題的回答並不一樣"
> >
> > **Issue**: 前文缺乏上下文鋪陳，未能明確說明問卷具體指涉之題目內容與對應關係。
> >
> > **Fix**: "因為使用率與滿意度兩項調查數據係採分開統計"
>
> ### Issue 2
> > "延長的部分會影響原來工作"
> >
> > **Issue**: 文意表達過於含糊，未具體說明延長開放對館員日常既有業務之排擠狀況。
> >
> > **Fix**: "夜間延長開放時間將嚴重排擠館員之日常既有業務"
>
> ### Issue 3
> > "把沒有來的人為何沒來弄清楚"
> >
> > **Issue**: 句式極為口語且用語重複，缺乏正式公文書面報告應有之精確度與專業感。
> >
> > **Fix**: "廣泛調查並深入釐清潛在使用者未曾到館之背後具體原因"

### 第二輪

短 prompt 的回覆（269 個中文字）：

> 原文分析與具體修改建議如下：
>
> **問題診斷**：
> 一、**語意模糊與邏輯斷層**：「兩個問題的回答並不一樣」未具體說明問卷題目與數據連結，致使調查結果與推論產生邏輯斷層；對「新使用者」定義不清，難以對照實際效益。
> 二、**句構冗長與口語化**：後半段句型過長且多以轉折詞連接，缺乏清晰層次；使用如「弄清楚」等口語，降低公務文本的專業度。
>
> **具體修改建議**：
> 一、**補強數據與因果邏輯**：明確列出「晚間使用率」與「滿意度」的交叉統計數據，精確說明何以無法等同於滿意度比例。
> 二、**重組層次與精簡用語**：改採「試辦成效—人力困境—因應方案與後續規劃」三段式架構；並將口語表達改為專業用語（如將「弄清楚未到館原因」改為「深入調查潛在使用者未到館主因」），以提升整體精確度與流暢度。

論文 prompt 的回覆（215 個中文字）：

> ### Issue 1
> > "因為兩個問題的回答並不一樣"
> >
> > **Issue**: 前後數據邏輯交代不清，未具體說明問卷中兩道問題的採計差異。
> >
> > **Fix**: "因為夜間實際到館紀錄與滿意度評價屬於兩項獨立採計的調查題項"
>
> ### Issue 2
> > "延長的部分會影響原來工作"
> >
> > **Issue**: 文意指涉對象極為模糊，未明確指出延長開放對館員日常業務的影響。
> >
> > **Fix**: "延長開放時間將會大幅排擠館員原本必須進行與處理的日常行政業務"
>
> ### Issue 3
> > "把沒有來的人為何沒來弄清楚"
> >
> > **Issue**: 敘述句式過於口語散漫，缺乏正式工作報告應具備的專業性與精準度。
> >
> > **Fix**: "進一步深入調查並釐清潛在使用者未能前來利用圖書館空間資源的具體原因"

## 論文、檔案與執行紀錄

- [論文 PDF](paper.pdf)：本庫保存的 arXiv:2604.11009v2。
- [arXiv 全文與附錄](https://arxiv.org/html/2604.11009v2)：第 3–5 節為方法與結果，第 8 節為限制，附錄 C 為七份 prompt 的來源。
- [示範的完整檔案與執行紀錄](../../examples/clarity/)：包含素材、填好內容的兩種 prompt，以及每次呼叫的請求、回覆和模型資訊。

七份獨立的純文字模板保存在本頁所在資料夾的 `prompts/`。論文與原始 prompt 依 CC BY-NC-SA 4.0 收錄；本頁中文說明與額外示範由本庫整理。作者歸屬與原始檔案雜湊分別記錄於 repository 根目錄的 `ATTRIBUTION.md` 和 `sources.json`。更新日期：2026-11-13。
