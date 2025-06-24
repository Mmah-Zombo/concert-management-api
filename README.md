# 🎭 Concert Management API

A RESTful API built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy** with **JWT-based authentication**, designed for managing concert-related data such as Plays, Actors, Directors, Tickets, Customers, and Showtimes.

## 📦 Features


- **User Authentication**  
  - Register & login users with secure JWT tokens  

- **CRUD Operations**  
  - Plays
  - Actors
  - Directors
  - Showtimes
  - Tickets
  - Customers

- **Tech Stack**  
  - FastAPI
  - SQLAlchemy ORM
  - PostgreSQL
  - Python 3.x
  - Pydantic schemas
  - JWT password flows

- **Scalable structure**  
  - Modular design: `models/`, `schemas/`, `routes/`, `utils/`, and `crud/`

- **Interactive docs**  
  - Auto-generated via Swagger UI at `/docs`

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Mmah-Zombo/concert-management-api.git
cd concert-management-api
```

### 2. Set up a virtual environment

```commandline
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


### 3. Install dependencies

```commandline
pip install -r requirements.txt
```

### 4. Set up your PostgreSQL database

Ensure you have `PostgreSQL` installed and create a database for the project.

Update your `.env` file (or environment variables) with your DB credentials:

```requirements
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<your_database>
SECRET_KEY=your_jwt_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Run the server

```commandline
uvicorn main:app --reload
```


Access the interactive docs at: http://127.0.0.1:8000/docs

## 🧱 Project Structure

```commandline
concert-management-api/
│
├── models/         # SQLAlchemy ORM models
├── schemas/        # Pydantic request/response schemas
├── crud/           # DB operations (create, read, update, delete)
├── routes/         # FastAPI routes grouped per entity
├── utils/          # Helper functions (e.g., JWT, auth)
├── database.py     # DB engine & session setup
├── config.py       # Configuration loader (env variables)
├── main.py         # FastAPI app & route links
├── requirements.txt
├── .env.example    # Example environment file
└── README.md
```

## 🔐 Authentication

Authentication
- Register ➝ POST /auth/register: email, password → user
- Login ➝ POST /auth/login: email, password → access_token
-  the token in protected routes:

`Authorization: Bearer <your_token>`

## 👩‍💻 Authors

- M’mah Zombo. GitHub: @Mmah-Zombo
- Josephine Anne-marie. GitHub: Magona @josephine-annmarie-magona


## 📄 License

This project is licensed under the MIT License.