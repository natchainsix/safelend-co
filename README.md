# Safelend

Synthetic consumer lending repository for regulatory code review. Run `python app.py` (Python 3.9+, no dependencies). All storage is in memory. Never use real customer data.

## Review context
Assume a UK regulated personal credit agreement, no relevant exemptions, and that these functions are the only controls for the illustrated operations. The status cache needs only application ID and status; audit needs only application ID and event. No legal requirement to retain this duplicate cache indefinitely is assumed. The enforcement example concerns termination or acceleration for breach within CCA s87 scope.

Review against FCA CONC 5.2A, CONC 4.2.5R, CCA ss87–88 and UK GDPR Art 5. Positive controls are illustrative, not legal certification. Full disclosures, policy validation, security and operational evidence are outside scope.
