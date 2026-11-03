# timeline

An AI-assisted Available-to-Promise (ATP) platform that calculates reliable delivery dates using real production capacity, inventory constraints, and routing data.

The system combines deterministic scheduling algorithms with agentic AI workflows capable of transforming unstructured business inputs (emails, notes, spreadsheets, screenshots, PDFs) into structured production data.

---

# Why timeline?

Most SMEs still calculate delivery commitments using spreadsheets, tribal knowledge, or rough estimates.

timeline aims to answer one question:

> "If I receive a new customer order today, when can I realistically deliver it?"

The answer must be:

- Capacity-aware
- Routing-aware
- Data-driven
- Explainable
- Auditable

AI assists the user, but never replaces the mathematical scheduling engine.

---

# Core Principles

## AI for understanding

AI is used to:

- extract data
- classify information
- validate inputs
- recommend governance improvements

## Mathematics for planning

AI never calculates capacity.

Scheduling decisions are performed by deterministic Python algorithms.

This guarantees:

- reproducibility
- auditability
- reliability

---

# Architecture

```text
User Input
(Text / PDF / Screenshot)
            │
            ▼
     Gemini Agent
            │
            ▼
 Structured Validation
     (Pydantic)
            │
            ▼
       Supabase
            │
            ▼
 Capacity Engine
   (scheduler.py)
            │
            ▼
  Delivery Promise
        (ATP)
```

---

# Technology Stack

| Layer | Technology |
|---------|---------|
| Frontend | Streamlit |
| AI | Gemini AI Studio |
| Validation | Pydantic |
| Database | Supabase (PostgreSQL) |
| Scheduling | Python + Pandas |
| Testing | Pytest |
| Dev Environment | GitHub Codespaces |
| Deployment | Streamlit Community Cloud |

---

# Database Model

## Products

Represents the product master data.

Primary Key:

```text
id_product
```

Examples:

```text
PRD-0001
PRD-0002
```

---

## Equipment

Represents production resources.

Primary Key:

```text
id_equipment
```

Examples:

```text
CNC-01
CUTTER-02
PRESS-03
```

---

## Routings

Represents the sequence of operations required to manufacture a product.

Relationship:

```text
Product
    ↓
Routing
    ↓
Equipment
```

---

# Development Roadmap

## Week 1

Foundation

Deliverables:

- Repository structure
- Codespaces setup
- Supabase connection
- CRUD operations
- Environment management

Files:

```text
database.py
.env
```

---

## Week 2

Capacity Engine

Deliverables:

- Finite capacity scheduling
- ATP calculations
- Equipment load simulation
- Unit testing

Files:

```text
scheduler.py
tests/test_scheduler.py
```

---

## Week 3

Agentic Layer

Deliverables:

- Intent recognition
- Structured extraction
- SKU validation
- Governance recommendations

Files:

```text
agent.py
```

---

## Week 4

Application Layer

Deliverables:

- Streamlit UI
- Dashboard
- Chat interface
- Deployment

Files:

```text
app.py
```

---

# Repository Structure

```text
timeline/
│
├── .devcontainer/
│   └── devcontainer.json
│
├── app.py
├── agent.py
├── database.py
├── scheduler.py
│
├── tests/
│   └── test_scheduler.py
│
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

# Future Enhancements

- Multi-factory planning
- Shift calendars
- Maintenance windows
- Inventory ATP
- Customer portal
- ERP integration
- Predictive lead times
- What-if simulations

---
