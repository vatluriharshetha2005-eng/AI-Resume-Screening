# AI-Based Resume Screening and Job Matching

An AI-powered web application built with Python and Streamlit to analyze resumes and match candidates with job descriptions using Natural Language Processing (NLP).

## Features

- Upload resumes in PDF, DOCX, or TXT format
- Enter a job description for candidate screening
- Extract skills from resumes
- Identify matching and missing skills
- Compare candidates against job requirements
- Download screening results as a CSV file

## Tech Stack

- Python
- Streamlit
- Natural Language Processing (NLP)
- Pandas
- Resume parsing and skill extraction

## Project Structure

```text
AI-Resume-Screening/
├── app.py
├── job_matcher.py
├── nlp_processing.py
├── resume_parser.py
├── skill_extractor.py
├── requirements.txt
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/vatluriharshetha2005-eng/AI-Resume-Screening.git
cd AI-Resume-Screening
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## How It Works

1. Enter the job description.
2. Upload one or more resumes.
3. Click **Screen Resumes**.
4. Review candidate matches and missing skills.
5. Download the results as a CSV file.

## Disclaimer

This is a student project intended to assist with resume screening. Results may be inaccurate and should not be used as the sole basis for hiring decisions. Protect candidate data and obtain appropriate permission before processing resumes.

## Author

**Harshe**

GitHub: [vatluriharshetha2005-eng](https://github.com/vatluriharshetha2005-eng)
