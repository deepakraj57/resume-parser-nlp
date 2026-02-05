import spacy
import subprocess
import sys

# ---------- ENSURE SPACY MODEL EXISTS (FOR STREAMLIT CLOUD) ----------
try:
    spacy.load("en_core_web_sm")
except OSError:
    subprocess.check_call(
        [sys.executable, "-m", "spacy", "download", "en_core_web_sm"]
    )

import streamlit as st
import json
from parse_resume import parse_resume

st.title("Resume Parser")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF/DOCX)",
    type=["pdf", "docx"]
)

if uploaded_file:
    file_extension = uploaded_file.name.split('.')[-1]
    temp_file_path = f"uploaded_resume.{file_extension}"

    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # ---------- ERROR HANDLING ----------
    try:
        parsed_data = parse_resume(temp_file_path)
    except Exception:
        st.error("Failed to parse resume. Please upload a valid PDF or DOCX file.")
        st.stop()

    # ---------- UI LAYOUT ----------
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📇 Contact Info")
        st.write(f"**Name:** {', '.join(parsed_data['name']) if parsed_data['name'] else 'Not found'}")
        st.write(f"**Email:** {parsed_data['email'] or 'Not found'}")
        st.write(f"**Phone:** {parsed_data['phone'] or 'Not found'}")

    with col2:
        st.subheader("💼 Professional Info")
        st.write(f"**Years of Experience:** {parsed_data['experience_years'] or 'Not found'}")
        st.write(
            f"**Job Titles:** {', '.join(parsed_data['job_titles'])}"
            if parsed_data['job_titles'] else "**Job Titles:** Not found"
        )

    # ---------- SKILLS ----------
    st.divider()
    st.subheader("🛠 Skills")
    if parsed_data["skills"]:
        st.write(", ".join(parsed_data["skills"]))
    else:
        st.write("Not found")

    # ---------- EDUCATION ----------
    st.subheader("🎓 Education")
    if parsed_data["education"]:
        st.write(", ".join(parsed_data["education"]))
    else:
        st.write("Not found")

    # ---------- EXPORT ----------
    st.divider()
    st.download_button(
        label="⬇️ Download Parsed Data (JSON)",
        data=json.dumps(parsed_data, indent=2),
        file_name="parsed_resume.json",
        mime="application/json"
    )
