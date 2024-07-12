# online-payment-fraud-detector
Fraud Detection Tool for Bank Transactions

This project is a web-based application designed to identify fraudulent bank transactions using a machine learning model. Users can input transaction details such as transaction type, amount, old balance, and new balance to determine if a transaction is fraudulent. The application leverages a trained Decision Tree Classifier to make predictions and provides an intuitive user interface for ease of use.

Key features include:

User Input Form: Users can enter transaction details through a web form.
Real-time Prediction: The machine learning model predicts whether the transaction is fraudulent based on the input data.
Result Display: The prediction result is displayed on a separate page, indicating if the transaction is fraudulent or not.
Model Accuracy: The application provides the accuracy of the model for user awareness.
The application is built using Flask for the backend, with HTML and CSS for the front-end interface.

Here, we are using a Decision Tree Classifier, a type of machine learning model, to predict whether a transaction is fraudulent based on features such as transaction_type, amount, oldbalanceOrg, and newbalanceOrig. Here’s a detailed explanation of the model and how it is applied to the given features:

Decision Tree Classifier
A Decision Tree Classifier is a supervised learning algorithm used for classification tasks. It works by splitting the data into subsets based on the value of input features, creating a tree-like structure where each node represents a feature and each branch represents a decision rule. The leaves of the tree represent the final class labels (e.g., fraudulent or not fraudulent).

Steps Involved in Training and Using the Model
Data Preprocessing:

Label Encoding: Convert the categorical feature transaction_type (e.g., CASH_IN, CASH_OUT) into numerical values using LabelEncoder. This is necessary because machine learning models work with numerical data.
Feature Matrix and Target Vector: Define the feature matrix X (which includes transaction_type, amount, oldbalanceOrg, and newbalanceOrig) and the target vector y (which is isFraud).
Training the Model:

Train-Test Split: Split the data into training and testing sets to evaluate the model's performance.
Model Training: Fit the Decision Tree Classifier to the training data (X_train, y_train).
Making Predictions:

Feature Input: Take user input for transaction_type, amount, oldbalanceOrg, and newbalanceOrig and convert them into a numerical feature array.
Model Prediction: Use the trained model to predict whether the transaction is fraudulent based on the input features.
Applying the Model to Transaction Types
Here’s how the model applies to different transaction types and other features:

Label Encoding Transaction Types:

Convert categorical transaction types (e.g., CASH_IN, CASH_OUT, DEBIT, PAYMENT, TRANSFER) into numerical values. For example:
CASH_IN -> 0
CASH_OUT -> 1
DEBIT -> 2
PAYMENT -> 3
TRANSFER -> 4
Feature Vector Creation:

Create a feature vector using the numerical value of transaction_type and other features (amount, oldbalanceOrg, newbalanceOrig).
Model Prediction:

Use the feature vector to predict the probability of the transaction being fraudulent. The Decision Tree model will traverse the tree based on the feature values and arrive at a leaf node representing the predicted class (fraudulent or not fraudulent).
Example Workflow
User Input:

transaction_type: CASH_IN
amount: 1000.0
oldbalanceOrg: 5000.0
newbalanceOrig: 6000.0
Label Encoding:

CASH_IN -> 0
Feature Vector:

[0, 1000.0, 5000.0, 6000.0]
Model Prediction:

The model uses the feature vector to predict whether the transaction is fraudulent.
