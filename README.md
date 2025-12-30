Job Application Tracker – Backend

A production-style backend API for tracking job and internship applications, built with FastAPI, PostgreSQL, and SQLAlchemy.
Designed with clean architecture, proper validation, relational data modeling, and RESTful principles.

Features  Core Backend
```text
User management

Job / internship application tracking

One-to-many relationship (User → Applications)

Clean CRUD APIs

Proper HTTP status codes & error handling

```

Backend Engineering Practices
```
Layered architecture (main.py, crud.py, schemas.py, models.py)
SQLAlchemy ORM with relationships
Pydantic request & response schemas
Dependency injection using FastAPI
PostgreSQL integration
```
Planned Enhancements
```
Authentication & Authorization (JWT)
Password hashing
Protected routes
ML-based insights on applications (analytics / predictions)
Cloud deployment
```
Tech Stack
```
Backend Framework: FastAPI
Database: PostgreSQL
ORM: SQLAlchemy
Validation: Pydantic
Language: Python
API Docs: Swagger UI (/docs)
```

Project Structure
```text
job-application-tracker-backend/
├── app/
│   ├── main.py          # API entry point & routes
│   ├── crud.py          # Database CRUD logic
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic request/response validation
│   └── database.py      # Engine configuration & SessionLocal
├── .gitignore           # Python & Environment exclusions
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation

```
 Database Design

User
```
id
name
email
```

Application
```
id
company
role
status
user_id (Foreign Key → User)

Relationship:
One User → Many Applications
```

 API Endpoints
```
Users
POST   /users
GET    /users
GET    /users/{user_id}/applications
```

Applications
```
POST   /applications
GET    /applications
```
Author 🧑🏻‍💻

Roshan

Backend & AI-oriented Developer
Focused on building scalable, future-ready systems.