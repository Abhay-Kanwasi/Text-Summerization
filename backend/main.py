from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Existing imports and setup
import os
import requests
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi import HTTPException

load_dotenv()

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
HUGGINGFACE_INFERENCE_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from the React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str

@app.get("/")
async def main():
    return {"sucess": "successfully deploy"}

@app.post("/api/summarize/")
async def summarize(request: TextRequest):
    try:
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Input text cannot be empty.")

        headers = {
            "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}",
            "Content-Type": "application/json",
        }
        payload = {
            "inputs": request.text,
            "parameters": {
                "max_length": 150,
                "min_length": 30,
                "do_sample": False,
            },
        }

        response = requests.post(HUGGINGFACE_INFERENCE_URL, headers=headers, json=payload)
        response.raise_for_status()

        summary = response.json()[0]['summary_text']
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))