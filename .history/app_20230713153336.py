"""
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def extract_numeric_values(text):
    # Extract numeric values using regular expressions
    numeric_values = re.findall(r'\b\d+(?:\.\d+)?\b', text)

    # Retrieve the values at positions 7, 8, and 9
    extracted_values = numeric_values[7:11]

    # Return the extracted values
    return extracted_values

@app.route('/extract-values', methods=['POST'])
def extract_values():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'})

    text = data['text']
    extracted_values = extract_numeric_values(text)

    response = {
        "Total": extracted_values[0],
        "Ht": extracted_values[1],
        "Base Ht": extracted_values[2],
        "Tva": extracted_values[3]
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()
"""
from flask import Flask, request, jsonify
import joblib
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Load the model from the saved file
model = joblib.load('XML/XMLPRegressor_model.pkl')

# Load the fitted vocabulary from the vectorizer
vectorizer = CountVectorizer()
vectorizer.vocabulary_ = joblib.load('XML/vectorizer_vocabxml.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    input_data = request.get_json()
    
    # Extract the text from the input
    text = input_data['text']
    
    # Convert the text into numerical features using the fitted vectorizer
    text_vector = vectorizer.transform([text])
    
    # Make predictions
    prediction = model.predict(text_vector)
    
    # Reshape the prediction array to have shape (1, 4)
    prediction = prediction.reshape(1, -1)
    
    # Retrieve the predicted values
    total = prediction[0][0]
    ht = prediction[0][1]
    base_ht = prediction[0][2]
    tva = prediction[0][3]
    
    # Create a response dictionary
    response = {
        "total": total,
        "ht": ht,
        "base_ht": base_ht,
        "tva": tva
    }
    
    # Return the response as JSON
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)