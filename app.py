from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define the transaction type mapping
type_mapping = {'CASH_IN': 0, 'CASH_OUT': 1, 'DEBIT': 2, 'PAYMENT': 3, 'TRANSFER': 4}

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        transaction_type = request.form.get('transaction_type')
        amount = float(request.form.get('amount'))
        oldbalanceOrg = float(request.form.get('oldbalanceOrg'))
        newbalanceOrig = float(request.form.get('newbalanceOrig'))

        # Convert transaction_type to numeric
        if transaction_type not in type_mapping:
            raise ValueError("Invalid transaction type")

        transaction_type_numeric = type_mapping[transaction_type]

        # Prepare features for prediction
        features = np.array([[transaction_type_numeric, amount, oldbalanceOrg, newbalanceOrig]])
        
        # Predict fraud
        prediction = model.predict(features)

        # Determine result
        result = "Fraudulent" if prediction[0] == 1 else "Not Fraudulent"

    except ValueError as e:
        # Handle value errors
        result = f"Error: {str(e)}"
    except Exception as e:
        # Handle other exceptions
        result = f"An unexpected error occurred: {str(e)}"

    # Render result
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
