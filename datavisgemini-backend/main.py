import logging
from flask import Flask, request, jsonify, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.secret_key = 'your_secret_key'

logging.basicConfig(level=logging.INFO)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the file in session for temporary use
    session['file_data'] = file.read().decode('utf-8')  # Decode if text file

    # Add any initial processing here if needed

    return jsonify({"message": "File uploaded successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)

import pandas as pd
from io import BytesIO

@app.route('/clean', methods=['POST'])
def clean_data():
    file_data = session.get('file_data')
    if not file_data:
        return jsonify({"error": "No data available"}), 400
    
    # Load the data into a Pandas DataFrame
    df = pd.read_csv(BytesIO(file_data))

    # Perform data cleaning (example: drop missing values)
    df.dropna(inplace=True)

    # Store the cleaned data back into the session
    session['cleaned_data'] = df.to_csv(index=False)

    return jsonify({"message": "Data cleaned successfully"}), 200

import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

@app.route('/visualize', methods=['GET'])
def visualize_data():
    cleaned_data = session.get('cleaned_data')
    if not cleaned_data:
        return jsonify({"error": "No cleaned data available"}), 400
    
    # Load the cleaned data into a Pandas DataFrame
    df = pd.read_csv(BytesIO(cleaned_data.encode()))

    # Create a simple visualization (example: histogram)
    plt.figure(figsize=(10, 6))
    sns.histplot(df, kde=True)
    
    # Save the plot to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Convert plot to base64 to send over HTTP
    plot_base64 = base64.b64encode(buf.read()).decode('utf-8')

    return jsonify({"visualization": plot_base64}), 200

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

@app.route('/ml', methods=['POST'])
def run_ml_model():
    cleaned_data = session.get('cleaned_data')
    if not cleaned_data:
        return jsonify({"error": "No cleaned data available"}), 400
    
    # Load the cleaned data into a Pandas DataFrame
    df = pd.read_csv(BytesIO(cleaned_data.encode()))

    # Example: Simple linear regression
    X = df.drop('target_column', axis=1)  # Replace 'target_column' with your actual target column
    y = df['target_column']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    return jsonify({"mse": mse, "coefficients": model.coef_.tolist()}), 200
