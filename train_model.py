import os
import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("dataset/t20_cricket_dataset.csv")

# -----------------------------
# Features
# -----------------------------
X = df.drop("FinalScore", axis=1)
y = df["FinalScore"]

categorical_features = [
    "BattingTeam",
    "BowlingTeam"
]

numeric_features = [
    "CurrentScore",
    "Overs",
    "Wickets",
    "RunsLast5",
    "WicketsLast5"
]

# -----------------------------
# Preprocessing
# -----------------------------
preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "num",
            "passthrough",
            numeric_features
        )
    ]
)

# -----------------------------
# Model
# -----------------------------
model = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])

pipeline.fit(X, y)

# Save to model folder in the project root (not /tmp)
os.makedirs("model", exist_ok=True)
joblib.dump(pipeline, "model/cricket_score_model.pkl")

print("✅ Model trained and saved to model/cricket_score_model.pkl")
