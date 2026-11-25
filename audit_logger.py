def audit(log, customer, event):
    log.append({"application_id": customer["application_id"], "event": event})
