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
| **Backend**    | FastAPI, Python 3.11, Uvicorn  |
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

#!/bin/bash

echo "🚀 Cloning repository and moving into it..."
git clone https://github.com/sathiyaprabha012/social_media_app.git && cd social_media_app || { echo "Failed to clone repo"; exit 1; }

echo "🛠 Creating Python virtual environment..."
python -m venv venv || { echo "Failed to create virtual env"; exit 1; }

echo "⚡ Activating virtual environment..."
# Detect OS and activate accordingly
if [[ "$OSTYPE" == "msys"* ]] || [[ "$OSTYPE" == "win32" ]]; then
  # Windows (Git Bash or WSL)
  source venv/Scripts/activate
else
  # Mac/Linux
  source venv/bin/activate
fi

echo "📦 Installing dependencies..."
pip install -r requirements.txt || { echo "Failed to install dependencies"; exit 1; }

echo "✍️ Creating .env file..."
cat > .env <<EOL
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_USERNAME=yourusername
DATABASE_PASSWORD=yourpassword
DATABASE_NAME=yourdb
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
EOL

echo "🛢 Running database migrations..."
alembic upgrade head || { echo "Migration failed"; exit 1; }

echo "🚀 Starting development server..."
uvicorn app.main:app --reload

