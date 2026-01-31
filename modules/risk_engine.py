risk_patterns = {
    "Penalty Clause": ["penalty", "liquidated damages"],
    "Indemnity Clause": ["indemnify", "hold harmless"],
    "Unilateral Termination": ["sole discretion", "terminate without notice"],
    "Auto Renewal": ["automatically renew"],
    "Non-Compete": ["non-compete", "restrict"],
    "IP Transfer": ["intellectual property shall belong"],
    "Arbitration Clause": ["arbitration", "jurisdiction"]
}

def analyze_clause(clause):
    risk_score = 1
    issues = []

    for category, keywords in risk_patterns.items():
        for word in keywords:
            if word in clause.lower():
                issues.append(category)
                risk_score = 3

    if len(clause) > 700:
        risk_score = 2

    if risk_score == 1:
        level = "Low"
    elif risk_score == 2:
        level = "Medium"
    else:
        level = "High"

    return level, issues


def contract_risk_score(results):
    score_map = {"Low": 1, "Medium": 2, "High": 3}
    avg = sum([score_map[r["risk"]] for r in results]) / len(results)

    if avg < 1.5:
        return "Low"
    elif avg < 2.3:
        return "Medium"
    else:
        return "High"
