from fastapi import FastAPI, UploadFile, File, Form
from app.screener import extract_text_from_pdf, screen_resume
from typing import List
import shutil
import os
import json

app = FastAPI()

@app.post("/screen")
async def screen_resumes(
    job_description: str = Form(...),
    api_key: str = Form(...),
    resumes: List[UploadFile] = File(...)
):
    results = []
    
    for resume in resumes:
        temp_path = f"temp_{resume.filename}"
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)
        
        resume_text = extract_text_from_pdf(temp_path)
        os.remove(temp_path)
        
        candidate_name = resume.filename.replace(".pdf", "").replace("_", " ")
        
        result = screen_resume(job_description, resume_text, candidate_name, api_key)
        
        score = 0
        for line in result.split("\n"):
            if line.startswith("SCORE:"):
                try:
                    score = int(line.replace("SCORE:", "").strip())
                except:
                    score = 0
        
        results.append({
            "candidate": candidate_name,
            "score": score,
            "analysis": result
        })
    
    results.sort(key=lambda x: x["score"], reverse=True)
    return {"results": results}