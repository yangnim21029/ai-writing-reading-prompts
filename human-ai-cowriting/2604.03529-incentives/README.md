# 人機共寫與多輪修改

**Incentives Shape How Humans Co-Create with Generative AI**

作者：Nathanael Jo；Manish Raghavan

機構：麻省理工學院

arXiv：2604.03529v2 · 首次提交：2026-04-04

[PDF](paper.pdf) · [arXiv](https://arxiv.org/abs/2604.03529) · [HTML 全文](https://arxiv.org/html/2604.03529v2) · [回到總目錄](../../README.md)

## 用途與證據

短故事和商品簡介實驗公開參與者的實際提示紀錄。作者描述 AI 協助的技術品質較高，同時觀察到作品同質化；沒有單一標準寫作 prompt。

**比較對象：** 人類＋AI vs. 無 AI；另比較獎勵條件

**使用方式：** 從兩份使用者 prompt CSV 看真實的提問與修改方式。另有兩份英文評分 system prompt，可用於參考品質評估。

**研究範圍：** 技術品質增益屬描述性分析。評分 prompt 用來評估作品，並不是產生較好作品的寫作指令；個別使用者提示也沒有獨立成效驗證。

[結果定位](https://arxiv.org/html/2604.03529v2#S7.SS2)

## Prompts

英文原文檔可直接開啟。從論文 HTML 擷取的模板僅整理排版；改編模板另有標記。

| 檔案 | 類型 | 來源 |
|---|---|---|
| [study1-quality-judge.en.txt](prompts/study1-quality-judge.en.txt) | 原始評分模板 | [原始位置](https://arxiv.org/html/2604.03529v2#A2.SS2.SSSx1) |
| [study1-user-prompts.csv](prompts/study1-user-prompts.csv) | 原始使用者紀錄 | [原始位置](https://huggingface.co/datasets/nathanaeljo/ai-cocreation-incentives/blob/475a751e12ca548f51ad631673e1845330ad3c53/study1/processed/ai_requests.csv) |
| [study2-quality-judge.en.txt](prompts/study2-quality-judge.en.txt) | 原始評分模板 | [原始位置](https://arxiv.org/html/2604.03529v2#A2.SS2.SSSx2) |
| [study2-user-prompts.csv](prompts/study2-user-prompts.csv) | 原始使用者紀錄 | [原始位置](https://huggingface.co/datasets/nathanaeljo/ai-cocreation-incentives/blob/475a751e12ca548f51ad631673e1845330ad3c53/study2/processed/ai_requests.csv) |

瀏覽範例：[短故事](prompts/study1-examples.md) · [商品簡介](prompts/study2-examples.md)。CSV 的 ai_requests 欄每格包含一位參與者的多輪提示清單；保留上游原始格式。

## 來源與授權

論文 PDF：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，保留原始檔案。原始 prompt 與資料依各來源授權；詳細歸屬見 [ATTRIBUTION](../../ATTRIBUTION.md)。

整理日期：2026-11-13。
