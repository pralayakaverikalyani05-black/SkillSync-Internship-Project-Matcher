from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List
from matching import calculate_match, generate_explanation

app = FastAPI()

# In-memory storage (for demo)
candidates = []
internships = []


# ----------- Data Models ------------

class Candidate(BaseModel):
    id: int
    name: str
    skills: Dict[str, int]  # skill: proficiency (1-5)


class Internship(BaseModel):
    id: int
    title: str
    required_skills: Dict[str, int]  # skill: weight


# ----------- Add Candidate ------------

@app.post("/add_candidate")
def add_candidate(candidate: Candidate):
    candidates.append(candidate)
    return {"message": "Candidate added successfully"}


# ----------- Add Internship ------------

@app.post("/add_internship")
def add_internship(internship: Internship):
    internships.append(internship)
    return {"message": "Internship added successfully"}


# ----------- Match Candidates ------------

@app.get("/match/{internship_id}")
def match_candidates(internship_id: int):
    internship = next((i for i in internships if i.id == internship_id), None)

    if not internship:
        return {"error": "Internship not found"}

    results = []

    for candidate in candidates:
        score = calculate_match(candidate.skills, internship.required_skills)
        explanation = generate_explanation(candidate.skills, internship.required_skills)

        results.append({
            "candidate_name": candidate.name,
            "match_score": score,
            "explanation": explanation
        })

    # Sort by highest score
    results.sort(key=lambda x: x["match_score"], reverse=True)

    return results