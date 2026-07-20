from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model/cricket_score_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    batting = request.form["batting"]

    bowling = request.form["bowling"]

    current_score = int(request.form["score"])

    overs = float(request.form["overs"])

    wickets = int(request.form["wickets"])

    last5 = int(request.form["last5"])

    wickets5 = int(request.form["wickets5"])

    prediction = model.predict([[
        batting,
        bowling,
        current_score,
        overs,
        wickets,
        last5,
        wickets5
    ]])

    final_score = round(prediction[0])

    return render_template(
        "index.html",
        prediction=final_score
    )

if __name__ == "__main__":
    app.run(debug=True)