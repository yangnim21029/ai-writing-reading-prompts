# Incentives Shape How Humans Co-Create with Generative AI

Nathanael Jo、Manish Raghavan<br>
麻省理工學院<br>
首次提交：2026-04-04 · 收錄版本：arXiv:2604.03529v2

[論文 PDF](paper.pdf) · [HTML 全文](https://arxiv.org/html/2604.03529v2) · [公開資料集](https://huggingface.co/datasets/nathanaeljo/ai-cocreation-incentives) · [回到目錄](../../README.md)

## 獎勵條件與人機協作

研究以兩項實驗觀察，原創性與技術品質的獎勵如何改變人機協作及作品間的差異。Study 1 招募 200 位參與者撰寫 250–350 個英文字的短故事；Study 2 招募 400 位參與者撰寫 100–125 個英文字的商品簡介。兩項實驗都交叉操弄是否可以使用 AI，以及獎勵原創性或技術品質。[任務與分組](https://arxiv.org/html/2604.03529v2#S3)

參與者自行決定如何向 AI 提問和修改文字，因此公開資料保存了實際發生的多輪提示，而非所有人共同使用的一份寫作模板。這些紀錄可用於分析起草、請求修改與採納建議等協作行為；每則提示的效果並未被獨立測試。

作者另以語言模型評估作品的技術品質。短故事評分著重組織與文字表現，商品簡介評分則關注資訊是否充分正確，以及表達是否清楚。評分指示明確排除對原創性或個人喜好的評價，藉此將技術品質與作品差異分開考察。

品質分析中，AI 協助的作品分數較高；作者同時觀察到作品同質化，以及原創性獎勵在部分條件下增加作品差異的效果。論文 §7.2 將技術品質結果明確列為描述性分析，因為品質本身也受到獎勵操弄影響。[品質分析與條件比較](https://arxiv.org/html/2604.03529v2#S7.SS2)

## 使用者提示紀錄

以下 CSV 保留資料集原始檔案。Study 1 有 100 筆 AI 組參與者紀錄，Study 2 有 200 筆；實驗中的無 AI 組不會產生這類提示紀錄。每一列是一位參與者，`participant_id` 是上游使用的代號，`ai_requests` 保存該參與者的多輪提示清單。

| 任務 | 完整資料 | 閱讀用摘錄 |
|---|---|---|
| 短故事 | [Study 1 提示紀錄 CSV](prompts/study1-user-prompts.csv) | [前五筆非空參與者紀錄](prompts/study1-examples.md) |
| 商品簡介 | [Study 2 提示紀錄 CSV](prompts/study2-user-prompts.csv) | [前五筆非空參與者紀錄](prompts/study2-examples.md) |

摘錄依資料檔順序選取，保留各輪文字，未依作品成績挑選。完整 CSV 沿用上游的清單表示格式，若用程式分析，需先解析 `ai_requests` 欄位，再區分參與者與對話輪次。

## 品質評分 Prompts

兩份 system prompts 擷取自附錄 B.2，用來評分已完成的作品。它們指定評分規準、各分數的描述與輸出方式；適用任務分別是研究中的短故事與商品簡介。

| 評分任務 | Prompt | 原文位置 |
|---|---|---|
| 短故事技術品質 | [Study 1 評分 Prompt](prompts/study1-quality-judge.en.txt) | [附錄 B.2，Study 1](https://arxiv.org/html/2604.03529v2#A2.SS2.SSSx1) |
| 商品簡介資訊與表達品質 | [Study 2 評分 Prompt](prompts/study2-quality-judge.en.txt) | [附錄 B.2，Study 2](https://arxiv.org/html/2604.03529v2#A2.SS2.SSSx2) |

若改用商品簡介評分 prompt，需先替換其中研究指定產品的資訊，否則模型會依原實驗的產品規格評分。更換任務或評分規準後，也應重新檢查評分與人工判斷的一致性。

論文、公開資料集與擷取的評分 prompts 採 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。CSV 固定於資料集版本 `475a751e12ca548f51ad631673e1845330ad3c53`；逐檔來源見 [sources.json](../../sources.json)，作者歸屬見 [ATTRIBUTION](../../ATTRIBUTION.md)。整理日期：2026-11-13。
