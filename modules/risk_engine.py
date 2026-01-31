risk_patterns = {
    "Penalty Clause": ["penalty", "liquidated damages", "interest", "late payment"],
    "Indemnity Clause": ["indemnify", "hold harmless"],
    "Unilateral Termination": ["sole discretion", "without notice"],
    "Auto Renewal": ["auto-renew", "automatically renew"],
    "Non-Compete": ["non-compete", "not provide similar services", "restrict"],
    "IP Transfer": ["intellectual property", "exclusive property"],
    "Arbitration Clause": ["arbitration"],
    "Jurisdiction Clause": ["jurisdiction", "courts of"],
    "Limitation of Liability": ["liability shall not exceed"],
    "Lock-in Period": ["minimum term", "lock-in"]
}

def analyze_clause(clause):
    score = 1
    issues = []

    for category, keywords in risk_patterns.items():
        for word in keywords:
            if word.lower() in clause.lower():
                issues.append(category)
                score += 1

    if score <= 2:
        level = "Low"
    elif score <= 4:
        level = "Medium"
    else:
        level = "High"

    return level, issues, score


def contract_risk_score(results):
    avg = sum([r["numeric_score"] for r in results]) / len(results)

    if avg < 2:
        return "Low"
    elif avg < 4:
        return "Medium"
    else:
        return "High"
