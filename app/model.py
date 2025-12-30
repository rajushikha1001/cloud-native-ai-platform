from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def predict_text(text: str):
    result = classifier(text)[0]
    return {
        "label": result["label"],
        "score": round(result["score"], 3)
    }
