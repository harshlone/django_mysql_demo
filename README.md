# Django MySQL Demo Project

A Django project with MySQL integration, containerized using Docker, and deployable on Render.

---

## Features

- Django backend with REST API
- MySQL database support (local or cloud)
- Dockerized setup
- Environment variables via `.env`
- Products app for demo

---

## Project Structure

# Django MySQL Demo Project

A Django project with MySQL integration, containerized using Docker, and deployable on Render.

---

## Features

- Django backend with REST API
- MySQL database support (local or cloud)
- Dockerized setup
- Environment variables via `.env`
- Products app for demo

---

## Project Structure

django-postgres-demo/
├── demo_project/ # Django project settings
├── products/ # Django app
├── scripts/ # Utility scripts
├── Dockerfile # Docker build instructions
├── docker-compose.yml # Docker Compose setup
├── requirements.txt # Python dependencies
├── .env # Environment variables (gitignored)
└── manage.py # Django management script


---

## Local Setup

1. **Clone the repo**

```bash
git clone <your-github-repo-url>
cd django-postgres-demo

##Create a virtual environment

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows


##Install dependencies

pip install -r requirements.txt


##Create .env file

DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306


##Run migrations

python manage.py migrate


##Run the server

python manage.py runserver


Access at: http://127.0.0.1:8000

##Docker Setup

Build Docker image

docker build -t django-demo .


##Run Docker container

docker run -p 8000:8000 --env-file .env django-demo


##Access app

http://localhost:8000

