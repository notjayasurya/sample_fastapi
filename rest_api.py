import uvicorn
from fastapi import FastAPI
import joblib , os 
import pickle
import numpy as np

#models

student_model = open('models/api_pickle.pkl','rb')
student_api = pickle.load(student_model)

# init the app
app = FastAPI(debug = True)

#Routes
@app.get('/')
async def index():
    return{'text':'vanakkam'}

@app.get('/items/{name}')
async def get_items(name):
    return{'name':name}

# ML Screen:


@app.get('/predict')
async def student_pred():
    X = [[5,9,3,5,7]]
    prediction = student_api.predict(X)
    str_val = str(prediction)
    return {"predicted_value":str_val}

    


if __name__ == '__main__':
    uvicorn.run(app,host = "127.0.0.1",port = 8000)