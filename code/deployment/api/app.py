from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
class InputData(BaseModel):
    input_data: str

@app.post("/predict")
def predict(data: InputData):
    return {"prediction": f"{make_pred(model, data.input_data)}"}
