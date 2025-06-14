# 🎭 Concert Management API

A RESTful API built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy** with **JWT-based authentication**, designed for managing concert-related data such as Plays, Actors, Directors, Tickets, Customers, and Showtimes.

## 📦 Features

- JWT Authentication (Login & Register)
- CRUD operations for:
  - Plays
  - Actors
  - Directors
  - Tickets
  - Customers
  - Showtimes
- PostgreSQL for data persistence
- Modular and scalable structure

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Mmah-Zombo/concert-management-api.git
cd concert-management-api
```

### 2. Create and activate virtual environment

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
├── models/             # SQLAlchemy ORM models
├── routes/             # API route definitions
├── schemas/            # Pydantic models
├── auth/               # JWT utilities & user authentication
├── database.py         # DB engine & session management
├── main.py             # FastAPI app entry point
├── requirements.txt    # Python dependencies
```

## 🔐 Authentication

This API uses `JWT` for authentication. Users must login to obtain an access token and include it in the Authorization header for protected routes:

`Authorization: Bearer <your_token>`

## 👩‍💻 Author

M’mah Zombo
GitHub: @Mmah-Zombo

## 📄 License

This project is licensed under the MIT License.