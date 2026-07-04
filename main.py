from src.preprocess import preprocess_data
from src.train import train_model

from src.evaluate import evaluate_model

df = preprocess_data()
model, x_test, y_test = train_model(df)
accuracy = evaluate_model(model, x_test, y_test)

print("model loaded successfully!")
