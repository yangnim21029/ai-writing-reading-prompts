# 範文與風格模仿

**Can Good Writing Be Generative? Expert-Level AI Writing Emerges through Fine-Tuning on High-Quality Books**

作者：Tuhin Chakrabarty；Paramveer S. Dhillon

機構：密西根大學、石溪大學

arXiv：2601.18353v1 · 首次提交：2026-01-26

[PDF](paper.pdf) · [arXiv](https://arxiv.org/abs/2601.18353) · [HTML 全文](https://arxiv.org/html/2601.18353v1) · [回到總目錄](../../README.md)

## 用途與證據

比較 20 段範文的 in-context prompting 與作家作品微調。只用 prompt 時，一般讀者對部分模型有較高偏好，專家整體仍偏好人類；專家偏好 AI 的主要優勢來自另外微調。

**比較對象：** AI vs. 人類作者；須區分 prompt 與微調

**使用方式：** 本庫提供依方法整理的填空模板，以及 50 位作家的官方 prompt 連結。自備 20 段範文、風格特徵、內容要求和字數。

**研究範圍：** 填空模板是整理者改編，不是作者原始檔；未附原 prompt 的完整文學作品節錄。研究評估短篇風格模仿的品質偏好，沒有直接驗證更好懂或更忠於原意。

[結果定位](https://arxiv.org/html/2601.18353v1#A1.SS2)

## Prompts

英文原文檔可直接開啟。從論文 HTML 擷取的模板僅整理排版；改編模板另有標記。

| 檔案 | 類型 | 來源 |
|---|---|---|
| [style-imitation.adapted.en.txt](prompts/style-imitation.adapted.en.txt) | 整理者改編 | [原始位置](https://arxiv.org/html/2601.18353v1#S3.SS1.SSS3) |

[50 位作家的完整官方 Prompt 目錄](upstream-prompts.md)

## 來源與授權

論文 PDF：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，保留原始檔案。原始 prompt 與資料依各來源授權；詳細歸屬見 [ATTRIBUTION](../../ATTRIBUTION.md)。

整理日期：2026-11-13。
