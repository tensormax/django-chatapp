# ================================
# Stage 1: Build dependencies
# ================================
FROM python:3.11-slim AS builder

WORKDIR /app

# Install system deps needed for many Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --prefix=/install -r requirements.txt

# ================================
# Stage 2: Final runtime image
# ================================
FROM python:3.11-slim

WORKDIR /app

# System deps required at runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Cloud Run requires PORT env
ENV PORT=8000
EXPOSE 8000

# Run Gunicorn with proper settings
CMD ["gunicorn", "--bind", "0.0.0.0:PORT", "--workers", "2", "--timeout", "60", "auth.wsgi:application"]
