# Spotify Tracks Genre Classification Project

## 中文版

### 项目简介

本项目基于 **Spotify Tracks Dataset**，使用歌曲的音频特征进行数据分析，并构建机器学习 / 深度学习模型来预测歌曲的音乐类型 `track_genre`。

主要任务是理解数据、清洗数据、进行探索性数据分析，并比较不同模型在音乐类型分类任务上的表现。

---

### GitHub 使用规范

为了避免多人同时修改同一个文件造成冲突，本项目采用 **每个人单独建立分支、只更新自己负责的 notebook** 的协作方式。

#### 1. 不要直接修改 `main` 分支

`main` 分支只用于保存稳定版本。所有成员都不应该直接在 `main` 分支上修改文件。

每次开始工作前，先从 `main` 创建自己的分支，例如：

```bash
git checkout main
git pull origin main
git checkout -b your-name-working-branch
```

分支命名示例：

```text
xinran-working
siyuan-working
heyi-working
weiye-working
```

也可以按照任务命名：

```text
feature/data-cleaning
feature/eda
feature/baseline-models
feature/advanced-models
```

---

#### 2. 每个人只更新自己的 notebook

每位成员应该在 `notebooks/` 文件夹中创建并维护自己的工作 notebook，例如：

```text
notebooks/xinran_work.ipynb
notebooks/siyuan_work.ipynb
notebooks/heyi_work.ipynb
notebooks/weiye_work.ipynb
```

可以查看其他成员的 notebook，也可以运行和测试其他成员的代码，但不要直接修改其他成员的 notebook。

如果发现其他成员的代码有问题，建议：

1. 在小组沟通中说明问题；
2. 或者在自己的分支中进行测试；
3. 不要直接覆盖别人的文件。

---

#### 3. 每次更新前先同步远程仓库

开始工作前建议先执行：

```bash
git checkout main
git pull origin main
git checkout your-name-working-branch
git merge main
```

这样可以保证自己的分支基于最新版本，减少后续合并冲突。

---

#### 4. 提交代码时写清楚 commit message

每次完成一个小更新后，使用清楚的 commit message。

示例：

```bash
git add notebooks/xinran_work.ipynb
git commit -m "update data cleaning notebook"
git push origin xinran-working
```

推荐的 commit message 风格：

```text
update data cleaning notebook
add EDA visualizations
add baseline model results
fix preprocessing code
update model comparison table
```

---

#### 5. 合并到 `main` 前先检查

将自己的分支合并到 `main` 前，需要确认：

- notebook 可以正常打开；
- 主要代码 cell 可以正常运行；
- 没有误删其他人的文件；
- 没有上传无关的大文件或临时文件；
- 图表、结果表和说明文字是清楚的。

建议通过 Pull Request 合并到 `main`，不要直接强制 push。

---

#### 6. 不要上传无关文件

请不要上传以下内容：

```text
.DS_Store
.ipynb_checkpoints/
__pycache__/
临时测试文件
本地环境文件
过大的模型文件
无关截图
```

如果需要保存图表，可以放在：

```text
figures/
```

如果需要保存模型结果表，可以放在：

```text
results/
```

---

### 建议的仓库结构

```text
spotify-tracks-final-project/
├── dataset/                 # 数据集和数据说明
├── notebooks/               # 每位成员的工作 notebook 和最终 notebook
├── figures/                 # 可视化图表
├── results/                 # 模型评价结果和比较表
├── requirement/             # 老师提供的项目要求文件
├── README.md                # 项目说明和 GitHub 使用规范
├── requirements.txt         # Python 依赖包
└── .gitignore               # Git 忽略规则
```

---

### Notebook 建议框架

最终 notebook 可以按照下面的结构整理。每一部分不仅需要代码，也需要 Markdown 解释说明“做了什么、为什么这样做、结果说明了什么”。

```text
1. Project Introduction
   - 项目背景
   - 问题定义
   - 项目目标

2. Dataset Overview
   - 数据来源
   - 数据规模
   - 字段说明
   - 目标变量说明

3. Data Cleaning
   - 缺失值检查和处理
   - 重复值检查和处理
   - 异常值检查和处理
   - 删除无用字段

4. Exploratory Data Analysis
   - 音乐类型分布
   - popularity 分布
   - 主要音频特征分布
   - 相关性分析
   - 不同音乐类型之间的特征比较

5. Data Preprocessing
   - 特征选择
   - 类别变量编码
   - 标准化 / 归一化
   - train-test split

6. Baseline Models
   - Logistic Regression
   - KNN
   - Decision Tree
   - 初步模型评价

7. Advanced Models
   - Random Forest / ensemble model
   - Neural Network / deep learning model

8. Hyperparameter Tuning
   - 调参方法
   - 调参前后结果比较

9. Model Evaluation and Comparison
   - Accuracy
   - Macro F1-score
   - Weighted F1-score
   - 模型结果比较表
   - 错误分析

10. Conclusion
   - 主要发现
   - 最佳模型
   - 项目限制
   - 未来改进方向
```

---

## English Version

### Project Overview

This project is based on the **Spotify Tracks Dataset**. The goal is to analyze audio features of songs and build machine learning / deep learning models to predict the music genre, represented by `track_genre`.

The main workflow includes understanding the dataset, cleaning the data, performing exploratory data analysis, and comparing different models for the music genre classification task.

---

### GitHub Collaboration Rules

To avoid conflicts caused by multiple people editing the same file at the same time, this project follows a **separate-branch and separate-notebook workflow**.

#### 1. Do not directly modify the `main` branch

The `main` branch should only contain stable versions of the project. Team members should not work directly on `main`.

Before starting your work, create your own branch from `main`:

```bash
git checkout main
git pull origin main
git checkout -b your-name-working-branch
```

Example branch names:

```text
xinran-working
siyuan-working
heyi-working
weiye-working
```

Task-based branch names are also acceptable:

```text
feature/data-cleaning
feature/eda
feature/baseline-models
feature/advanced-models
```

---

#### 2. Each member should only update their own notebook

Each member should create and maintain their own working notebook inside the `notebooks/` folder, for example:

```text
notebooks/xinran_work.ipynb
notebooks/siyuan_work.ipynb
notebooks/heyi_work.ipynb
notebooks/weiye_work.ipynb
```

You may view other members' notebooks and run their code for testing, but you should not directly modify another member's notebook.

If you find an issue in someone else's code, please:

1. Discuss it with the team;
2. Test it in your own branch if needed;
3. Do not overwrite another member's file directly.

---

#### 3. Sync with the remote repository before updating your work

Before starting your work, it is recommended to run:

```bash
git checkout main
git pull origin main
git checkout your-name-working-branch
git merge main
```

This keeps your branch up to date and reduces merge conflicts later.

---

#### 4. Use clear commit messages

After completing a small update, commit it with a clear message.

Example:

```bash
git add notebooks/xinran_work.ipynb
git commit -m "update data cleaning notebook"
git push origin xinran-working
```

Recommended commit message examples:

```text
update data cleaning notebook
add EDA visualizations
add baseline model results
fix preprocessing code
update model comparison table
```

---

#### 5. Check your work before merging into `main`

Before merging your branch into `main`, make sure that:

- the notebook can be opened correctly;
- the main code cells can run successfully;
- you did not accidentally delete other members' files;
- no unrelated large files or temporary files are uploaded;
- figures, result tables, and explanations are clear.

It is recommended to merge through a Pull Request instead of force pushing directly to `main`.

---

#### 6. Do not upload unrelated files

Please avoid uploading files such as:

```text
.DS_Store
.ipynb_checkpoints/
__pycache__/
temporary test files
local environment files
large model files
unrelated screenshots
```

If you need to save figures, place them in:

```text
figures/
```

If you need to save model result tables, place them in:

```text
results/
```

---

### Suggested Repository Structure

```text
spotify-tracks-final-project/
├── dataset/                 # Dataset and dataset description
├── notebooks/               # Working notebooks and final notebook
├── figures/                 # Visualization outputs
├── results/                 # Model evaluation results and comparison tables
├── requirement/             # Project requirement files provided by the instructor
├── README.md                # Project description and GitHub collaboration rules
├── requirements.txt         # Python dependencies
└── .gitignore               # Git ignore rules
```

---

### Suggested Notebook Framework

The final notebook can be organized using the following structure. Each section should include both code and Markdown explanations describing what was done, why it was done, and what the results mean.

```text
1. Project Introduction
   - Background
   - Problem statement
   - Project goals

2. Dataset Overview
   - Data source
   - Dataset size
   - Column descriptions
   - Target variable explanation

3. Data Cleaning
   - Missing value checking and handling
   - Duplicate checking and handling
   - Invalid value checking and handling
   - Removing unnecessary columns

4. Exploratory Data Analysis
   - Genre distribution
   - Popularity distribution
   - Main audio feature distributions
   - Correlation analysis
   - Feature comparison across genres

5. Data Preprocessing
   - Feature selection
   - Categorical encoding
   - Standardization / normalization
   - Train-test split

6. Baseline Models
   - Logistic Regression
   - KNN
   - Decision Tree
   - Initial model evaluation

7. Advanced Models
   - Random Forest / ensemble model
   - Neural Network / deep learning model

8. Hyperparameter Tuning
   - Tuning methods
   - Comparison before and after tuning

9. Model Evaluation and Comparison
   - Accuracy
   - Macro F1-score
   - Weighted F1-score
   - Model comparison table
   - Error analysis

10. Conclusion
   - Main findings
   - Best model
   - Limitations
   - Future improvements
```
