import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib


def preprocess_data():
    df = pd.read_csv("data/final_dataset.csv")
    encoders = {}
    for column in ["home_team",
                   "away_team",
                   "tournament",
                   "city",
                   "country",
                   "neutral",
                   "result"
                   ]:
        encoder = LabelEncoder()
        df[column] = encoder.fit_transform(df[column])
        encoders[column] = encoder
        joblib.dump(encoders, "models/encoder.pkl")
    return df
