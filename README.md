# AI 算法工程师 16 周学习计划

这是一个面向 **LLM/NLP 算法工程师求职** 的 16 周学习执行仓库。

它来自本地 PDF《2025年深度学习快速入门到进阶的学习路线》里的绿色路线，但做了求职向修正：不仅学 Python、数学、机器学习、深度学习和论文复现，也补上 Git、实验记录、项目交付、RAG、LoRA、LLM 评测和面试准备。

## 我的目标

- 学习周期：16 周
- 每周投入：25 小时以上
- 当前基础：Python 会一点
- 求职方向：LLM/NLP 算法工程师
- 最终产出：2 个可写进简历的项目 + 1 个论文/开源项目复现 + 1 版可投递简历

## 为什么不完全照 PDF 绿色路线走

PDF 的绿色路线适合建立“深度学习 + 论文复现”的主线，但如果目标是找 AI 算法工程师工作，还需要补足这些内容：

- 机器学习阶段不能只看懂，要能用 `sklearn` 完整跑训练、验证、调参和评估。
- 深度学习阶段不能只听课，要能写 PyTorch 训练循环并分析训练失败原因。
- LLM/NLP 岗位需要掌握 Transformer、Hugging Face、RAG、LoRA/QLoRA、模型评测。
- 求职项目必须有 README、运行命令、实验表格、错误分析和可讲清楚的技术取舍。
- 16 周内不把“发高区论文”作为主要目标，更现实的是做出能证明能力的项目。

## 文件说明

- [16-week-checklist.md](./16-week-checklist.md)：16 周逐周、逐日任务清单
- [dated-calendar-2026.md](./dated-calendar-2026.md)：按日期排好的日历版，默认从 2026-05-04 开始
- [daily-template.md](./daily-template.md)：每日学习模板
- [PROGRESS.md](./PROGRESS.md)：每周进度同步记录
- [progress-tracker.csv](./progress-tracker.csv)：表格版进度追踪
- [project-portfolio.md](./project-portfolio.md)：项目作品集验收标准
- [interview-checklist.md](./interview-checklist.md)：面试准备清单
- [study-workspace](./study-workspace)：实际学习代码、笔记、实验和项目目录

当前学习进度以 [PROGRESS.md](./PROGRESS.md) 为准。

## 每周固定节奏

- 周一到周五：每天 3 小时
  - 1 小时理论
  - 1.5 小时代码
  - 0.5 小时笔记/复盘
- 周六：6-8 小时，集中做项目、复现实验、整理 GitHub
- 周日：4-5 小时，复盘本周、补缺口、准备下周

## GitHub 进度同步方式

推荐每周至少同步 2 次：

1. 平时用 commit 同步代码、笔记和实验表格。
2. 周日更新 [PROGRESS.md](./PROGRESS.md)。
3. 如果想公开监督自己，可以每周开一个 GitHub Issue，使用仓库里的“周复盘”模板。

建议 commit 格式：

```text
week-01: finish python exercises
week-02: add text dataset eda
week-10: implement rag retrieval baseline
week-14: add paper reproduction ablation
```

## 阶段验收

- 第 4 周：能独立解释并跑通一个传统机器学习项目。
- 第 8 周：能讲清楚反向传播、attention、Transformer 基本结构。
- 第 12 周：有一个可运行的 RAG 或 LLM 微调项目。
- 第 15 周：至少 2 个可写进简历的项目，其中 1 个必须有实验对比。
- 第 16 周：能用 5 分钟讲清楚项目背景、方法、指标、失败案例和改进方向。

## 我的原则

- 不只收藏资料，要产出代码、笔记、实验和项目。
- 不追求一开始就看最难论文，先建立可解释、可复现、可面试的能力。
- 不把项目包装过度，简历里的每一句都要能被追问。
