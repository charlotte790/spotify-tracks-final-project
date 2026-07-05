"""
Part 6-8: Basic Machine Learning Models

Author: Siyuan

This file matches the final group plan for Person 3:
- Part 6: Logistic Regression
- Part 7: KNN
- Part 8: Decision Tree
- Basic model evaluation with Accuracy, Precision, Recall, and F1-score

If the prepared variables from Person 2 already exist, this file uses them:
X_train_scaled, X_test_scaled, y_train, y_test

If they do not exist, this file prepares the same modeling variables from
dataset/dataset.csv so it can still run independently in PyCharm.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import GroupShuffleSplit
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def prepare_data_if_needed():
    """
    Use Person 2's prepared data if available.
    Otherwise, reproduce the minimum required preparation steps so this file
    can be run independently.
    """
    required_objects = ["X_train_scaled", "X_test_scaled", "y_train", "y_test"]
    if all(name in globals() for name in required_objects):
        print("Using prepared data from Person 2.")
        return

    print("Prepared variables were not found. Preparing data from dataset.csv...")

    data_path = PROJECT_ROOT / "dataset" / "dataset.csv"
    if not data_path.exists():
        data_path = Path("../dataset/dataset.csv")

    df = pd.read_csv(data_path)

    df_clean = df.copy()
    if "Unnamed: 0" in df_clean.columns:
        df_clean = df_clean.drop(columns=["Unnamed: 0"])

    df_clean = df_clean.drop_duplicates()
    df_clean = df_clean.dropna(subset=["track_id", "track_genre"])

    selected_features = [
        "danceability",
        "energy",
        "key",
        "loudness",
        "mode",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
        "time_signature",
    ]

    X = df_clean[selected_features].copy()
    y = df_clean["track_genre"].copy()
    groups = df_clean["track_id"].copy()

    group_split = GroupShuffleSplit(
        n_splits=1,
        test_size=0.2,
        random_state=42,
    )

    train_index, test_index = next(group_split.split(X, y, groups=groups))

    X_train = X.iloc[train_index].copy()
    X_test = X.iloc[test_index].copy()

    globals()["y_train"] = y.iloc[train_index].copy()
    globals()["y_test"] = y.iloc[test_index].copy()

    groups_train = groups.iloc[train_index].copy()
    groups_test = groups.iloc[test_index].copy()
    overlap = set(groups_train).intersection(set(groups_test))

    scaler = StandardScaler()
    globals()["X_train_scaled"] = pd.DataFrame(
        scaler.fit_transform(X_train),
        columns=selected_features,
        index=X_train.index,
    )
    globals()["X_test_scaled"] = pd.DataFrame(
        scaler.transform(X_test),
        columns=selected_features,
        index=X_test.index,
    )

    print("Training rows:", X_train.shape[0])
    print("Test rows:", X_test.shape[0])
    print("Overlapping track_id count:", len(overlap))


prepare_data_if_needed()


# Evaluation helper
results = []


def evaluate_model(model_name, model):
    """
    Train one model and evaluate it with the same metrics.
    Weighted metrics are used because this is a multi-class genre task.
    """
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)

    result = {
        "Model": model_name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision_weighted": precision_score(
            y_test,
            y_pred,
            average="weighted",
            zero_division=0,
        ),
        "Recall_weighted": recall_score(
            y_test,
            y_pred,
            average="weighted",
            zero_division=0,
        ),
        "F1_weighted": f1_score(
            y_test,
            y_pred,
            average="weighted",
            zero_division=0,
        ),
        "F1_macro": f1_score(
            y_test,
            y_pred,
            average="macro",
            zero_division=0,
        ),
    }

    results.append(result)

    print("\n" + "=" * 80)
    print(f"Classification Report: {model_name}")
    print("=" * 80)
    print(classification_report(y_test, y_pred, zero_division=0))

    return model, y_pred


# Part 6: Logistic Regression
logistic_regression = LogisticRegression(
    max_iter=2000,
    random_state=42,
    n_jobs=-1,
)

logistic_regression_model, logistic_regression_pred = evaluate_model(
    "Logistic Regression",
    logistic_regression,
)


# Part 7: KNN
knn = KNeighborsClassifier(
    n_neighbors=5,
    n_jobs=-1,
)

knn_model, knn_pred = evaluate_model(
    "KNN",
    knn,
)


# Part 8: Decision Tree
decision_tree = DecisionTreeClassifier(
    random_state=42,
)

decision_tree_model, decision_tree_pred = evaluate_model(
    "Decision Tree",
    decision_tree,
)


# Basic model evaluation summary
results_df = pd.DataFrame(results)
results_df = results_df.sort_values("F1_weighted", ascending=False)

print("\nBasic Model Evaluation Summary:")
print(results_df)

results_dir = PROJECT_ROOT / "results"
results_dir.mkdir(exist_ok=True)
results_df.to_csv(results_dir / "siyuan_part6_8_basic_model_results.csv", index=False)

figures_dir = PROJECT_ROOT / "figures"
figures_dir.mkdir(exist_ok=True)

plt.figure(figsize=(8, 5))
plt.bar(results_df["Model"], results_df["F1_weighted"])
plt.title("Basic Model Comparison by Weighted F1-score")
plt.ylabel("Weighted F1-score")
plt.ylim(0, max(results_df["F1_weighted"]) * 1.15)
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig(figures_dir / "siyuan_basic_model_f1_comparison.png", dpi=300)
plt.show()

best_model_name = results_df.iloc[0]["Model"]
best_f1 = results_df.iloc[0]["F1_weighted"]

print("\nInterpretation:")
print(
    f"Among the three basic machine learning models, {best_model_name} achieved "
    f"the best weighted F1-score ({best_f1:.4f}). These baseline results provide "
    "a reference point for the later advanced models, especially Random Forest "
    "and Neural Network."
)
