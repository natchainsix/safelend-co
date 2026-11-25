# Illustrative status-cache policy, not a statutory retention period.
RETENTION_DAYS = 30

def purge(records, today):
    return [r for r in records if (today - r["created"]).days < RETENTION_DAYS]
