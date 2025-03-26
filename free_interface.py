import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}


def summarize(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]['summary_text']


if __name__ == "__main__":
    print(summarize(
        "The roadmap is designed specifically for someone with your background (Python, React, web frameworks).It provides a structured learning path from beginner to intermediate AI project development. Key focus areas: Learning essential ML/AI libraries Practical project implementations API integration with Hugging Face and Groq Full-stack AI application development"))  # Test summarization
