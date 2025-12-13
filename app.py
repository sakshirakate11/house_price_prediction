from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict-page")
def predict_page():
    return render_template("predict.html")

@app.route("/predict", methods=["POST"])
def predict():
    area = float(request.form["area"])
    bedrooms = int(request.form["bedrooms"])
    bathrooms = int(request.form["bathrooms"])
    parking = int(request.form["parking"])

    features = np.array([[area, bedrooms, bathrooms, parking]])
    price = model.predict(features)[0]

    return render_template("predict.html", result=f"Predicted Price: ₹{round(price,2)}")

if __name__ == "__main__":
    app.run(debug=True)
