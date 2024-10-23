from datetime import datetime

import requests

GENDER = "female"
WEIGHT_LBS = 120
HEIGHT_INCH = 62
AGE = 17

APP_ID = "f4d16408"
APP_KEY = "cf3d3aac0cf269665d0b4e52f9507891"

USERNAME = "amelia"
PASSWORD = "amelia"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/848b11e05a8c0afa47d0755c0c2c486f/copyOfMyWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,

}

data_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight": WEIGHT_LBS,
    "height": HEIGHT_INCH,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=data_params, headers=header)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth={
            USERNAME,
            PASSWORD,
        }
    )

    print(sheet_response.text)