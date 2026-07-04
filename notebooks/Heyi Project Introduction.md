# 1. Project Introduction

## Background

Music streaming platforms such as Spotify receive thousands of newly uploaded songs every day. To organize these songs efficiently and provide personalized recommendations, accurate genre classification is essential. However, manually assigning genre labels is time-consuming and difficult to scale. Therefore, automatic music genre classification using machine learning has become an important application in music information retrieval.

## Problem Statement

The Spotify Tracks dataset contains songs from **114 different music genres**, making genre classification a challenging multi-class classification problem. Many genres share similar acoustic characteristics, leading to overlapping decision boundaries and making accurate prediction difficult.

Rather than simplifying the problem by reducing the number of classes, this project preserves all **114 original genres** to evaluate whether machine learning models can learn meaningful distinctions from audio features alone.

## Research Questions

This project aims to answer the following questions:

1. **Can audio features accurately predict a song's music genre?**
2. **Which machine learning model performs best on a large-scale multi-class classification task?**
3. **Which audio features contribute most to distinguishing different music genres?**
4. **Besides Top-1 Accuracy, can Top-3 Accuracy provide a more informative evaluation for music genre prediction?**

## Project Objective

The objective of this project is to develop and compare multiple machine learning models for automatic music genre classification using Spotify audio features. The project includes data cleaning, exploratory data analysis, feature preprocessing, baseline machine learning models, advanced ensemble and deep learning models, hyperparameter tuning, and model comparison.

Considering the large number of genre categories and their similarity, the project evaluates model performance using not only traditional metrics such as Accuracy, Precision, Recall, and F1-score, but also Top-3 Accuracy to assess whether the correct genre appears among the model's three most confident predictions. This provides a more practical evaluation for real-world music recommendation systems.
