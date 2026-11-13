# 詩歌細讀：用文本證據解釋用字、視角與形式

這篇研究觀察讀者接觸 AI 解讀後，如何辨認詩中的文本特徵、提出詮釋並寫出說明。研究公開的任務指示要求分析三類例子：特殊用字、詩人的聲音或視角，以及形式或風格。每個例子都要引用文本，再解釋它在詩中的作用。

論文為 *What Does AI Do for Cultural Interpretation? A Randomized Experiment on Close Reading Poems with Exposure to AI Interpretation*，作者是 Jiayin Zhi、Hoyt Long、Richard Jean So 與 Mina Lee，分別來自芝加哥大學與杜克大學。首次提交於 2026 年 3 月 6 日，本頁依據 arXiv:2603.06855v1。

## 研究測量的是讀者接觸 AI 解讀後的表現

研究採隨機實驗，最終納入 400 位參與者。每位參與者閱讀三首詩，並被分配至無 AI 解讀、閱讀一份 AI 解讀，或閱讀三份 AI 解讀的條件，隨後完成文本分析與閱讀體驗問卷。

單份解讀由 GPT-4o 依與參與者相同的任務指示產生。多份解讀的條件另要求模型提出三種不同分析，指出不同特徵並說明其效果。研究人員先以評分規準檢查 AI 解讀，再把材料放進實驗介面。參與者閱讀的是預先準備的內容。

兩位受訓評分者評閱參與者的回答。文本特徵辨認以 0 或 1 分表示錯誤或正確；詮釋品質評估說明的深度與洞見，寫作品質評估清晰度與連貫性，兩者皆採 1–5 分量尺。研究先將每首詩的三項任務分數按評估面向取平均，再進行分析。

原文第 4.1.1 節報告以下相對於無 AI 組的分數差異：

| 評估面向 | 閱讀一份 AI 解讀 | 閱讀三份 AI 解讀 |
|---|---:|---:|
| 文本特徵辨認（0–1） | +0.048，p = .042 | +0.051，p = .020 |
| 詮釋品質（1–5） | +0.865，p < .001 | +0.593，p < .001 |
| 寫作品質（1–5） | +1.035，p < .001 | +0.784，p < .001 |

表中每格都是與無 AI 組的比較，不能由這張表直接判定單份解讀與三份解讀之間的差異是否顯著。分數反映參與者閱讀 AI 材料後的分析表現，也不能換算成 AI 單獨作答勝過人類的比例。評分方法與 AI 材料的準備程序分別見第 3.2.1 節與第 3.1.5 節。

## 細讀 prompt 的完整原文與用法

這份文字取自研究介面 `pageInfo.ts` 的 `page5_1.left_top_instruction`，移除 HTML 標籤後保留原始措辭。論文第 3.1.5 節說明，生成單份 AI 解讀時採用與參與者相同的任務指示，因此本庫收錄這份文字作為該條件的任務來源。

它要求每個分析例子分成兩部分：先用一句話辨認並界定文本特徵，附短引文或具體位置；再用兩到三句話說明該特徵為何突出、詩人可能為何採用它，以及預期對讀者產生什麼效果。

| 分析對象 | 要找的文本例子 |
|---|---|
| 用字或片語 | 顯著、刻意或不尋常的語言使用 |
| 聲音或視角 | 呈現詩人立場、自我表現或觀看方式的詩句 |
| 形式與風格 | 重複、節奏、押韻、聲音、視覺排列等特徵 |

```text
[Question] Next we ask: What message or meaning is this poem trying to communicate to you, the reader? How does the poem use its language to accomplish this task? Here, we want you to identify three kinds of examples to answer this question.

First example: identify a specific word or phrase that stands out as distinctive in the poem or which is being used in an intentional or irregular way.

Second example: identify a specific line or phrase that gives you insight into the poet's voice or perspective , revealing something about him or herself.

Third example: Considering a specific phrase or the poem as a whole, identify an element of poetic style that stands out to you and that plays an important role in communicating the poem’s message or meaning. Common examples of style include: repetition, rhythm, rhyme, the use of sounds, and the visual structure or arrangement of the poem, etc.

Once you have identified your three examples, please then do the following in Your Answer :

1. In each left textbox, write one sentence for each example in which you clearly identify and define the textual feature, using short quotes or references to specific sentences/passages from the poem to help us locate it.

2. Next, in each right textbox, write 2-3 sentences that explain why that textual feature stands out in the poem, why you think this poet chose it, and what is its intended effect on the reader.
```

原文的左右文字框對應研究介面的兩欄作答區。改用於聊天介面時，需把詩文一起提供，並另行說明以一般文字列出這兩部分。下方示範保留原始任務指示，在兩組共用指示中處理文字框的呈現。本庫收錄範圍限於這份任務文字，未重建原研究的三份解讀生成與審核流程。

## 論文 prompt 與一般短 prompt 的實際解讀

這組示範讓兩種 prompt 分析同一首中文詩。素材與模型回覆由本庫另行準備，沒有使用原研究的詩作、預先審核的解讀或真人參與者。

素材由本庫撰寫，共 235 個中文字，不計標點與空白。

```text
末班車開走以後
母親仍把門口的燈留著
她說不是等誰
只是巷子太暗

我在電話這頭答應
下次回去會早一點
窗外另一座城市的車聲
把那個下次推得更遠

她問我有沒有吃飯
我說吃了
桌上那碗還沒拆封的麵
慢慢失去熱氣

通話結束前
她又說燈泡最近不太亮
我想起小時候走過巷口
總能先看見那一小塊黃
再看見她站在門裡
手上拿著忘了收起的雨傘

現在我把手機翻過來
房間忽然安靜得像一條巷子
我沒有訂票
也沒有把燈關掉
只是把那碗麵放進鍋裡
等水重新沸騰

樓下有人拖著行李經過
輪子一格一格碰著路面
我聽到聲音漸漸走遠
才發現自己一直站在門邊
```

短 prompt 由 Gemini 在未接觸論文模板的另一個請求中產生，要求寫出日常可用的指令，最多 35 個英文單字。實際使用的指令如下，後面接上同一份素材。

```text
Examine the provided poem by analyzing its central themes, imagery, figurative language, and structural choices, explaining how these literary devices contribute to its overall meaning and emotional impact.
```

論文條件使用上方完整英文任務指示，後面附上同一首詩。原研究使用 GPT-4o；本次示範的模型依下方執行紀錄標示。

兩組共用的指示如下：

> 請用繁體中文完成任務。回答以 200–300 個中文字為目標，不計標點與空白；這是輸出篇幅的共同要求。不要加上額外的開場白或結語。素材為虛構的示範文本。 若任務提到左右文字框，請依序以一般文字呈現對應內容。

兩組各執行兩輪，每次均為獨立請求，沒有先前對話、外部檢索或工具。執行日期為 2026 年 11 月 13 日。API 請求的模型名稱為 `gemini-3.5-flash`，服務端實際回傳 `gemini-3.6-flash`。第一輪的 seed 為 20261113，第二輪為 20261114，每輪兩組使用相同的請求設定。

以下保留四份成功回覆，沒有事後改寫或依內容挑選。這裡只有一份素材、每組兩次生成，供讀者直接閱讀產出；它們不提供普遍勝率的估計。

### 第一輪

短 prompt 的回覆（249 個中文字）：

> 本詩以空間距離與情感疏離為核心主題，藉由細膩的意象與修辭描繪出異鄉子女對母愛的愧疚與思念。
>
> 詩中「門口的燈」與「那一小塊黃」象徵母親無聲的守候與溫暖，與主角異地房間的冷清形成強烈對比。「未拆封的麵慢慢失去熱氣」將生活疲累與孤獨具象化；「房間安靜得像一條巷子」則運用明喻，將現實空間與記憶中的家巷重疊，延伸孤寂感。
>
> 結構上採時空交錯，從電話對白推移至童年回憶，最後落腳於掛斷電話後的微小動作。結尾「把麵放進鍋裡等水重新沸騰」與「一直站在門邊」，將原本被動的疏離轉化為對溫暖的渴望與同理。行李聲的漸遠，深刻反襯出主角內心停滯且沉重的思鄉情緒，增添無盡的情感餘韻。

論文 prompt 的回覆（270 個中文字）：

> 【左側文字框一】
> 詩中「把那個下次推得更遠」將抽象承諾轉化為被距離推開的實體物。
>
> 【右側文字框一】
> 此擬人寫法凸顯主角身處異鄉的愧疚。作者藉此展現都市喧囂對親情陪伴的吞噬，讓讀者感受無法陪伴父母的焦慮。
>
> 【左側文字框二】
> 「才發現自己一直站在門邊」揭示了主角對母親的依戀與潛意識模仿。
>
> 【右側文字框二】
> 這展現作者自省且壓抑的視角，反映他雖未明言，行動上已與母親遙相呼應。這能引發讀者對血緣羈絆的共鳴，體會無聲的關愛。
>
> 【左側文字框三】
> 全詩重複運用「巷子」與「燈」的意象對比，建立孤獨與溫暖並存的風格。
>
> 【右側文字框三】
> 這種對比加強了詩歌的視覺感，映照出母子兩地相隔卻心意相通。作者藉微光再現，傳達母愛終能照亮內心陰暗角落的主旨。

### 第二輪

短 prompt 的回覆（216 個中文字）：

> 本詩以「黃光」與「距離」為核心意象，深刻剖析離鄉子女的愧疚與孤寂。詩中母親留著的燈光，象徵無聲卻恆常的母愛；而主角眼前「冷掉的麵」與「漸遠的車聲」，則與這份溫暖形成強烈對比，具象化了都市生活中的疏離與壓抑。
>
> 詩人巧用擬人與比喻修辭，將都市「車聲」賦予「推遠歸期」的動作，並將「寂靜房間」化為「暗巷」，使現實困境與記憶場景重疊。結構上採用空間與時間的雙線對照，從電話寒暄轉入童年回憶，最後落腳於主角「加熱麵條」與「站在門邊」的動作。此結尾不僅遙相呼應母親的等待，更在克制的敘事中爆發出濃烈而沉重的鄉愁與遺憾。

論文 prompt 的回覆（271 個中文字）：

> 左框一：詩人使用「一小塊黃」這一獨特的視覺名詞，指稱童年巷口那盞溫暖的門燈。
> 右框一：此詞將抽象記憶具象為微小符號，突顯母親守候的溫柔。詩人藉此勾勒游子對家鄉光亮的依戀，引發讀者對親情溫度的共鳴。
>
> 左框二：詩末「才發現自己一直站在門邊」這句話，揭示了詩人在通話後無意識模仿母親佇立門口的姿態。
> 右框二：這展現出詩人內心的愧疚與思念，揭露他雖身在異鄉，情感卻與母親同步。此描繪讓讀者體會異鄉人無法即刻返家的無奈與愛意。
>
> 左框三：本詩運用「燈光」與「空間」的重複對比手法，將異鄉房間與故鄉巷子進行平行疊合。
> 右框三：詩人藉由意象重疊模糊了兩地距離，強化牽掛的主題。這種風格使讀者在平實敘述中感受到深沉的孤獨與情感張力。

## 論文、原始任務與執行紀錄

- [論文 PDF](paper.pdf)：本庫保存的 arXiv:2603.06855v1。
- [arXiv 全文與附錄](https://arxiv.org/html/2603.06855v1)：第 3 節交代實驗與評分，第 4 節報告結果。
- [研究介面的原始程式](https://github.com/xxxxbrandieeee/close-reading-interface/blob/main/close-reading/src/pageInfo.ts)：任務指示的來源。
- [示範的完整檔案與執行紀錄](../../examples/close-reading/)：包含詩文、兩種 prompt、每次請求與完整回覆。

論文採 CC BY 4.0。任務指示沿用研究介面的 MIT 授權，Copyright (c) 2026 jiayin-3zh-research，授權全文保存在 `prompts/LICENSE-MIT.txt`。純文字任務檔為 `prompts/close-reading-task.en.txt`；作者歸屬與來源記錄於 repository 根目錄的 `ATTRIBUTION.md` 和 `sources.json`。更新日期：2026-11-13。
