from fastapi import FastAPI
import joblib
import numpy as np 
import pandas as pd
import os

app = FastAPI(title="Loan Prediction Default API")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR,"model")

models = [joblib.load(os.path.join(MODEL_DIR,f"lgb_fold_{i+1}.pkl")) for i in range(5)]
features_col = joblib.load(os.path.join(MODEL_DIR,'features_cols.pkl'))
cat_col = joblib.load(os.path.join(MODEL_DIR,'cat_cols.pkl'))

def preprocess(df):
    for col in cat_col:
        df[col] = df[col].astype('category')

    df = df[features_col]
    return df

@app.post("/predict")
def predict(data:dict):
    df = pd.DataFrame([data])
    df = preprocess(df)

    preds = np.mean(
        [model.predict_proba(df)[:,1] for model in models],
        axis = 0
    )

    return{
        "loan_default_probability":float(preds[0]),
        "loan_status" : int(preds[0]>0.5)

    }