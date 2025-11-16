FastAPI Blog API
=================

A simple FastAPI project that exposes JWT‑protected CRUD APIs for Users and Blogs.

It uses:
- FastAPI + Starlette for the web framework
- SQLAlchemy (sync) for ORM
- Pydantic v2 for request/response schemas
- BCrypt for password hashing
- OAuth2 with Password flow and JWT (via `python-jose`)
- Alembic for database migrations 


Features
--------
- User management: create, list, retrieve, delete
- Blog management: create, list, retrieve, update, delete
- OAuth2 Password flow with Bearer tokens
- Passwords hashed with bcrypt
- Interactive API docs at `/docs` and `/redoc`


Project layout
--------------
```
FastApi/
├─ main.py                    # App entrypoint, includes routers
├─ database.py                # SQLAlchemy engine & session factory
├─ models.py                  # SQLAlchemy models (User, Blog)
├─ schemas.py                 # Pydantic schemas
├─ oauth2.py                  # JWT creation + current user dependency
├─ hashPassword.py            # bcrypt helpers
├─ routers/
│  ├─ authentication.py       # POST /authentication (login)
│  ├─ blogs.py                # /blogs endpoints (JWT‑protected)
│  └─ users.py                # /users endpoints (JWT‑protected)
├─ repository/
│  ├─ blogs.py                # CRUD logic for blogs
│  └─ users.py                # CRUD logic for users
├─ alembic/                   # (Optional) migrations
├─ alembic.ini
└─ requirements.txt
```
Authentication
--------------
The API uses OAuth2 Password flow with JWT Bearer tokens.

- Token endpoint: `POST /authentication/`
- Request format: `application/x-www-form-urlencoded` (standard `OAuth2PasswordRequestForm`)
  - Field `username` is treated as the user email in this project
  - Field `password` is the user password


Configuration
-------------
Environment variables (loaded from `.env`):
- `DATABASE_URL` (required) — SQLAlchemy database URL
- `SECRET_KEY` (required for JWT)


