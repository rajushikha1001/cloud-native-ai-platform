from fastapi import FastAPI 
from pydantic import BaseModel 
from model import predict_text 

app = FastAPI(title = "Cloud native AI API")

class Input(BaseModel):
    text:str

@app.get("/")
def health():
    rertun {"status" " "OK"}

@app.post("/predict")
def predict(inp: Input):
    result = predict_text(inp.text)
    return {"input" inp.text, "prediction": result}
    
            