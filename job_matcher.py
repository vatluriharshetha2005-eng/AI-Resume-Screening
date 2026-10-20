from skill_extractor import extract_skills
from nlp_processing import calculate_similarity


def match_resume(filename, resume_text, job_description):

    job_skills = extract_skills(job_description)
    resume_skills = extract_skills(resume_text)

    matched_skills = sorted(
        set(job_skills) & set(resume_skills)
    )

    missing_skills = sorted(
        set(job_skills) - set(resume_skills)
    )

    if job_skills:
        skill_coverage = round(
            len(matched_skills) / len(job_skills) * 100,
            2
        )
    else:
        skill_coverage = 0.0

    similarity = calculate_similarity(
        resume_text,
        job_description
    )

    return {
        "Resume": filename,
        "Skill Coverage (%)": skill_coverage,
        "Text Similarity (%)": similarity,
        "Matched Skills": ", ".join(matched_skills),
        "Missing Skills": ", ".join(missing_skills)
    }