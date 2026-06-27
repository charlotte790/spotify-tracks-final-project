# Spotify Tracks 音乐类型分类项目

本项目为 **Python and Advanced Data Science** 课程最终小组项目。项目基于 Spotify Tracks Dataset，使用歌曲的音频特征进行数据分析，并构建机器学习 / 深度学习模型预测歌曲的音乐类型 `track_genre`。

## 数据集

数据文件位于：

```text
dataset/dataset.csv
```

目标变量为：

```text
track_genre
```

主要使用的特征包括歌曲的音频属性，例如：

- popularity
- duration_ms
- danceability
- energy
- loudness
- acousticness
- instrumentalness
- valence
- tempo

## GitHub 使用规范

为避免多人同时修改同一文件造成冲突，本项目采用分支协作方式。

### 1. 每个人使用自己的分支

不要直接在 `main` 分支上修改文件。每位成员应创建自己的分支进行开发，例如：

```text
xinran-working
siyuan-working
heyi-working
weiye-working
```

### 2. 每个人维护自己的 Notebook

每位成员在 `notebooks/` 文件夹中创建自己的 notebook，例如：

```text
notebooks/xinran_work.ipynb
notebooks/siyuan_work.ipynb
notebooks/heyi_work.ipynb
notebooks/weiye_work.ipynb
```

可以查看和运行其他成员的代码，但不要直接修改他人的 notebook。

如果发现其他成员的代码有问题，可以在小组内沟通，或在自己的 notebook 中测试修改方案。

### 3. 提交自己的修改

完成修改后，将自己的 notebook 提交到自己的分支。

示例：

```bash
git add notebooks/your_notebook.ipynb
git commit -m "update notebook"
git push origin your-branch-name
```

### 4. 合并前检查

合并到 `main` 前，请确认：

- notebook 可以正常打开
- 主要代码可以运行
- 没有修改或删除他人的文件
- 没有上传无关文件

建议通过 Pull Request 合并到 `main`，不要直接覆盖主分支内容。

## 项目结构

```text
spotify-tracks-final-project/
├── dataset/          # 数据集
├── notebooks/        # 小组成员的 notebooks
├── figures/          # 图表文件
├── results/          # 模型结果
├── requirement/      # 老师提供的项目要求
├── README.md
├── requirements.txt
└── .gitignore
```

## Notebook 建议框架

最终 notebook 建议按照以下结构整理：

```text
1. Project Introduction
2. Dataset Overview
3. Data Cleaning
4. Exploratory Data Analysis
5. Data Preprocessing
6. Baseline Models
7. Advanced Models
8. Hyperparameter Tuning
9. Model Evaluation and Comparison
10. Conclusion
```

每一部分应包含代码和必要的文字说明，解释做了什么、为什么这样做，以及结果说明了什么。

---

# Spotify Tracks Genre Classification Project

This is the final group project for the **Python and Advanced Data Science** course. The project is based on the Spotify Tracks Dataset. We use audio features of songs for data analysis and build machine learning / deep learning models to predict the music genre `track_genre`.

## Dataset

The dataset file is located at:

```text
dataset/dataset.csv
```

The target variable is:

```text
track_genre
```

The main features are audio attributes of songs, such as:

- popularity
- duration_ms
- danceability
- energy
- loudness
- acousticness
- instrumentalness
- valence
- tempo

## GitHub Rules

To avoid conflicts caused by multiple people editing the same file, this project uses a branch-based workflow.

### 1. Each member uses their own branch

Do not modify files directly on the `main` branch. Each member should create their own branch for development, for example:

```text
xinran-working
siyuan-working
heyi-working
weiye-working
```

### 2. Each member maintains their own Notebook

Each member should create their own notebook in the `notebooks/` folder, for example:

```text
notebooks/xinran_work.ipynb
notebooks/siyuan_work.ipynb
notebooks/heyi_work.ipynb
notebooks/weiye_work.ipynb
```

You may view and run other members' code, but do not directly modify another member's notebook.

If you find an issue in someone else's code, discuss it with the group or test your solution in your own notebook.

### 3. Commit your own changes

After finishing your changes, commit your notebook to your own branch.

Example:

```bash
git add notebooks/your_notebook.ipynb
git commit -m "update notebook"
git push origin your-branch-name
```

### 4. Check before merging

Before merging into `main`, please make sure that:

- the notebook can be opened correctly
- the main code cells can run
- you did not modify or delete other members' files
- no unrelated files are uploaded

It is recommended to merge through a Pull Request instead of directly overwriting the main branch.

## Project Structure

```text
spotify-tracks-final-project/
├── dataset/          # dataset
├── notebooks/        # team members' notebooks
├── figures/          # figures and plots
├── results/          # model results
├── requirement/      # project requirements from the instructor
├── README.md
├── requirements.txt
└── .gitignore
```

## Suggested Notebook Framework

The final notebook is recommended to follow this structure:

```text
1. Project Introduction
2. Dataset Overview
3. Data Cleaning
4. Exploratory Data Analysis
5. Data Preprocessing
6. Baseline Models
7. Advanced Models
8. Hyperparameter Tuning
9. Model Evaluation and Comparison
10. Conclusion
```

Each section should include both code and necessary explanations, describing what was done, why it was done, and what the results mean.
