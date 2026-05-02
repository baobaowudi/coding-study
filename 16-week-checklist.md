# 16 周任务清单：LLM/NLP 算法工程师

只有留下了明确产出，才勾选任务。产出可以是代码、笔记、notebook、实验结果、README、demo 或模拟面试记录。

## 第 1 周：AI 认知、Python 复盘、开发环境

目标：搭好工作环境，恢复 Python 编码手感。

当前实际进度备注：

- PDF 路线中的“人工智能认知建立”已完成。
- PDF 路线中的“Python 基础知识”已完成。
- 本清单中的开发环境已经完成；30 道 Python 练习已经准备题目和 starter 文件，但练习本身仍需自己完成。

必交付：

- [x] Python、Git、VS Code/PyCharm、Jupyter 安装并测试通过
- [x] 初始化一个学习仓库
- [ ] 完成 30 道 Python 练习
- [ ] 写一篇笔记：《AI 算法工程师到底做什么》

每日任务：

- [ ] 周一：重读 PDF 路线，写下目标岗位、每周可投入时间、为什么选 LLM/NLP。
- [ ] 周二：复盘 Python 基础：变量、函数、类、列表/字典推导式。
- [ ] 周三：完成 10 道 Python 练习：字符串、列表、字典、文件读写。
- [ ] 周四：完成 10 道 Python 练习：函数、类、异常、模块。
- [ ] 周五：完成 10 道 Python 练习：简单算法和数据处理。
- [x] 周六：配置 Git 仓库、notebook 环境和目录结构。
- [ ] 周日：写周复盘和下周风险清单。

验收标准：

- [ ] 能创建虚拟环境、安装包、打开 notebook、提交代码。
- [ ] 能不频繁搜索基础语法，独立写一个 Python 脚本。

## 第 2 周：NumPy、Pandas、文本数据 EDA

目标：掌握机器学习和 LLM 数据处理需要的基本能力。

当前实际进度备注：

- NumPy/Pandas 推荐视频已完成。
- 当前下一步是阅读《利用Python进行数据分析》，并把书籍内容转化为 EDA notebook、数据清洗脚本和数据质量报告。

必交付：

- [ ] 阅读《利用Python进行数据分析》中 NumPy、Pandas、数据清洗、数据整理、分组聚合相关章节
- [ ] 文本数据 EDA notebook
- [ ] 数据清洗脚本
- [ ] 一份报告：缺失值、标签分布、文本长度分布、典型样例

每日任务：

- [ ] 周一：学习 NumPy array、shape、broadcasting、索引、矩阵运算。
- [ ] 周二：完成 8 个 NumPy 练习，包括归一化和向量化操作。
- [ ] 周三：学习 Pandas Series/DataFrame、过滤、groupby、merge、apply。
- [ ] 周四：加载一个公开文本数据集或 CSV，检查字段、标签、重复、缺失。
- [ ] 周五：画文本长度分布和标签分布。
- [ ] 周六：完成 `eda.ipynb` 和 `clean_data.py`。
- [ ] 周日：写 EDA 报告，说明哪些数据质量问题会影响模型。

验收标准：

- [ ] 能解释数据质量为什么会影响模型效果。
- [ ] 能用 NumPy/Pandas 做基础数据处理，而不是只复制代码。

## 第 3 周：数学核心：线代、概率、微积分

目标：理解优化和神经网络背后的基本数学。

必交付：

- [ ] NumPy 实现线性回归
- [ ] NumPy 实现梯度下降
- [ ] NumPy 实现 softmax 和交叉熵
- [ ] 一篇数学笔记：公式 + 代码链接

每日任务：

- [ ] 周一：复习向量、矩阵、点积、矩阵乘法、范数。
- [ ] 周二：复习特征值直觉、协方差、概率分布、期望。
- [ ] 周三：复习导数、偏导、链式法则、梯度。
- [ ] 周四：实现线性回归 forward 和 MSE loss。
- [ ] 周五：实现梯度下降并画 loss 曲线。
- [ ] 周六：实现 softmax、交叉熵和数值稳定技巧。
- [ ] 周日：手写公式，并用中文解释每段代码。

验收标准：

- [ ] 能不用背诵模板解释梯度下降。
- [ ] 能把公式符号对应到代码变量。

## 第 4 周：传统机器学习与 sklearn

目标：跑通完整机器学习流程，而不是只看概念。

必交付：

- [ ] 分类项目：Logistic Regression、Decision Tree、Random Forest 或 XGBoost
- [ ] 训练/验证/测试集划分
- [ ] 指标表：accuracy、precision、recall、F1、confusion matrix
- [ ] 一篇模型对比报告

每日任务：

- [ ] 周一：学习监督学习流程和数据泄漏。
- [ ] 周二：训练 Logistic Regression baseline。
- [ ] 周三：训练树模型并比较特征重要性。
- [ ] 周四：如果可用，加入 XGBoost 或 GradientBoosting；否则用 RandomForest。
- [ ] 周五：用验证集或交叉验证调参。
- [ ] 周六：整理完整 notebook 和指标表。
- [ ] 周日：写《如果面试官问这个 ML 项目，我怎么讲》。

验收标准：

- [ ] 能解释过拟合、欠拟合、验证集和常见指标。
- [ ] 能独立跑完一个 sklearn 项目。

## 第 5 周：PyTorch 基础

目标：熟悉 tensor、autograd、Dataset、DataLoader 和训练循环。

必交付：

- [ ] PyTorch MLP 分类器
- [ ] 自定义 Dataset 和 DataLoader
- [ ] 包含 loss、optimizer、validation metric 的训练循环
- [ ] 一篇 NumPy 和 PyTorch 对比笔记

每日任务：

- [ ] 周一：学习 tensor 创建、shape 操作、GPU device 切换。
- [ ] 周二：学习 autograd，并手动检查梯度。
- [ ] 周三：写一个简单 MLP forward。
- [ ] 周四：为小型分类数据集实现 Dataset 和 DataLoader。
- [ ] 周五：写训练和验证循环。
- [ ] 周六：训练 MLP，保存 checkpoint，画 loss 曲线。
- [ ] 周日：复盘错误，并解释每个 tensor shape 为什么正确。

验收标准：

- [ ] 能凭记忆写出 PyTorch 训练循环。
- [ ] 能调试 shape mismatch 和 device mismatch。

## 第 6 周：深度学习训练技巧

目标：理解实际训练中的常见现象和失败模式。

必交付：

- [ ] 学习率、正则化、dropout、BatchNorm/LayerNorm 实验
- [ ] 包含配置和结果的实验表格
- [ ] 一篇失败分析笔记

每日任务：

- [ ] 周一：学习 train/val 曲线和过拟合信号。
- [ ] 周二：跑不同学习率对比实验。
- [ ] 周三：跑 weight decay 和 dropout 实验。
- [ ] 周四：加入 BatchNorm 或 LayerNorm，并比较收敛情况。
- [ ] 周五：加入 early stopping 和 checkpoint 选择。
- [ ] 周六：整理实验表格和图。
- [ ] 周日：写哪个因素影响最大，以及为什么。

验收标准：

- [ ] 能诊断至少 5 种常见训练问题。
- [ ] 能做出可用于简历项目的实验表。

## 第 7 周：NLP 基础

目标：理解文本预处理、分词、embedding 和文本分类。

必交付：

- [ ] 文本分类 baseline
- [ ] 分词方案对比笔记
- [ ] 词向量或简单序列模型实验

每日任务：

- [ ] 周一：学习 tokenization、vocabulary、OOV、padding、truncation。
- [ ] 周二：构建 bag-of-words 或 TF-IDF baseline。
- [ ] 周三：训练一个简单文本分类器。
- [ ] 周四：学习 embedding 和序列建模基础。
- [ ] 周五：构建 embedding-based 分类器。
- [ ] 周六：比较 baseline 和神经网络模型。
- [ ] 周日：分析至少 20 个错误预测样例。

验收标准：

- [ ] 能解释分词和文本长度为什么重要。
- [ ] 能快速做出文本分类 baseline。

## 第 8 周：Transformer

目标：理解 attention，并实现一个简化 Transformer block。

必交付：

- [ ] scaled dot-product attention 推导笔记
- [ ] PyTorch 简化 Transformer block
- [ ] Q、K、V、attention score、output 的 shape 追踪笔记

每日任务：

- [ ] 周一：学习 seq2seq 动机和 attention 直觉。
- [ ] 周二：推导 Q、K、V 和 scaled dot-product attention。
- [ ] 周三：实现 single-head attention。
- [ ] 周四：实现 multi-head attention wrapper。
- [ ] 周五：加入 feed-forward、residual connection、LayerNorm。
- [ ] 周六：用 fake input 和 shape assertion 测试 Transformer block。
- [ ] 周日：用 5 分钟录音或文字讲解 Transformer。

验收标准：

- [ ] 能解释 attention 公式和张量形状。
- [ ] 能不盲抄代码实现一个小 Transformer block。

## 第 9 周：Hugging Face 微调

目标：掌握预训练模型的标准 NLP 工程流程。

必交付：

- [ ] 微调后的文本分类模型
- [ ] 数据加载和预处理 pipeline
- [ ] 评估结果和错误样例分析

每日任务：

- [ ] 周一：学习 tokenizer、model、config、dataset、Trainer。
- [ ] 周二：用 `datasets` 加载公开分类数据集。
- [ ] 周三：不微调，先跑 pretrained baseline。
- [ ] 周四：微调 DistilBERT 或小型中文模型。
- [ ] 周五：评估并导出指标。
- [ ] 周六：写 README：命令、环境、结果、样例。
- [ ] 周日：写微调提升了什么，仍然失败在哪里。

验收标准：

- [ ] 能脱离 notebook 使用 Hugging Face 基本流程。
- [ ] 能说明 pretrained model 和 fine-tuned model 的区别。

## 第 10 周：RAG 基础

目标：构建本地文档问答系统，并理解检索质量。

必交付：

- [ ] 本地 RAG demo
- [ ] 文档切分和 embedding pipeline
- [ ] 至少 30 个问题的检索评测集
- [ ] 带架构图的 README

每日任务：

- [ ] 周一：学习 RAG pipeline：文档、切分、embedding、向量索引、检索、生成。
- [ ] 周二：选择文档并实现 chunking。
- [ ] 周三：构建 embedding 和向量搜索。
- [ ] 周四：加入小模型或 API 兼容接口做答案生成。
- [ ] 周五：建立 30 个 QA 测试样例，测 retrieval hit rate。
- [ ] 周六：做一个 CLI、Gradio 或 FastAPI demo。
- [ ] 周日：写失败案例：切分差、上下文缺失、幻觉。

验收标准：

- [ ] 有一个可运行的 RAG 项目。
- [ ] 能区分检索质量和生成质量。

## 第 11 周：LoRA/QLoRA 微调

目标：理解参数高效微调，并完成一个小模型适配实验。

必交付：

- [ ] LoRA 或 QLoRA 微调运行记录
- [ ] loss 曲线或训练日志
- [ ] 微调前后固定 prompt 对比
- [ ] 算力和成本说明

每日任务：

- [ ] 周一：学习 SFT、LoRA、QLoRA、adapter、rank、target modules。
- [ ] 周二：准备小型 instruction dataset。
- [ ] 周三：先在 tiny subset 上跑 smoke test。
- [ ] 周四：跑主微调任务。
- [ ] 周五：固定 prompt，对比 base model 和 fine-tuned model。
- [ ] 周六：写训练报告并保存 config。
- [ ] 周日：判断这个项目是否适合写进简历，还是只作为学习材料。

验收标准：

- [ ] 能解释 LoRA 改了什么，以及没有改什么。
- [ ] 能从 config 和命令复现自己的实验。

## 第 12 周：LLM 评测

目标：学习评估模型行为，而不是只展示好看的样例。

必交付：

- [ ] 评测数据集
- [ ] 人工评测 rubric
- [ ] 自动指标或 judge-model 脚本
- [ ] 错误类型分析报告

每日任务：

- [ ] 周一：定义评测目标：正确性、相关性、忠实性、格式、安全性。
- [ ] 周二：构建至少 50 个测试 prompt 或 QA 样例。
- [ ] 周三：跑 baseline model 评测。
- [ ] 周四：跑 RAG 或微调模型评测。
- [ ] 周五：比较结果并归类错误。
- [ ] 周六：把表格和样例加入项目 README。
- [ ] 周日：准备 5 分钟讲解你的评测方法。

验收标准：

- [ ] 能解释为什么 cherry-picked demo 不够。
- [ ] 项目有指标和错误分析。

## 第 13 周：论文阅读

目标：以实现和面试理解为目的读论文。

必交付：

- [ ] 3 篇论文笔记：Transformer、LoRA、RAG/Agent
- [ ] 一张论文对比表
- [ ] 选定一个复现目标

每日任务：

- [ ] 周一：读 Transformer 论文 abstract、intro、method。
- [ ] 周二：完成 Transformer 笔记：问题、方法、关键公式、局限。
- [ ] 周三：读 LoRA 论文，并和第 11 周实验对应起来。
- [ ] 周四：读一篇 RAG 或 Agent 论文/项目报告。
- [ ] 周五：比较 3 篇论文的问题、方法、实验、局限。
- [ ] 周六：选择一个中等难度复现目标。
- [ ] 周日：写复现计划：数据集、指标、baseline、ablation。

验收标准：

- [ ] 能 5 分钟讲清楚每篇论文。
- [ ] 能判断 1 周内哪些内容真正可复现。

## 第 14 周：论文或开源项目复现

目标：复现一个有意义的结果，并做一个小 ablation。

必交付：

- [ ] 复现仓库或文件夹
- [ ] baseline 结果
- [ ] 至少一个 ablation
- [ ] 复现报告

每日任务：

- [ ] 周一：搭建代码和环境。
- [ ] 周二：跑官方 baseline 或最小 baseline。
- [ ] 周三：确认数据 pipeline 和指标计算没有问题。
- [ ] 周四：跑主复现实验。
- [ ] 周五：跑一个 ablation：超参数、组件移除、chunk size、rank 或 prompt 格式。
- [ ] 周六：写结果表，并和原始结论对比。
- [ ] 周日：写局限性，以及如果有更多算力会怎么改。

验收标准：

- [ ] 能区分“代码跑起来了”和“结果被复现了”。
- [ ] 报告包含失败案例和诚实缺口。

## 第 15 周：作品集整合

目标：把学习材料打磨成可面试项目。

必交付：

- [ ] 项目 1 打磨完成：ML 或 NLP baseline 项目
- [ ] 项目 2 打磨完成：RAG 或 LLM 微调项目
- [ ] 项目 3 总结完成：论文复现
- [ ] 作品集 README 和架构图

每日任务：

- [ ] 周一：选择两个最强项目，删除站不住的描述。
- [ ] 周二：重写 README：背景、方法、运行命令、结果、局限。
- [ ] 周三：补架构图和实验表。
- [ ] 周四：补 demo 截图或短录屏。
- [ ] 周五：写带指标和技术深度的简历 bullet。
- [ ] 周六：练习每个项目 5 分钟讲解。
- [ ] 周日：找人或用 AI 工具追问你的项目解释。

验收标准：

- [ ] 至少 2 个项目能经受细问。
- [ ] 至少 1 个项目有真实实验对比。

## 第 16 周：简历与面试

目标：把学习转化成求职准备。

必交付：

- [ ] 简历 v1
- [ ] ML/DL/LLM 面试题库
- [ ] 3 次项目模拟讲解
- [ ] 下一阶段 8 周补弱计划

每日任务：

- [ ] 周一：写简历：教育背景、技能、项目、链接。
- [ ] 周二：准备 ML 高频题：过拟合、指标、LR、树模型、XGBoost。
- [ ] 周三：准备 DL 高频题：反向传播、优化器、归一化、dropout、CNN/RNN 基础。
- [ ] 周四：准备 LLM 高频题：Transformer、attention、RAG、LoRA、评测。
- [ ] 周五：模拟面试 1：项目深挖。
- [ ] 周六：模拟面试 2 和 3，记录薄弱答案。
- [ ] 周日：根据薄弱点和目标岗位 JD，制定下一阶段 8 周计划。

验收标准：

- [ ] 能用 5 分钟讲清楚项目背景、方法、指标、失败案例和改进方向。
- [ ] 简历上没有任何一句你讲不清或守不住的项目描述。
