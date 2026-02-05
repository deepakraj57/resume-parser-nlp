# Resume Parser using NLP

An NLP-based resume parsing application that extracts key candidate information from PDF and DOCX resumes.

## Features
- Extracts Name, Email, Phone Number
- Identifies Skills, Education, Job Titles
- Calculates Years of Experience when available
- Supports PDF and DOCX formats
- Download parsed data as JSON

## Tech Stack
- Python
- spaCy
- pdfplumber
- python-docx
- Streamlit

## Accuracy (Tested on 10 resumes)
- Name: 100%
- Email: 100%
- Phone: 100% (Indian numbers)
- Skills: 80%
- Education: 100%
- Experience: 100% (when mentioned)

## Known Limitations
- Skill extraction is keyword-based and may miss synonyms
- Experience calculation depends on date formats
- Phone extraction currently supports Indian numbers only

## How to Run Locally
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
