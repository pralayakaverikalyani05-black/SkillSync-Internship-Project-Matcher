"""
models.py

Defines data models for:
- Candidate
- Internship
- Match Result

Using Pydantic for validation.
"""

from pydantic import BaseModel, Field
from typing import Dict, List


# -----------------------------
# Candidate Model
# -----------------------------
class Candidate(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="Ravi")
    
    # skill name : proficiency (1–5 scale)
    skills: Dict[str, int] = Field(
        ...,
        example={
            "Python": 5,
            "Machine Learning": 4,
            "SQL": 3
        }
    )


# -----------------------------
# Internship Model
# -----------------------------
class Internship(BaseModel):
    id: int = Field(..., example=101)
    title: str = Field(..., example="AI Intern")

    # skill name : weight (importance %)
    required_skills: Dict[str, int] = Field(
        ...,
        example={
            "Python": 40,
            "Machine Learning": 30,
            "SQL": 20,
            "Communication": 10
        }
    )


# -----------------------------
# Match Result Model
# -----------------------------
class MatchResult(BaseModel):
    candidate_name: str
    match_score: float
    explanation: List[str]