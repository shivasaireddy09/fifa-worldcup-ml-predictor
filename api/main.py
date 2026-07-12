from fastapi.middleware.cors import CORSMiddleware
import joblib
from pprint import pp

from fastapi import FastAPI
from pydantic import BaseModel

from src.predict import predict_match


class MatchRequest(BaseModel):
    home_team: str
    away_team: str
    tournament: str
    city: str
    country: str
    neutral: bool


app = FastAPI(
    title="FIFA world cup predictor",
    description="Predict FIFA World cup match results using Machine Learning ",
    version="1.0.0"
)
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )

model = joblib.load("models/fifa_model.pkl")
encoder = joblib.load("models/encoder.pkl")

# can make a single end point instead of making too many same endpoints @app.get


@app.get("/")
def home():
    return {
        "message": "welcome to FIFA world cup prediction API"
    }


@app.get("/teams")
def get_teams():
    return {
        "teams": sorted(encoder["home_team"].classes_.tolist())
    }


@app.get("/tournaments")
def get_tournaments():
    return {
        "tournaments": sorted(encoder["tournament"].classes_.tolist())
    }


@app.get("/cities")
def get_cities():
    return {
        "cities": sorted(encoder["city"].classes_.tolist())

    }


@app.get("/countries")
def get_countries():
    return {
        "countries": sorted(encoder["country"].classes_.tolist())
    }


@app.get("/neutral-options")
def neutral():
    return {
        "neutral": [True, False]
    }


@app.post("/predict")
def predict(data: MatchRequest):
    prediction = predict_match(model, encoder, data.home_team, data.away_team,
                               data.tournament, data.city, data.country, str(data.neutral))
    pred = prediction.strip().lower()
    if "home" in pred:
        winner = data.home_team
    elif "away" in pred:
        winner = data.away_team
    elif "draw" in pred:
        winner = "draw"
    else:
        winner = prediction
    return {
        "prediction": winner

    }
