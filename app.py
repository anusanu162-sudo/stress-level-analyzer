from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    sleep = int(request.form["sleep"])
    work = int(request.form["work"])
    screen = int(request.form["screen"])
    exercise = int(request.form["exercise"])
    caffeine = int(request.form["caffeine"])
    mood = int(request.form["mood"])
    headache = int(request.form["headache"])
    deadline = int(request.form["deadline"])
    social = int(request.form["social"])
    life_event = int(request.form["life_event"])

    stress_score = sleep + work + screen + exercise + caffeine + mood + headache + deadline + social + life_event

    percentage = min(stress_score, 100)

    if percentage < 30:
        level = "Low"
        emoji = "😌"
        color = "#4CAF50"
        quote = "You are doing great. Keep balancing work and rest."
    elif percentage < 60:
        level = "Moderate"
        emoji = "🙂"
        color = "#ff9800"
        quote = "Take small breaks. You deserve mental peace."
    else:
        level = "High"
        emoji = "😟"
        color = "#f44336"
        quote = "Pause. Breathe. You are stronger than this moment."

    return render_template("result.html", percentage=percentage, level=level, emoji=emoji, color=color, quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
