"""
database.py

Simple in-memory database for storing:
- Candidates
- Internships

For hackathon demo purposes.
"""

from typing import List
from models import Candidate, Internship


# -----------------------------
# In-Memory Storage
# -----------------------------

candidates_db: List[Candidate] = []
internships_db: List[Internship] = []


# -----------------------------
# Candidate Operations
# -----------------------------

def add_candidate(candidate: Candidate):
    candidates_db.append(candidate)


def get_all_candidates():
    return candidates_db


def get_candidate_by_id(candidate_id: int):
    for candidate in candidates_db:
        if candidate.id == candidate_id:
            return candidate
    return None


# -----------------------------
# Internship Operations
# -----------------------------

def add_internship(internship: Internship):
    internships_db.append(internship)


def get_all_internships():
    return internships_db


def get_internship_by_id(internship_id: int):
    for internship in internships_db:
        if internship.id == internship_id:
            return internship
    return None