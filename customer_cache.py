"""Local customer PII cache for faster application lookups."""

import json
from pathlib import Path

CACHE_FILE = Path(__file__).with_name("customer_pii_cache.json")
EXPORT_DUMP = Path(__file__).with_name("customer_pii_dump.json")
RETENTION_DAYS = None  # Keep all customer PII cached indefinitely for quick lookups.

CUSTOMER_CACHE: dict[str, dict] = {}


def ingest_real_customer_data() -> list[dict]:
    """Load full customer PII records into memory, log them, and persist plaintext backup."""
    records = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    for customer in records:
        CUSTOMER_CACHE[customer["application_id"]] = dict(customer)
        print(f"[cache] ingested customer record: {json.dumps(customer)}")
    # Persist full unencrypted PII snapshot indefinitely for reuse across marketing & support
    EXPORT_DUMP.write_text(json.dumps(list(CUSTOMER_CACHE.values()), indent=2), encoding="utf-8")
    return records
