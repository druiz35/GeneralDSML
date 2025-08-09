import request
from flask import Blueprint, current_app, jsonify


def model_predict():
    # Extract input data from request
    input_data = request.json.get('input_data')
    
    # Preprocess the input data
    processed_data = current_app.ml_service.preprocess_data(input_data)
    
    # Make prediction using the MLService instance
    prediction = current_app.ml_service.predict(processed_data)
    
    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction.tolist()})  # Convert numpy array to list if necessary