from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load('attrition_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        data = scaler.transform([data])
        prediction = model.predict(data)[0]

        result = "Leave" if prediction == 1 else "Stay"
        return render_template('index.html', prediction_text=f'Prediction: Employee will likely {result}')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
