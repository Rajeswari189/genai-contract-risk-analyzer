# MOCK MODE - No API Required

def translate_to_english(text):
    return text  # Assuming already English for demo


def explain_clause(clause):
    explanation = "This clause has been analyzed using our AI engine.\n\n"

    if "terminate" in clause.lower():
        explanation += (
            "⚠ Risk: This clause allows unilateral termination, "
            "which may expose the SME to instability.\n\n"
            "✅ Suggestion: Make termination mutual with 30-day notice."
        )

    elif "indemnify" in clause.lower():
        explanation += (
            "⚠ Risk: Indemnity clause may create unlimited liability.\n\n"
            "✅ Suggestion: Add liability cap equal to 6 months' compensation."
        )

    elif "non-compete" in clause.lower():
        explanation += (
            "⚠ Risk: Long non-compete period may be unreasonable.\n\n"
            "✅ Suggestion: Limit non-compete to 6–12 months and specific geography."
        )

    elif "intellectual property" in clause.lower():
        explanation += (
            "⚠ Risk: Full IP transfer may disadvantage employee or vendor.\n\n"
            "✅ Suggestion: Clarify ownership scope and usage rights."
        )

    else:
        explanation += (
            "No major red flags detected. Clause appears standard."
        )

    return explanation


def generate_summary(text):
    return (
        "This contract contains clauses related to termination, indemnity, "
        "non-compete obligations, and intellectual property transfer.\n\n"
        "Overall, the agreement presents medium-to-high legal exposure for "
        "an SME unless liability limits and mutual protections are added."
    )
