# AI Resume Screener 🤖

An AI-powered resume screening tool that ranks candidates against a job description instantly.

🔗 **Live Demo:** [https://ai-cv-screener-hwcolmopszgdryrcovaq58.streamlit.app](https://ai-cv-screener-hwcolmopszgdryrcovaq58.streamlit.app)

## Features
- Upload multiple resumes (PDF) at once
- Paste any job description
- AI scores each candidate from 0-100
- Shows strengths, weaknesses and verdict for each candidate
- Color coded ranking (green/yellow/red)
- Powered by Groq LLM (free & fast)

## Tech Stack
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **LLM:** Groq (Llama 3.1)
- **PDF Processing:** PyPDF

## How to Run Locally

1. Clone the repo
2. Create a virtual environment and install dependencies:
```bash
pip install -r requirements.txt
```
3. Run FastAPI backend:
```bash
uvicorn app.main:app --reload
```
4. Run Streamlit frontend:
```bash
streamlit run streamlit_app.py
```
5. Open http://localhost:8501 and enter your Groq API key

## Demo
Upload a JD + multiple resumes → AI ranks candidates instantly!
