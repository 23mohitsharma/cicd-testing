from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_predict_api():
    payload = {
        "person_age": 30,
        "person_income": 300000,
        "person_home_ownership": "RENT",
        "person_emp_length": 5,
        "loan_intent": "EDUCATION",
        "loan_grade": "B",
        "loan_amnt": 10000,
        "loan_int_rate": 12.5,
        "loan_percent_income": 0.15,
        "cb_person_default_on_file": "N",
        "cb_person_cred_hist_length": 8
    }

    response = client.post("/predict",json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "loan_default_probability" in data
    assert "loan_status" in data

    assert 0.0 <=data['loan_default_probability'] <= 1.0
    assert data['loan_status'] in [0,1]