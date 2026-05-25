from pypdf import PdfReader
from groq import Groq

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def screen_resume(job_description, resume_text, candidate_name, groq_api_key):
    client = Groq(api_key=groq_api_key)
    
    prompt = f"""You are an expert HR recruiter. Analyze this resume against the job description.

Job Description:
{job_description}

Resume ({candidate_name}):
{resume_text}

Respond in this exact format:
SCORE: [0-100]
STRENGTHS: [2-3 key strengths]
WEAKNESSES: [2-3 key weaknesses]
VERDICT: [Shortlist/Maybe/Reject]
SUMMARY: [2 sentence summary]"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content