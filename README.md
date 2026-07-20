# 🏏 Cricket Score Predictor

A Machine Learning web application that predicts the projected final score of a cricket team in a T20 match based on the current match situation. The application is built using **Python**, **Flask**, **Scikit-learn**, and **Pandas**, and is deployed on Render.

## 🌐 Live Demo

**Live Application:** https://cricket-score-predictor-2.onrender.com

---

## 📌 Project Overview

This project predicts the expected final innings score using a trained Machine Learning model.

The prediction is based on important match features such as:

- Batting Team
- Bowling Team
- Current Score
- Overs Completed
- Wickets Lost
- Runs Scored in Last 5 Overs
- Wickets Lost in Last 5 Overs

The application provides an estimated final score instantly after the user enters the current match details.

---

## 🚀 Features

- Predicts projected final cricket score
- User-friendly web interface
- Machine Learning based prediction
- Real-time prediction
- Responsive design
- Free cloud deployment using Render

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Data Preprocessing
5. Model Training
6. Model Evaluation
7. Model Saving
8. Flask Web Application
9. Cloud Deployment

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Pandas
- NumPy

### Backend

- Flask

### Deployment

- Gunicorn
- Render

### Version Control

- Git
- GitHub

---

## 📂 Project Structure

```
Cricket-Score-Predictor/
│
├── app.py
├── train_model.py
├── requirements.txt
├── runtime.txt
├── Procfile
├── model/
│   └── cricket_score_model.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── dataset/
│   └── cricket_data.csv
│
└── README.md
```

---

## 📊 Input Features

| Feature | Description |
|----------|-------------|
| Batting Team | Team currently batting |
| Bowling Team | Team currently bowling |
| Current Score | Runs scored till now |
| Overs | Overs completed |
| Wickets | Wickets lost |
| Last 5 Runs | Runs scored in last 5 overs |
| Last 5 Wickets | Wickets lost in last 5 overs |

---

## 🎯 Output

The model predicts the projected final innings score.

Example:

```
Projected Score: 184 Runs
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Arpit-Pandey019/cricket-score-predictor.git
```

Move inside the project

```bash
cd cricket-score-predictor
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## 📦 Requirements

- Python 3.11+
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Gunicorn

---

## 📈 Future Improvements

- Live cricket API integration
- Match win probability prediction
- IPL-specific model
- ODI and Test score prediction
- Interactive charts and analytics
- Player performance prediction

---



---

## 👨‍💻 Author

**Arpit Kumar Pandey**

- GitHub: https://github.com/Arpit-Pandey019
- LinkedIn: *(Add your LinkedIn profile)*

---

## ⭐ If you found this project useful

Please consider giving the repository a **Star ⭐**.
