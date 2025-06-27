# Employee Attrition Prediction System

Employee attrition happens when an employee leaves an organization for any reason and is not replaced for a long time
This is a machine learning project where I built a simple web app to predict whether an employee is likely to leave their job, based on various input features. The project was created to learn and apply concepts like preprocessing, model training, and deploying a model using Flask.

# Dataset
This project uses the IBM HR Analytics Employee Attrition & Performance Dataset from Kaggle.

Rows: 1,470 employees
Columns: 35 features (both categorical and numerical)
Target variable: Attrition (Yes/No)

---

# Feature Selection
To keep the model simple and lightweight for the web app, I selected 7 high-importance features:

Age
DistanceFromHome
YearsSinceLastPromotion
NumCompaniesWorked
OverTime (converted to OverTime_Yes)
BusinessTravel (converted to BusinessTravel_Travel_Frequently)
JobRole (focused on Laboratory Technician role)

---

## 💼 Use Case

This tool can assist HR teams in identifying potential employee churn and taking proactive retention measures.

---

## 🛠️ Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas / NumPy
- Bootstrap 5 (for the UI)

---

## ⚙️ Setup Instructions

1. Clone the Repository
   ```bash
   git clone https://github.com/dhruvPrajapati13/Employee-Attrition-Prediction.git

2. Create Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Start the Flask App
python app.py

5. Open in Browser
http://127.0.0.1:5000/

