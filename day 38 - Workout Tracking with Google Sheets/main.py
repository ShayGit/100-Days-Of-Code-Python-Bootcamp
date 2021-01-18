import requests
from datetime import datetime
import os

SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
BASE_URL = os.environ["BASE_URL"]
SHEETY_URL = os.environ["SHEETY_URL"]
GENDER = "male"
WEIGHT_KG = "60"
HEIGHT_CM = "167"
AGE = "22"

auth_data = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

exercise = input("Tell me which exercise you did:")
query_data = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=f"{BASE_URL}/natural/exercise", json=query_data, headers=auth_data)
exercise_data = response.json()["exercises"]


date = datetime.now()
format_date = date.strftime("%d/%m/%Y")
format_time = date.strftime("%H:%M:%S")
headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
for exercise in exercise_data:
    workout = {
        "workout":{
            "date": format_date,
            "time": format_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    print(workout)
    response = requests.post(url=SHEETY_URL, json=workout,headers=headers)
    response.raise_for_status()
    print(response.json())
