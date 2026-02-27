# database.py
from typing import List
from models import Candidate, Internship, Project

# In-memory storage
candidates_db: List[Candidate] = []
internships_db: List[Internship] = []
projects_db: List[Project] = []

# Candidate functions
def add_candidate(candidate: Candidate):
    candidates_db.append(candidate)

def get_all_candidates():
    return candidates_db

# Internship functions
def add_internship(internship: Internship):
    internships_db.append(internship)

def get_internship_by_id(internship_id: int):
    for internship in internships_db:
        if internship.id == internship_id:
            return internship
    return None

# Project functions
def add_project(project: Project):
    projects_db.append(project)

def get_project_by_id(project_id: int):
    for project in projects_db:
        if project.id == project_id:
            return project
    return None