# Job Application Tracker – Authentication Module

This branch adds **secure authentication and authorization** to the Job Application Tracker backend.

## Features Implemented

- User signup with password hashing (bcrypt)
- User login with JWT token generation
- OAuth2 password flow
- Protected routes using Bearer tokens
- User-specific access control

## Authentication Flow

1. User signs up with email and password  
2. Password is securely hashed before storing in the database  
3. User logs in and receives a JWT access token  
4. Token is sent in the `Authorization` header for protected requests  
5. Backend validates token and identifies the current user  

## Key Endpoints

- `POST /users/signup` – Create a new user  
- `POST /users/login` – Authenticate user and return JWT  
- Protected routes require:


## Security Notes

- Passwords are never stored in plain text
- JWT tokens contain user identity and expiry
- Access to applications is restricted to the owner

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- JWT (OAuth2)
- Passlib (bcrypt)

This branch focuses on **backend security and access control**, following industry best practices.
