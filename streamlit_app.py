import streamlit as st
import requests

st.set_page_config(page_title="AI CV Screener", page_icon="📄")
st.title("🤖 AI Resume Screener")
st.markdown("Upload a Job Description and multiple resumes — AI will rank candidates instantly!")

st.divider()

api_key = st.text_input("Enter your Groq API Key", type="password")

job_description = st.text_area("Paste Job Description here", height=200, placeholder="e.g. We are looking for a Python developer with 2+ years experience in FastAPI, machine learning...")

uploaded_resumes = st.file_uploader("Upload Resumes (PDF)", type="pdf", accept_multiple_files=True)

if st.button("🔍 Screen Resumes"):
    if not api_key:
        st.error("Please enter your Groq API key!")
    elif not job_description:
        st.error("Please paste a job description!")
    elif not uploaded_resumes:
        st.error("Please upload at least one resume!")
    else:
        with st.spinner("AI is screening resumes... please wait"):
            files = [("resumes", (r.name, r.read(), "application/pdf")) for r in uploaded_resumes]
            data = {"job_description": job_description, "api_key": api_key}
            
            try:
                response = requests.post("http://localhost:8000/screen", files=files, data=data)
                
                if response.status_code == 200:
                    results = response.json()["results"]
                    
                    st.success(f"✅ Screened {len(results)} candidates!")
                    st.divider()
                    
                    for i, result in enumerate(results):
                        score = result["score"]
                        
                        if score >= 70:
                            color = "🟢"
                        elif score >= 50:
                            color = "🟡"
                        else:
                            color = "🔴"
                        
                        with st.expander(f"{color} #{i+1} {result['candidate']} — Score: {score}/100"):
                            st.markdown(result["analysis"])
                else:
                    st.error("Something went wrong!")
            except Exception as e:
                st.error(f"Error: {str(e)}")