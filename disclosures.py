def agreement_step(key_features_shown, total_amount_payable_shown, missed_payment_consequences_shown, withdrawal_right_shown, questions_offered):
    required_explanation = all((key_features_shown, total_amount_payable_shown, missed_payment_consequences_shown, withdrawal_right_shown))
    if not (required_explanation and questions_offered):
        return "BLOCKED"
    return "READY_FOR_REVIEW"
