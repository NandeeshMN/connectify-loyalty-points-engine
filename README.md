# Connectify Loyalty Points Engine

---

## Project Overview

Connectify Loyalty Points Engine is a transactional loyalty and rewards backend system built using FastAPI, SQLAlchemy, and SQLite.

The system allows users to earn points through business events, redeem rewards, reverse transactions, and maintain a complete auditable history of all points movements.

---

## Project Context & Domain Choice

For this assignment, I selected a generic customer loyalty program domain that can be applied to e-commerce, retail, fintech, and referral-based platforms.
The goal was to build a backend system demonstrating core backend engineering concepts:
- Event Processing
- Event Idempotency
- Configurable Rules Engine
- Immutable Ledger
- Reward Redemption
- Event Reversals

The implementation focuses on correctness, auditability, and extensibility while keeping the architecture simple and easy to evaluate.

---

## Quick Start

### Clone Repository

```bash
git clone https://github.com/NandeeshMN/connectify-loyalty-points-engine.git
cd connectify-loyalty-points-engine
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

PowerShell:

```bash
venv\Scripts\Activate.ps1
```

Command Prompt:

```bash
venv\Scripts\activate.bat
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn main:app --reload
```

### Open API Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Features

### Event Ingestion

Processes transaction events containing:

- Event ID
- User ID
- Event Type
- Amount
- Timestamp

Supports strict idempotency by preventing duplicate event processing.

### Configurable Rules Engine

Business rules are maintained in:

```text
rules.json
```

Supported rules:

- Base points per event type
- Weekend multiplier bonus
- Maximum points cap per event

### Immutable Points Ledger

The system maintains a complete ledger rather than a mutable balance field.

Each points movement is stored as:

- CREDIT
- DEBIT
- REVERSAL

Current balances are calculated dynamically from ledger records.

### Reward Redemption

Users can redeem earned points against a reward catalogue.

Sample rewards:

- ₹100 Coupon
- ₹500 Coupon
- Free Delivery

Redemptions are rejected when sufficient points are unavailable.

### Event Reversal

Events can be reversed without deleting historical records.

Instead, compensating ledger entries are created to preserve a complete audit trail.

---

## Design Decisions

### Idempotent Event Processing

The system validates event IDs before processing.

This ensures duplicate requests do not award points multiple times.

### Externalized Rules

Business rules are stored in a JSON configuration file instead of being hardcoded.

Benefits:

- Easier maintenance
- Better flexibility
- Separation of business logic from application code

### Ledger-Based Accounting

Balances are not stored directly.
All balances are derived from ledger transactions, ensuring complete traceability and auditability.

### Compensating Reversals

Rather than deleting records, reversals create offsetting transactions.
This mirrors real-world financial transaction systems.

---

## Assignment Requirements Coverage

### 2.1 Event Ingestion

Implemented:

- Unique Event ID
- User ID
- Event Type
- Amount
- Timestamp
- Idempotency

### 2.2 Rules Engine

Implemented:

- Base Points Rule
- Weekend Multiplier
- Points Cap
- Configurable JSON Rules

### 2.3 Points Ledger

Implemented:

- Immutable Ledger
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
- Compensating Entries
- Full Audit History Preservation

---


## Technology Stack

### Backend

- Python
- FastAPI

### Database

- SQLite
- SQLAlchemy ORM


### API Documentation

- Swagger UI
- OpenAPI

---
