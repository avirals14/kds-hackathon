# Use official Python slim image (Linux)
FROM python:3.10-slim

# Prevent Python buffering issues
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies needed by Pathway
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy dependency list first (Docker cache optimization)
COPY requirements.txt .

# Upgrade pip and install Python deps
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY data/ ./data/

# Default command
CMD ["python", "src/main.py"]