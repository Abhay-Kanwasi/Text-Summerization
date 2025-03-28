import os
import requests
from dotenv import load_dotenv

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

# Replace with your Hugging Face API token
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
HUGGINGFACE_INFERENCE_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from the React frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

class TextRequest(BaseModel):
    text: str

@app.post("/summarize/")
async def summarize(request: TextRequest):
    try:
        # Ensure the input text is not empty
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Input text cannot be empty.")

        # Prepare headers and payload for the Hugging Face API
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

        # Send a POST request to the Hugging Face API
        response = requests.post(HUGGINGFACE_INFERENCE_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the response
        summary = response.json()[0]['summary_text']
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)