import json
import logging
import os
import joblib
import pytest
from prediction_service.prediction import form_response, api_response
import prediction_service

input_data = {
    "incorrect_range": 
    {"Pregnancies": 7897897, 
    "Glucose": 555, 
    "BloodPressure": 99, 
    "SkinThickness": 99, 
    "Insulin": 12, 
    "BMI": 789, 
    "DiabetesPedigreeFunction": 75, 
    "Age": 2
    },

    "correct_range":
    {"Pregnancies": 16, 
    "Glucose": 150, 
    "BloodPressure": 120, 
    "SkinThickness": 42, 
    "Insulin": 120, 
    "BMI": 41, 
    "DiabetesPedigreeFunction": 1, 
    "Age": 30
    },

    "incorrect_col":
    {"Pregnancies": 16, 
    "Glucose": 150, 
    "BloodPressure": 120, 
    "SkinThickness": 42, 
    "Insulin": 120, 
    "BMI": 41, 
    "DiabetesPedigreeFunction": 1, 
    "Age": 30
    },
}

TARGET_range = {
    "min": 0.0,
    "max": 1.0
}

def test_form_response_correct_range(data=input_data["correct_range"]):
    res = form_response(data)
    assert  TARGET_range["min"] <= res <= TARGET_range["max"]

def test_api_response_correct_range(data=input_data["correct_range"]):
    res = api_response(data)
    assert  TARGET_range["min"] <= res["response"] <= TARGET_range["max"]

def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        res = form_response(data)

def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInRange().message

#def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
#    res = api_response(data)
#    assert res["response"] == prediction_service.prediction.NotInCols().message
