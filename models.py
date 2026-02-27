# models.py
from pydantic import BaseModel
from typing import Dict, List

class Candidate(BaseModel):
    id: int
    name: str
    skills: Dict[str, int]  # {"Python": 5, "SQL": 3}

class Internship(BaseModel):
    id: int
    title: str
    required_skills: Dict[str, int]

class Project(BaseModel):
    id: int
    title: str
    required_skills: Dict[str, int]

class MatchResult(BaseModel):
    rank: int
    name: str
    match_score: float
    category: str
    explanation: List[str]