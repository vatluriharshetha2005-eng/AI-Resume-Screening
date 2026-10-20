import streamlit as st
import pandas as pd

from resume_parser import extract_text
from job_matcher import match_resume


st.set_page_config(
    page_title="AI Resume Screening",
    page_icon="📄",
    layout="wide"
)

st.title("AI-Based Resume Screening and Job Matching")
st.subheader("Using Natural Language Processing (NLP)")

st.write(
    "Upload resumes and compare them with a job description "
    "to identify matching and missing skills."
)

st.info(
    "This is a student project. Results are only screening aids "
    "and should not be used as the sole basis for hiring decisions."
)

job_description = st.text_area(
    "Enter the Job Description",
    placeholder=(
        "Example: We need a Data Analyst with Python, SQL, "
        "Excel, Pandas, NumPy and Power BI skills."
    ),
    height=150
)

uploaded_files = st.file_uploader(
    "Upload Resumes (PDF, DOCX or TXT)",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if st.button("Screen Resumes", type="primary"):

    if not job_description.strip():
        st.warning("Please enter a job description.")

    elif not uploaded_files:
        st.warning("Please upload at least one resume.")

    else:
        results = []

        for file in uploaded_files:
            try:
                resume_text = extract_text(
                    file.getvalue(),
                    file.name
                )

                if not resume_text.strip():
                    st.warning(
                        f"No readable text found in {file.name}."
                    )
                    continue

                result = match_resume(
                    file.name,
                    resume_text,
                    job_description
                )

                results.append(result)

            except Exception as error:
                st.error(
                    f"Could not process {file.name}: {error}"
                )

        if results:
            df = pd.DataFrame(results)

            df = df.sort_values(
                by=[
                    "Skill Coverage (%)",
                    "Text Similarity (%)"
                ],
                ascending=False
            )

            st.header("Resume Screening Results")

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

            st.subheader("Detailed Resume Analysis")

            for result in results:
                with st.expander(result["Resume"]):

                    st.write(
                        "**Skill Coverage:**",
                        f'{result["Skill Coverage (%)"]}%'
                    )

                    st.write(
                        "**Text Similarity:**",
                        f'{result["Text Similarity (%)"]}%'
                    )

                    st.write(
                        "**Matched Skills:**",
                        result["Matched Skills"] or "None detected"
                    )

                    st.write(
                        "**Missing Skills:**",
                        result["Missing Skills"] or "None detected"
                    )

            csv_data = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="Download Results as CSV",
                data=csv_data,
                file_name="resume_screening_results.csv",
                mime="text/csv"
            )

st.divider()

st.caption(
    "Mini Project | Python | Streamlit | NLP | TF-IDF"
)