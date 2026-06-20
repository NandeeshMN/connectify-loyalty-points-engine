# Connectify Loyalty Points Engine - Writeup

---

## Assumptions

1. Every event contains a unique event ID.
2. Duplicate event IDs should not be processed more than once.
3. Rewards are predefined in the rewards catalogue.
4. Event reversals can only occur once per event.
5. User balance is calculated from ledger entries instead of being stored directly.

---

## Design Decisions

### Event Processing

The event ingestion endpoint uses unique event IDs to ensure idempotency. Duplicate submissions are detected and ignored.

### Rules Engine

Business rules are stored in a separate configuration file (`rules.json`) instead of being hardcoded inside API endpoints.

This allows:

- Easy modification of points rules
- Flexible business rule management
- Separation of business logic from application code

### Points Ledger

A ledger-based approach was implemented instead of maintaining a balance column.

Every points movement is stored as a separate immutable ledger entry:

- CREDIT
- DEBIT
- REVERSAL

Current balance is derived by summing ledger records.

### Redemption

Users can redeem rewards only when they have sufficient points balance.

Redemption requests that exceed the available balance are rejected.

### Reversal

Reversals are implemented using compensating ledger entries rather than deleting historical records.

This ensures complete auditability and transaction traceability.

---

## Assignment Requirements Mapping

### 2.1 Event Ingestion

Implemented:

- Unique Event ID
- User ID
- Event Type
- Amount
- Timestamp
- Idempotent Processing

### 2.2 Rules Engine

Implemented:

- Configurable Rules (rules.json)
- Base Points Rule
- Weekend Multiplier Rule
- Maximum Points Cap

### 2.3 Points Ledger

Implemented:

- Immutable Ledger Records
- Credit Entries
- Debit Entries
- Reversal Entries
- Balance Derived from Ledger

### 2.4 Redemption

Implemented:

- Reward Catalogue
- Reward Redemption
- Insufficient Balance Validation

### 2.5 Reversal

Implemented:

- Event Reversal Endpoint
- Compensating Ledger Entries
- Full Audit History Preservation

---

## Trade-offs

1. SQLite was chosen for simplicity and quick setup.
2. Authentication and authorization were not implemented because they were outside the assignment scope.
3. Rules are stored in JSON configuration rather than a database table.
4. Reward catalogue management is implemented through a utility endpoint for demonstration purposes.


---

## Conclusion

The solution implements a configurable loyalty points engine with event ingestion, points calculation, ledger accounting, reward redemption, and event reversal while maintaining idempotency and auditability.
