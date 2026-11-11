# Stress Level Analyzer

A small Flask web app that asks 10 lifestyle questions and shows an estimated **stress level**: Low, Moderate or High, with a short message.

## What it does

The user answers 10 questions — sleep duration, work hours, screen time, exercise, caffeine intake, mood, headaches, deadline pressure, social interaction and major life events. Each answer carries a fixed point value. The points are added up into a score out of 100, and the score is mapped to a stress level:

| Score | Level |
|---|---|
| 0 – 29 | Low |
| 30 – 59 | Moderate |
| 60 – 100 | High |

## Important: this is not machine learning

There is no dataset, no trained model and no prediction. The score is a **rule-based questionnaire**, similar in spirit to a self-assessment form. The point values were chosen by hand and are not clinically validated. It is a demonstration of a web application, not a medical or psychological tool.

## Tech stack

- Python
- Flask
- HTML/CSS (Jinja2 templates)

## Project structure

```
stressproject/
├── app.py                  # Flask app: routes and scoring logic
├── templates/
│   ├── index.html          # Questionnaire form
│   └── result.html         # Result page
├── requirements.txt
└── .gitignore
```

## Run it

```bash
# 1. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the app
python app.py
```

Then open <http://localhost:5000> (or the address printed in the terminal).

## Limitations

- Not a trained model — no learning, no data, no accuracy figure
- Point values are arbitrary and not clinically validated
- `debug=True` is left on, so this is for local development only, not deployment
- No input validation beyond the HTML form, no tests, no database
- Not a medical tool — do not use it to diagnose anything

## Possible improvements

- Train a real model on a public stress dataset
- Calibrate the weights against a validated questionnaire such as the Perceived Stress Scale
- Move the point values into a config file
- Add server-side validation and tests
- Turn off debug mode and deploy behind a proper WSGI server
