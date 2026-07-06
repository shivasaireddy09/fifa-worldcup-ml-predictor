from src.preprocess import preprocess_data
from src.train import train_model

from src.evaluate import evaluate_model
from src.predict import load_model
from src.predict import predict_match, load_model
df = preprocess_data()
model, x_test, y_test = train_model(df)
accuracy = evaluate_model(model, x_test, y_test)

print("model loaded successfully!")
model, encoders = load_model()
home_team = input("home team:").capitalize()
away_team = input("away team:").capitalize()
tournament = input("tournament:").capitalize()
city = input("city:").capitalize()
country = input("country").capitalize()
neutral = input("neutral(True/False):").capitalize()
predicition = predict_match(
    model,
    encoders,
    home_team,
    away_team,
    tournament,
    city,
    country,
    neutral
)
print("prediction:", predicition)
