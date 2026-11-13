# AI Writing and Reading Prompts

收錄 2026 年五篇寫作與閱讀研究，以及作者公開的實驗 prompts。研究主題涵蓋寫作階段、文學風格模仿、角色建構、詩歌細讀與人機協作。每篇資料夾保存論文 PDF，並說明 prompt 如何用於實驗、成效由誰評估，以及哪些條件需要一併重現。

本目錄以可查核的研究方法為選錄依據。各篇的比較對象不同：有些比較人機協作與獨立寫作，有些比較兩套 AI 生成流程，也有研究直接比較 AI 與人類作者。以下保留這些差異，供閱讀論文與改用 prompt 時參考。

## 實際產出對照

以同一份 200–300 字中文素材，將論文 prompt 與 AI 另外生成的短 prompt 各跑兩次，共保存 12 份完整回覆。每頁並排展示完整產出，附上兩邊的 prompt 與執行紀錄，供讀者自行比較。

| 任務 | 素材字數 | 對照內容 |
|---|---:|---|
| [清晰度修訂](examples/clarity/) | 232 | 短 prompt 與附錄 C.3.2，各兩輪產出 |
| [角色敘事](examples/narrative/) | 225 | 短 prompt 與附錄 A.5，各兩輪產出 |
| [詩歌細讀](examples/close-reading/) | 235 | 短 prompt 與研究任務指示，各兩輪產出 |

[查看素材、完整產出與執行紀錄](examples/)；實際回傳模型為 Gemini 3.6 Flash。這些是本庫的實作示範，與下方原論文的實驗結果分開呈現。

## 文獻目錄

| 研究主題 | 論文與方法說明 | 公開的 Prompt 資料 |
|---|---|---|
| 寫作階段與心理所有權 | [From Planning to Revision](writing-revision/2604.11009-planning-to-revision/) | 論點發想、大綱、起草、校對、清晰度與論證修訂 |
| 文學風格模仿 | [Can Good Writing Be Generative?](style-imitation/2601.18353-good-writing/) | 50 位作家的原始 prompt 連結；依研究方法整理的填空模板 |
| 角色建構與敘事生成 | [Narrative Keyframing](story-generation/2608.10337-narrative-keyframing/) | 角色特質、第一人稱視角、文本證據與第三人稱敘事 |
| AI 解讀與詩歌細讀 | [What Does AI Do for Cultural Interpretation?](close-reading/2603.06855-poem-interpretation/) | 辨認文本特徵、引用詩句與解釋閱讀效果的任務指示 |
| 協作寫作與獎勵制度 | [Incentives Shape How Humans Co-Create](human-ai-cowriting/2604.03529-incentives/) | 參與者的多輪提示紀錄，以及短故事與商品簡介的評分 prompts |

## Prompt 比較的證據

這五篇原論文的實驗中，尚未找到「論文公開的 prompt」與「由另一個 AI 生成的短 prompt」的直接對照。本庫另以三種任務製作了上方的產出示範；下表則整理原論文實際使用的比較條件。

| 論文 | 實際比較條件 | 能回答的問題 |
|---|---|---|
| Narrative Keyframing | 同一個 GPT-4.1、相同故事大綱；多步驟生成流程 vs. 一般大綱擴寫 | 這套流程是否優於該大綱擴寫基準 |
| From Planning to Revision | 不同寫作階段的 AI 支援 vs. 無 AI | AI 在哪個寫作階段介入，如何影響品質與心理所有權 |
| Can Good Writing Be Generative? | 提供範文的模型、微調模型與人類作者 | 不同模型條件與人類作品的評審偏好如何不同 |
| What Does AI Do for Cultural Interpretation? | 閱讀單份或多份 AI 解讀 vs. 未接觸 AI 解讀 | 接觸 AI 解讀是否影響讀者之後的文本分析 |
| Incentives Shape How Humans Co-Create | 有無 AI 與不同獎勵條件 | AI 使用與獎勵制度如何影響作品及協作過程 |

最接近一般 prompt 對照的是 [Narrative Keyframing 的技術評估](https://arxiv.org/html/2608.10337v1#S6.SS1.SSS1)。作者將對照稱為 vanilla prompt-based LLM baseline，但未將其描述為「另一個 AI 生成的短 prompt」。實驗條件同時加入角色設定、第一人稱敘述及證據整合等步驟，因此結果支持的是整套方法相對於該基準的效果，不能單獨歸因於提示詞長度或措辭。

## 寫作階段與心理所有權

### From Planning to Revision: How AI Writing Support at Different Stages Alters Ownership

Katy Ilonka Gero、Tao Long、Carly Schnitzler、Paramveer S. Dhillon<br>
雪梨大學、哥倫比亞大學、約翰霍普金斯大學、密西根大學 · 2026-04-13 · arXiv:2604.11009v2

這項實驗將 253 位參與者分為四組，分別在規劃、起草、修訂階段使用 AI，或全程獨立完成議論文。研究同時評估文章品質與心理所有權，也就是作者是否認為文章真正屬於自己。經控制題目、字數與作答時間後，起草組的品質分數為 7.27，無 AI 組為 5.69，量尺為 0–9 分；品質由經人工評分樣本校準的語言模型評估。起草組也出現最大的心理所有權下降。[研究結果](https://arxiv.org/html/2604.11009v2#S5.SS4)

附錄 C 公開各階段的七份 prompts。清晰度與校對模板要求模型引用原文片段，再提出可直接替換的修改文字；起草模板則依使用者的大綱生成全文。實驗中最明顯的品質增益來自起草條件，單獨使用清晰度或校對模板的效果需另行評估。

[PDF](writing-revision/2604.11009-planning-to-revision/paper.pdf) · [實驗與 Prompt 說明](writing-revision/2604.11009-planning-to-revision/) · [清晰度修改原始 Prompt](writing-revision/2604.11009-planning-to-revision/prompts/06-writing-clarity.en.txt)

## 文學風格模仿

### Can Good Writing Be Generative? Expert-Level AI Writing Emerges through Fine-Tuning on High-Quality Books

Tuhin Chakrabarty、Paramveer S. Dhillon<br>
石溪大學、密西根大學 · 2026-01-26 · arXiv:2601.18353v1

研究請人類作者與語言模型依同一份內容要求，模仿指定作家的風格。In-context prompting 條件提供 20 段範文、風格描述及待寫內容；另一條件則以作家的完整作品微調 GPT-4o。評審分為具寫作背景的專家與一般讀者，分別判斷寫作品質和風格相似度。

只使用 prompt 時，GPT-4o 在一般讀者評審中的寫作品質勝率為 66%，在專家評審中為 12%；Claude 3.5 Sonnet 分別為 56% 與 30%。另行微調 GPT-4o 後，專家評審的勝率才提高至 62.2%。這些數字是指定寫作任務下的人類偏好，不能直接解讀為閱讀理解或原意保留的改善。[評審與模型的分項結果](https://arxiv.org/html/2601.18353v1#A1.SS2)

[PDF](style-imitation/2601.18353-good-writing/paper.pdf) · [實驗與 Prompt 說明](style-imitation/2601.18353-good-writing/) · [50 位作家的原始 Prompt 目錄](style-imitation/2601.18353-good-writing/upstream-prompts.md)

## 角色建構與敘事生成

### Narrative Keyframing for Generative Creative Writing

Chao Zhang、Abe Davis<br>
康乃爾大學 · 2026-08-11 · arXiv:2608.10337v1

作者把故事生成拆成角色特質設定、第一人稱敘述、文本證據擷取與第三人稱敘事等步驟，讓角色在不同劇情段落中的變化能被明確指定。實驗以相同的 GPT-4.1 與故事大綱，比較這套流程和一般的大綱擴寫方法。

在隨機抽取的 30 組故事中，三位具專業寫作經驗的評審以多數決判定：25 組較偏好此方法的整體品質，29 組認為其角色刻畫較豐富。這項結果支持特定生成流程的優勢。部分評審也指出，增加角色細節有時會使文字過度鋪陳，因此角色刻畫與閱讀流暢度仍須分別考察。[評估方法與結果](https://arxiv.org/html/2608.10337v1#S6.SS1)

[PDF](story-generation/2608.10337-narrative-keyframing/paper.pdf) · [生成流程與八份 Prompt](story-generation/2608.10337-narrative-keyframing/)

## AI 解讀與詩歌細讀

### What Does AI Do for Cultural Interpretation? A Randomized Experiment on Close Reading Poems with Exposure to AI Interpretation

Jiayin Zhi、Hoyt Long、Richard Jean So、Mina Lee<br>
芝加哥大學、杜克大學 · 2026-03-06 · arXiv:2603.06855v1

400 位參與者被隨機分配至三種條件：閱讀一份 AI 解讀、閱讀三份不同的 AI 解讀，或不接觸 AI 解讀，隨後完成三首詩的文本分析。GPT-4o 依與參與者相同的任務指示生成單份解讀，內容經研究人員評分檢查後才用於實驗。

相較於無 AI 組，閱讀單份 AI 解讀的參與者在詮釋品質上平均增加 0.865 分，寫作品質增加 1.035 分；兩項皆採 1–5 分量尺，且 p < .001。這裡測量的是讀者接觸 AI 解讀之後的分析表現。公開的 prompt 要求辨認特殊用字、詩人的聲音或視角、詩歌形式，並以引文解釋其效果。[研究結果](https://arxiv.org/html/2603.06855v1#S4.SS1.SSS1)

[PDF](close-reading/2603.06855-poem-interpretation/paper.pdf) · [實驗與 Prompt 說明](close-reading/2603.06855-poem-interpretation/) · [原始細讀任務指示](close-reading/2603.06855-poem-interpretation/prompts/close-reading-task.en.txt)

## 協作寫作與獎勵制度

### Incentives Shape How Humans Co-Create with Generative AI

Nathanael Jo、Manish Raghavan<br>
麻省理工學院 · 2026-04-04 · arXiv:2604.03529v2

兩項實驗分別招募 200 人撰寫短故事、400 人撰寫商品簡介，交叉比較是否使用 AI，以及獎勵原創性或技術品質的條件。研究關注獎勵制度如何影響人機協作過程與作品間的差異。技術品質在這裡指文章組織、語言表達或資訊傳達等可依評分規準判斷的面向。

作者的描述性分析顯示，AI 協助的作品技術品質較高，同時存在作品同質化的現象。這篇公開了 AI 組參與者實際輸入的多輪 prompts，適合觀察提問與修改過程；另公開兩份用於品質評估的 system prompts。使用者紀錄中的每則提示並未個別接受成效檢驗。[品質分析](https://arxiv.org/html/2604.03529v2#S7.SS2)

[PDF](human-ai-cowriting/2604.03529-incentives/paper.pdf) · [實驗與資料說明](human-ai-cowriting/2604.03529-incentives/) · [短故事提示範例](human-ai-cowriting/2604.03529-incentives/prompts/study1-examples.md) · [商品簡介提示範例](human-ai-cowriting/2604.03529-incentives/prompts/study2-examples.md)

## 檔案與來源

每篇論文的資料夾包含 `paper.pdf`、`prompts/` 與研究說明。從附錄或程式擷取的英文 prompts 保留原文，只移除網頁排版；作家風格的填空模板標記為 `adapted`，完整原始 prompts 另列上游連結。額外撰寫的[中文局部修改模板](templates/)獨立存放，未經上述研究驗證。

[CSV 文獻清單](catalog.csv) · [JSON 文獻清單](catalog.json) · [逐檔來源與檔案雜湊](sources.json) · [作者歸屬與授權](ATTRIBUTION.md)

本目錄採用所列 arXiv 版本，收錄範圍限於這五篇研究。論文、prompts 與資料沿用各自授權；其中 From Planning to Revision 為 CC BY-NC-SA 4.0。中文說明以 AI 輔助整理並對照來源，英文原始 prompts 與另行改編的模板分開標示。

整理日期：2026-11-13。
