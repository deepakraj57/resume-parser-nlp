import streamlit as st
import json
from parse_resume import parse_resume

st.set_page_config(page_title="Resume Parser", layout="centered")

st.title("📄 Resume Parser")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1].lower()
    temp_file_path = f"/tmp/uploaded_resume.{file_extension}"

    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    try:
        parsed_data = parse_resume(temp_file_path)
    except Exception as e:
        st.error("❌ Failed to parse resume. Please upload a valid file.")
        st.stop()

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📇 Contact Info")
        st.write(f"**Name:** {', '.join(parsed_data['name']) if parsed_data['name'] else 'Not found'}")
        st.write(f"**Email:** {parsed_data['email'] or 'Not found'}")
        st.write(f"**Phone:** {parsed_data['phone'] or 'Not found'}")

    with col2:
        st.subheader("💼 Professional Info")
        st.write(f"**Experience (Years):** {parsed_data['experience_years'] or 'Not found'}")
        st.write(
            f"**Job Titles:** {', '.join(parsed_data['job_titles'])}"
            if parsed_data['job_titles'] else "**Job Titles:** Not found"
        )

    st.divider()

    st.subheader("🛠 Skills")
    st.write(", ".join(parsed_data["skills"]) if parsed_data["skills"] else "Not found")

    st.subheader("🎓 Education")
    st.write(", ".join(parsed_data["education"]) if parsed_data["education"] else "Not found")

    st.divider()

    st.download_button(
        "⬇️ Download Parsed Data (JSON)",
        data=json.dumps(parsed_data, indent=2),
        file_name="parsed_resume.json",
        mime="application/json"
    )
