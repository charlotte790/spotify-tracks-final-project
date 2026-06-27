# Spotify Tracks 音乐类型分类项目 / Spotify Tracks Genre Classification Project

这是 **Python and Advanced Data Science** 课程的最终小组项目。  
This is the final group project for the **Python and Advanced Data Science** course.

---

## 项目目标 / Project Goal

本项目使用 **Spotify Tracks Dataset**，对歌曲的音频特征进行分析，并构建机器学习 / 深度学习模型来预测歌曲的音乐类型 `track_genre`。

This project uses the **Spotify Tracks Dataset** to analyze audio features of songs and build machine learning / deep learning models to predict the music genre, represented by `track_genre`.

简单来说，我们希望回答：  
In simple terms, we want to answer:

> 能否根据一首歌的 `danceability`、`energy`、`tempo`、`acousticness`、`valence` 等音频特征，预测它属于哪一种音乐类型？  
> Can we predict the genre of a song based on audio features such as `danceability`, `energy`, `tempo`, `acousticness`, and `valence`?

---

## 数据集说明 / Dataset Description

- 数据集 / Dataset: Spotify Tracks Dataset
- 本地数据文件 / Local data file: `dataset/dataset.csv`
- 目标变量 / Target variable: `track_genre`
- 任务类型 / Task type: 多分类任务 / Multi-class classification

主要特征包括 / Main features include:

- `popularity`
- `duration_ms`
- `explicit`
- `danceability`
- `energy`
- `key`
- `loudness`
- `mode`
- `speechiness`
- `acousticness`
- `instrumentalness`
- `liveness`
- `valence`
- `tempo`
- `time_signature`

---

## 项目文件结构 / Project Structure

```text
Final_Project/
├── dataset/                 # 原始数据集和数据说明 / Raw dataset and dataset description
├── notebooks/               # 工作 notebook 和最终 notebook / Working notebooks and final notebook
├── figures/                 # 图表输出 / Exported figures and plots
├── results/                 # 模型结果表格 / Model result tables
├── requirement/             # 老师提供的项目要求 PDF / Requirement PDFs provided by the instructor
├── README.md                # 项目说明文件 / Project documentation
├── requirements.txt         # Python 依赖包 / Python dependencies
└── .gitignore               # Git 忽略规则 / Git ignore rules
```

---

## 推荐分工方式 / Recommended Team Division

建议小组按照以下方式分工：  
The team is recommended to divide the work as follows:

### 1. Final Notebook + PPT 整合 / Final Notebook and Presentation Integration

- 整合最终 notebook / Integrate the final notebook
- 编写 Markdown 解释 / Write Markdown explanations
- 整理最终 presentation / Prepare the final presentation
- 检查老师要求是否全部覆盖 / Check whether all instructor requirements are covered

### 2. 数据清洗、数据准备和 EDA / Data Cleaning, Data Preparation, and EDA

- 加载数据 / Load the dataset
- 检查缺失值、重复值和异常值 / Check missing values, duplicates, and invalid values
- 完成数据清洗和预处理准备 / Complete data cleaning and preparation
- 进行探索性数据分析和可视化 / Perform exploratory data analysis and visualization

### 3. 基础模型 / Baseline Models

- Logistic Regression
- KNN
- Decision Tree
- 输出基础模型评价结果 / Report baseline model evaluation results

### 4. 高级模型、调参和最终比较 / Advanced Models, Tuning, and Final Comparison

- Random Forest，作为 ensemble model / Random Forest as the ensemble model
- Neural Network / MLP，作为 deep learning model / Neural Network or MLP as the deep learning model
- Hyperparameter tuning
- 最终模型比较和结论分析 / Final model comparison and conclusion analysis

---

## 模型评价指标 / Evaluation Metrics

所有模型建议统一汇报以下指标，方便公平比较：  
All models should report the following metrics for fair comparison:

- Accuracy
- Macro F1-score
- Weighted F1-score

---

## 最终提交内容 / Final Submission

根据老师要求，最终需要提交：  
According to the instructor's requirements, the final submission should include:

- Final Jupyter Notebook `.ipynb`
- Presentation Slides

---

## 协作建议 / Collaboration Suggestions

- 不建议多人同时编辑同一个 notebook。  
  It is not recommended that multiple members edit the same notebook at the same time.

- 建议每个人先完成自己负责的部分，再由一名同学整合成最终 notebook。  
  Each member should complete their own section first, and then one member should integrate everything into the final notebook.

- 所有模型应使用相同的数据清洗规则、特征列表、train-test split 和评价指标。  
  All models should use the same data cleaning rules, feature list, train-test split, and evaluation metrics.

- 每个人需要在最终 notebook 或 slides 中写清楚自己的贡献。  
  Each member should clearly state their contribution in the final notebook or slides.
