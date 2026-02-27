# backend.py

from fastapi import FastAPI
from typing import List
from models import Candidate, Internship, Project
from database import add_candidate, add_internship, add_project, get_all_candidates, get_internship_by_id, get_project_by_id
from matching import rank_candidates

app = FastAPI()

# -------------------
# Candidate Endpoints
# -------------------

@app.post("/add_candidate")
def api_add_candidate(candidate: Candidate):
    add_candidate(candidate)
    return {"message": f"Candidate {candidate.name} added successfully!"}

@app.get("/get_candidates", response_model=List[Candidate])
def api_get_candidates():
    return get_all_candidates()


# -------------------
# Internship Endpoints
# -------------------

@app.post("/add_internship")
def api_add_internship(internship: Internship):
    add_internship(internship)
    return {"message": f"Internship '{internship.title}' added successfully!"}

@app.get("/match_internship/{internship_id}")
def api_match_internship(internship_id: int):
    internship = get_internship_by_id(internship_id)
    if not internship:
        return {"error": "Internship not found"}

    # 🔹 Apply communication filter for internships
    results = rank_candidates(get_all_candidates(), internship.required_skills, filter_communication=True)
    if not results:
        return {"error": "No eligible candidates due to poor communication"}
    return results


# -------------------
# Project Endpoints
# -------------------

@app.post("/add_project")
def api_add_project(project: Project):
    add_project(project)
    return {"message": f"Project '{project.title}' added successfully!"}

@app.get("/match_project/{project_id}")
def api_match_project(project_id: int):
    project = get_project_by_id(project_id)
    if not project:
        return {"error": "Project not found"}

    # Projects can consider all candidates
    results = rank_candidates(get_all_candidates(), project.required_skills, filter_communication=False)
    if not results:
        return {"error": "No candidates available"}
    return results