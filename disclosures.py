def agreement_step(explanation_shown, questions_offered):
    if not (explanation_shown and questions_offered):
        return "BLOCKED"
    return "READY_FOR_REVIEW"
