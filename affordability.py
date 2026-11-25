def assess(customer, repayment):
    required = ("monthly_income", "essential_expenses", "commitments")
    if not customer.get("verified") or any(k not in customer for k in required):
        return "MANUAL_REVIEW"
    remaining = customer["monthly_income"] - customer["essential_expenses"] - customer["commitments"] - repayment
    return {"remaining": remaining, "decision": "MANUAL_REVIEW", "policy": "demo-v1"}
