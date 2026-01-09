import joblib
import pandas as pd
#importing columns
columns = joblib.load("models/columns.pkl")
#importing model
model = joblib.load("models/model.pkl")

def predict(data : dict):
    df = pd.DataFrame([data])

    #making them to lower case
    df["company"] = df["company"].astype(str).str.lower().str.strip()
    df["role"] = df["role"].astype(str).str.lower().str.strip()
    df["platform"] = df["platform"].astype(str).str.lower().str.strip()

    df_encoded = pd.get_dummies(df, columns=['company', 'role', 'platform'])
    #making those trained columns into it
    df_aligned = df_encoded.reindex(columns=columns, fill_value=0)

    #reason we use [0][1] as index is the first index [0][0] returns the probability of failure and
    #[0][1] returns the probability of success and it's a numpy array (2d)

    probability = model.predict_proba(df_aligned)[0][1]

    return probability

