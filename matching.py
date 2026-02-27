def calculate_match(candidate_skills, required_skills):
    score = 0
    total_weight = 0

    for skill, weight in required_skills.items():
        total_weight += weight

        if skill in candidate_skills:
            proficiency = candidate_skills[skill]
            normalized_score = (proficiency / 5) * weight
            score += normalized_score

    if total_weight == 0:
        return 0

    final_score = (score / total_weight) * 100
    return round(final_score, 2)


def generate_explanation(candidate_skills, required_skills):
    explanation = []

    for skill, weight in required_skills.items():
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