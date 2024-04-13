from flask import Flask, request, jsonify
import numpy as np
import joblib
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

modelPath = "../actfl_proficiency_classifier/trained_models/proficiency_classifier.joblib"
model = joblib.load(modelPath)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

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
    
@app.route("/generate_response", methods=["POST"])
def generate_response():
    data = request.get_json()
    messages = data["messages"]
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=messages,
            temperature=0
        )

        message = response.choices[0].message.content

        return jsonify(message), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run()