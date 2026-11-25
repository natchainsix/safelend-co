import json
from pathlib import Path
from customer_service import save_status
from audit_logger import audit
from affordability import assess
from disclosures import agreement_step
from enforcement import enforcement_step

def main():
    customer = json.loads(Path(__file__).with_name("sample_customer.json").read_text())
    db, log = [], []
    save_status(db, customer)
    audit(log, customer, "application_received")
    print(json.dumps({"status_store": db, "audit": log, "assessment": assess(customer, 500), "agreement": agreement_step(False, False), "enforcement": enforcement_step(False, False, False, False)}, indent=2))

if __name__ == "__main__":
    main()
