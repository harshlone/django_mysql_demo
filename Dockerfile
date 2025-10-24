# ========================
# Base Image
# ========================
FROM python:3.13-slim

# ========================
# Environment Variables
# ========================
# Prevent Python from writing pyc files and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ========================
# Set Working Directory
# ========================
WORKDIR /code

# ========================
# Install System Dependencies
# ========================
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# ========================
# Copy and Install Python Dependencies
# ========================
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# ========================
# Copy Project Files
# ========================
COPY . .

# ========================
# Collect Static Files
# ========================
RUN python manage.py collectstatic --noinput

# ========================
# Expose Port
# ========================
EXPOSE 8000

# ========================
# Run Gunicorn (Production WSGI Server)
# ========================
CMD ["gunicorn", "demo_project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
