import joblib


def load_model():
    model = joblib.load("models/fifa_model.pkl")
    encoders = joblib.load("models/encoder.pkl")
    return model, encoders


def predict_match(model, encoders, home_team, away_team,
                  tournament, city, country, neutral):

    home_team = encoders["home_team"].transform([home_team])[0]
    away_team = encoders["away_team"].transform([away_team])[0]
    tournament = encoders["tournament"].transform([tournament])[0]
    city = encoders["city"].transform([city])[0]
    country = encoders["country"].transform([country])[0]
    neutral = encoders["neutral"].transform([neutral])[0]

    prediction = model.predict([[
        home_team,
        away_team,
        tournament,
        city,
        country,
        neutral
    ]])

    result = encoders["result"].inverse_transform(prediction)
    return result[0]
