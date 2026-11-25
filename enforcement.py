def enforcement_step(notice_validated, service_verified, legal_period_elapsed, breach_remedied):
    if notice_validated and service_verified and legal_period_elapsed and not breach_remedied:
        return "LEGAL_REVIEW"
    return "BLOCKED"
