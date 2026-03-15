from fastapi import FastAPI
from app.fraud_model import load_model
from app.agents import run_investigation
import pandas as pd

app = FastAPI()

model = load_model()

@app.post("/analyze")
def analyze_transaction(transaction: dict):

    df = pd.DataFrame([transaction])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    investigation = run_investigation(transaction)

    return {
        "fraud_prediction": int(prediction),
        "fraud_probability": float(probability),
        "agent_report": investigation
    }