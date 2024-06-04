from fastapi import FastAPI

import pickle

app = FastAPI()

@app.get("/")
def predict_menstruation(length_of_cycle: int, length_of_period: int, age_at_menarche: int, height: int, weight: int, bmi: float):
    with open('mestruation_prediction', 'rb') as file:
        mp = pickle.load(file)
        prediction = mp.predict([[length_of_cycle, length_of_period, age_at_menarche, height, weight, bmi]])
        return {"prediction": prediction[0]}

