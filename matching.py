# matching.py

from typing import List, Dict
from models import Candidate

def calculate_match(candidate_skills: Dict[str, int], required_skills: Dict[str, int]) -> float:
    """
    Calculate the weighted match score between candidate skills and required skills.
    Returns a percentage value between 0 and 100.
    """
    score = 0
    total_weight = sum(required_skills.values())
    if total_weight == 0:
        return 0.0

    for skill, weight in required_skills.items():
        if skill in candidate_skills:
            proficiency = candidate_skills[skill]  # Assume scale 1-5
            score += (proficiency / 5) * weight

    final_score = (score / total_weight) * 100
    return round(final_score, 2)


def generate_explanation(candidate_skills: Dict[str, int], required_skills: Dict[str, int]):
    """
    Generate a textual explanation of candidate's skill levels.
    """
    explanation = []

    for skill in required_skills:
        if skill in candidate_skills:
            level = candidate_skills[skill]
            if level >= 4:
                explanation.append(f"Strong in {skill}")
            elif level >= 2:
                explanation.append(f"Moderate in {skill}")
            else:
                explanation.append(f"Weak in {skill}")
        else:
            explanation.append(f"Missing {skill}")

    return explanation


def rank_candidates(candidates: List[Candidate], required_skills: Dict[str, int], filter_communication: bool = False):
    """
    Rank candidates based on match score and classify performance.
    If filter_communication=True, exclude candidates with Communication <=2.
    """
    results = []

    for candidate in candidates:
        # 🔹 Communication filter
        comm_score = candidate.skills.get("Communication", 0)
        if filter_communication and comm_score <= 2:
            continue  # Skip candidate with poor communication

        score = calculate_match(candidate.skills, required_skills)
        explanation = generate_explanation(candidate.skills, required_skills)

        # 🔥 Performance Classification
        if score >= 90:
            category = "Top Performer 🟢"
        elif score >= 60:
            category = "Medium Performer 🟡"
        else:
            category = "Low Performer 🔴"

        results.append({
            "name": candidate.name,
            "match_score": score,
            "category": category,
            "explanation": explanation
        })

    # Sort candidates by score descending
    results.sort(key=lambda x: x["match_score"], reverse=True)

    # Assign rank
    for i, r in enumerate(results):
        r["rank"] = i + 1

    return results