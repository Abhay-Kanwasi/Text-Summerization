# Text Summarizer

This is a simple text summarization application built using FastAPI for the backend and React for the frontend. It uses Hugging Face's `facebook/bart-large-cnn` model to generate text summaries.

## Features
- Summarizes input text using an AI model
- Simple and user-friendly UI
- Copy and save summarized text

## Technologies Used
- **Backend**: FastAPI, Pydantic, Hugging Face API
- **Frontend**: React, Axios

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Node.js & npm

## Setup Instructions

### Backend Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/text-summarizer.git
   cd text-summarizer
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your Hugging Face API token:
   ```sh
   HUGGINGFACE_API_TOKEN=your_token_here
   ```
5. Run the FastAPI server:
   ```sh
   uvicorn main:app --reload
   ```

### Frontend Setup
1. Navigate to the `frontend` directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the React app:
   ```sh
   npm start
   ```

## Usage
1. Open the React app in your browser (`http://localhost:3000`).
2. Enter text in the input box and click "Summarize".
3. View the summarized text and copy or save it if needed.

## API Endpoints
- **POST /summarize/**: Accepts a JSON request with a `text` field and returns the summarized text.

## License
This project is open-source and available under the MIT License.

