import shap
import pandas as pd
import joblib

MODEL_PATH = "app/fraud_model.pkl"

def generate_explanation(transaction_dict):
    model = joblib.load(MODEL_PATH)
    explainer = shap.TreeExplainer(model)

    df = pd.DataFrame([transaction_dict])

    shap_values = explainer.shap_values(df)

    feature_importance = dict(
        zip(df.columns, shap_values[0])
    )

    return sorted(
        feature_importance.items(),
        key=lambda x: abs(x[1]),
        reverse=True
    )