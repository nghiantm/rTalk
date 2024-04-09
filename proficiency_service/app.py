from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

modelPath = "../actfl_proficiency_classifier/trained_models/proficiency_classifier.joblib"
model = joblib.load(modelPath)

@app.route("/", methods=["GET"])
def home():
    return jsonify("WELCOME"), 200

@app.route("/predict_prof", methods=["POST"])
def predict_prof():
    try:
        # Get data from request as JSON
        data = request.get_json()
        userText = data["text"]

        prediction = model.predict(userText)
        # Convert to List to be able to jsonify
        predictionList = prediction.tolist() if isinstance(prediction, np.ndarray) else prediction


        response = {
            "prediction": predictionList
        }
        
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500