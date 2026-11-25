def save_status(db, customer):
    # This store exists solely to track application status.
    db.append({"application_id": customer["application_id"], "status": customer["status"]})
