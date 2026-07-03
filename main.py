# import pandas as pd

# print("here is the code for understnding the data")

# df = pd.read_csv('data/results.csv')    #path of the code
# print(df.shape)                          #prints the dataframe like (rows, columns)
# print()                                  # for space and readability
# print(df.columns)                         # displays or prints the colunms from the dataframe
# print()                                      # space for readability
# print(df.info())                         # prints the iformation about the dataframe like data types and non-null counts
# and returns none thats why often at the last
# print()   # readability
# print(df.isnull().sum()) # isnull() checks all cells in the dataframe and returns a boolean (ture or false ),
# .sum() counts the number of ture values in the dataframe and returns the count
# print("before dropping the null values:", df.shape)  # prints the shape of dataframe before cleaning data

# df = df.dropna()
# drops the null values from the dataframe and returns a with null value data farme

# print("after dropping the null values:", df.shape) # prints the shape after cleaning the dataframe#

# df.to_csv('data/results_cleaned.csv', index= False) # saves the cleaned dataframe to a new csv file
# index = false is used to avoid saving the index column number in the new data frame


# import pandas as pd
# reads the cleaned data from the csv file
# df = pd.read_csv('data/results_cleaned.csv')
# and stores in dataframe


# def get_result(row):                                                   # function to decide match result
#    if row["home_score"] > row["away_score"]:
#        return "Home win"
#    elif row["home_score"] < row["away_score"]:
#        return "Away win "
#        return "draw"


# df["result"] = df.apply(get_result, axis=1)   # this creates new column
# print(df[["home_team", "away_team", "home_score", "away_score", "result"]].head(
#    10))  # shows first 10 rows
# df.to_csv("data/final_dataset.csv", index=False)  # save updated dataset


import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# reads the data set and stores in the dataframe
df = pd.read_csv("data/final_dataset.csv")

# creates an object of the class LabeleEncoder and stores in the variable
encoder = LabelEncoder()
# encoder. this is only used for string data and not for numericals
#  it coverts string to integer data type since manchine learning models can only understands integers data

# converts "home_team " to some integer value
df["home_team"] = encoder.fit_transform(df["home_team"])
df["away_team"] = encoder.fit_transform(df["away_team"])
df["tournament"] = encoder.fit_transform(df["tournament"])
df["city"] = encoder.fit_transform(df["city"])
df["country"] = encoder.fit_transform(df["country"])
df["neutral"] = encoder.fit_transform(df["neutral"])
df["result"] = encoder.fit_transform(df["result"])

# here comes the actual machine learning part.

# features (x)
x = df[["home_team", "away_team", "tournament",
        "city", "country", "neutral", "result"]]

# Target (y)
y = df["result"]

# splitting the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42)  # 80% training and 20% testing

# creating the model
# creates an object of the class DecisionTreeclassifier and
model = DecisionTreeClassifier()
# stores in the varibale model

# train model
model.fit(x_train, y_train)

# make predicitions
predictions = model.predict(x_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)
