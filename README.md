# 📱 Social Media Backend Clone using FastAPI

A backend clone of a social media application built using **FastAPI** and modern backend technologies. This project demonstrates the entire backend development workflow — from API design to testing and CI/CD deployment.

---

## 🚀 Features

- ⚡ High-performance asynchronous APIs with FastAPI  
- 🔐 User authentication with OAuth2 and JWT tokens  
- 🧱 Relational data modeling using SQLAlchemy  
- 🔄 Database migrations using Alembic  
- 🐳 Fully Dockerized environment for development & production  
- 🧪 Robust testing suite with Pytest  
- 🔄 CI/CD pipeline using GitHub Actions  
- ✅ Modular, scalable and clean project structure  

---

## 📦 Tech Stack

| Layer         | Technologies Used              |
|---------------|--------------------------------|
| **Backend**    | FastAPI, Python 3.113.13.1, Uvicorn  |
| **API Testing**| Postman                        |
| **Database**   | PostgreSQL                     |
| **ORM**        | SQLAlchemy                     |
| **Validation** | Pydantic                       |
| **Auth**       | OAuth2, JWT                    |
| **Migrations** | Alembic                        |
| **Testing**    | Pytest, FastAPI TestClient     |
| **DevOps**     | Docker, Docker Compose         |
| **CI/CD**      | GitHub Actions                 |
| **Versioning** | Git, GitHub                    |
| **Config**     | Environment variables via `.env` |

---

## ⚙️ How to Run Locally

### 1.Clone the repository:
```bash
git clone https://github.com/kamalisreesathiyamoorthi/fastapi-project
cd FASTAPI
```

### 2.Create a virtual environment:
```bash
python -m venv venv
```

### 3.Install dependencies:
```bash
pip install -r requirements.txt
```

### 4.Configure environment variables:

- Create a .env file in the root directory with the following content:
```bash
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_USERNAME=yourusername
DATABASE_PASSWORD=yourpassword
DATABASE_NAME=yourdb
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5.Run the API Server:
```bash
uvicorn app.main:app --reload
```

### 6.Access the API:
- Open your browser and go to: http://localhost:8000/docs

### 7.Run tests:
```bash
pytest -v fastapi/tests
```








