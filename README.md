# Spotify Tracks Genre Classification

Final group project for Python and Advanced Data Science.

## Project Goal

Use the Spotify Tracks Dataset to analyze audio features and build machine learning / deep learning models to predict `track_genre`.

## Dataset

- Source: Spotify Tracks Dataset
- Local file: `dataset/dataset.csv`
- Target variable: `track_genre`
- Task type: multi-class classification

## Suggested Project Structure

```text
Final_Project/
├── dataset/                 # raw and cleaned datasets
├── notebooks/               # working notebooks and final notebook
├── figures/                 # exported plots for notebook and slides
├── results/                 # model result tables
├── slides/                  # final presentation
├── requirement/             # teacher requirement PDFs
├── README.md
├── requirements.txt
└── .gitignore
```

## Team Workflow

Recommended division:

1. Final Notebook + PPT integration
2. Data cleaning, preparation, and EDA
3. Baseline models: Logistic Regression, KNN, Decision Tree
4. Advanced models: Random Forest, Neural Network, tuning, final comparison

## Evaluation Metrics

All models should report:

- Accuracy
- Macro F1-score
- Weighted F1-score

## Submission

Submit:

- Final Jupyter Notebook `.ipynb`
- Final Presentation Slides
