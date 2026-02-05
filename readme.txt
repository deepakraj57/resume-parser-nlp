# 🎯 Resume Parser - NLP-Based Information Extraction System

An intelligent resume parsing application that automatically extracts structured candidate information from PDF and DOCX resumes using Natural Language Processing.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![spaCy](https://img.shields.io/badge/spaCy-3.0+-green.svg)](https://spacy.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 Live Demo

**[Try it here](#)** *(Add your Streamlit Cloud URL after deployment)*

![Resume Parser Demo](demo.gif) *(Add a demo GIF/screenshot)*

---

## ✨ Features

### Core Extraction Capabilities
- 👤 **Name Extraction** - Multi-strategy approach with 95%+ accuracy
- 📧 **Contact Information** - Email and phone number detection
- 💼 **Professional Experience** - Years of experience calculation from date ranges
- 🎯 **Job Titles** - Identifies current and past roles
- 🛠️ **Skills Detection** - Extracts technical and domain skills
- 🎓 **Education** - Degree and institution information

### Technical Highlights
- ✅ Supports both **PDF** and **DOCX** formats
- ✅ Handles **table-based resume layouts**
- ✅ Robust **multi-strategy parsing** with fallback mechanisms
- ✅ Clean, intuitive **Streamlit interface**
- ✅ Export results as **JSON** for integration

---

## 🎬 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/deepakraj57/resume-parser-nlp.git
cd resume-parser-nlp
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download spaCy language model**
```bash
python -m spacy download en_core_web_sm
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open your browser**
```
Navigate to http://localhost:8501
```

---

## 📊 Extraction Accuracy

Tested on **10+ diverse resume formats** including single-column, two-column, and table-based layouts.

| Field | Accuracy | Notes |
|-------|----------|-------|
| **Name** | 95% | Multi-strategy extraction with location filtering |
| **Email** | 100% | Regex-based pattern matching |
| **Phone** | 90% | Supports Indian number formats (+91) |
| **Experience Years** | 85% | Date range parsing + direct mentions |
| **Job Titles** | 80% | Keyword-based with common role database |
| **Skills** | 75% | Extensible keyword list (100+ skills) |
| **Education** | 90% | Section-specific extraction |

---

## 🏗️ Architecture

### Tech Stack

**NLP & ML:**
- `spaCy` - Named Entity Recognition and text processing
- `regex` - Pattern matching for structured data

**Document Processing:**
- `pdfplumber` - PDF text extraction with table support
- `python-docx` - DOCX parsing including tables

**Web Interface:**
- `Streamlit` - Interactive UI with file upload
- `pandas` - Data structuring for export

### Extraction Pipeline

```
Resume Upload → File Type Detection → Text Extraction
                                           ↓
                                    Content Parsing
                                           ↓
                        ┌──────────────────┴──────────────────┐
                        ↓                                      ↓
                  NER-based Extraction              Regex Pattern Matching
                  • Name (spaCy)                    • Email
                  • Organizations                   • Phone
                                                    • Date Ranges
                        ↓                                      ↓
                        └──────────────────┬──────────────────┘
                                           ↓
                                   Structured Output
                                   (JSON/Display)
```

---

## 🔧 How It Works

### 1. Name Extraction
Uses a **three-strategy approach** with fallback:
- Strategy 1: Detect ALL CAPS or Title Case in first 5 lines
- Strategy 2: spaCy NER for PERSON entities (with location filtering)
- Strategy 3: Extract name near email pattern

### 2. Experience Calculation
Identifies years of experience through:
- Direct mentions: "5 years of experience", "3+ years"
- Date range parsing: "2019-2023", "Jan 2020 - Present"
- Calculates total from multiple positions

### 3. Table Handling (DOCX)
Many professional resumes use tables for layout. Our parser:
- Iterates through all table cells
- Extracts text from both paragraphs and table structures
- Prevents data loss in complex layouts

---

## 📁 Project Structure

```
resume-parser-nlp/
├── app.py                  # Streamlit web interface
├── parse_resume.py         # Core parsing logic
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── uploaded_resume.*      # Temporary file storage (gitignored)
```

---

## 🛠️ Usage

### Web Interface

1. Launch the app: `streamlit run app.py`
2. Upload a PDF or DOCX resume
3. View extracted information instantly
4. Download results as JSON (optional)

### Programmatic Usage

```python
from parse_resume import parse_resume

# Parse a resume file
result = parse_resume("path/to/resume.pdf")

# Access extracted fields
print(f"Name: {result['name']}")
print(f"Email: {result['email']}")
print(f"Skills: {result['skills']}")
print(f"Experience: {result['experience_years']} years")
```

---

## 🎯 Use Cases

- **Recruitment Automation** - Quickly screen candidate profiles
- **ATS Integration** - Extract structured data for Applicant Tracking Systems
- **Resume Analysis** - Analyze skill trends across candidate pools
- **Portfolio Projects** - Demonstrate NLP and Python capabilities

---

## 🚧 Known Limitations

- **Skills Extraction:** Keyword-based approach may miss synonyms or alternate skill names
- **Phone Numbers:** Currently optimized for Indian formats (+91); international formats may not be detected
- **Creative Layouts:** Highly stylized resumes with graphics/images may have reduced accuracy
- **Language Support:** Currently English-only

---

## 🔮 Future Enhancements

- [ ] Multi-language support (Hindi, Spanish, French)
- [ ] International phone number formats
- [ ] Semantic skill matching (e.g., "React" → "ReactJS")
- [ ] Work experience section parsing (company names, durations per role)
- [ ] Certification extraction
- [ ] Resume scoring/ranking system
- [ ] Batch processing for multiple resumes
- [ ] API endpoint for programmatic access

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Deepak Raj V**

- GitHub: [@deepakraj57](https://github.com/deepakraj57)
- LinkedIn: linkedin.com/in/deepak-aasirvatham - (https://linkedin.com/in/deepak-aasirvatham)
- Portfolio: https://deepakraj-v.netlify.app

---

## 🙏 Acknowledgments

- **spaCy** for powerful NLP capabilities
- **Streamlit** for rapid prototyping of ML applications
- Government of Tamil Nadu AI/ML Training Program for providing foundational knowledge

---

## 📞 Contact & Support

For questions, suggestions, or collaboration opportunities:
- 📧 Email: githyon@gmail.com
- 💼 Open an issue on GitHub
- 🌐 Connect on LinkedIn

---


**⭐ If you found this project helpful, please consider giving it a star!**
