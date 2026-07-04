from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib


def train_model(df):

    x = df[["home_team", "away_team", "tournament",
           "city", "country", "neutral",]]

    y = df["result"]

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()

    model.fit(x_train, y_train)
    joblib.dump(model, "models/fifa_model.pkl")
    return model, x_test, y_test
