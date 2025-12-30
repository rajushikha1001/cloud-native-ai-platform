from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_text

app = FastAPI(title="Cloud Native AI API")

class Input(BaseModel):
    text: str

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(inp: Input):
    result = predict_text(inp.text)
    return {"input": inp.text, "prediction": result}
