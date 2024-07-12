import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load the data
data = pd.read_csv("onlinefraud.csv")

# Convert categorical columns to numeric
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data['type'] = le.fit_transform(data['type'])

# Define the feature matrix 'X' and target vector 'y'
X = data[["type", "amount", "oldbalanceOrg", "newbalanceOrig"]]
y = data["isFraud"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Save the model to disk
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

print("Model saved as model.pkl")
