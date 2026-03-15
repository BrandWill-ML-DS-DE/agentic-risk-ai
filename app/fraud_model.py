import pandas as pd
import xgboost as xgb
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

MODEL_PATH = "app/fraud_model.pkl"

def train_model():
    df = pd.read_csv("data/transactions.csv")

    X = df.drop("is_fraud", axis=1)
    y = df["is_fraud"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = xgb.XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1
    )

    mlflow.start_run()

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    print(classification_report(y_test, preds))

    mlflow.log_param("n_estimators", 200)
    mlflow.log_metric("accuracy", (preds == y_test).mean())

    joblib.dump(model, MODEL_PATH)

    mlflow.end_run()

    return model


def load_model():
    return joblib.load(MODEL_PATH)