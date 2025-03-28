# Base image
FROM python:3.9-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create and switch to app user
RUN useradd -m -d /app -s /bin/bash appuser
WORKDIR /app
USER appuser

# Install Python dependencies
COPY --chown=appuser:appuser requirements /app/requirements
RUN pip install --user --no-cache-dir -r requirements/production.txt

# Copy application code
COPY --chown=appuser:appuser . /app

# Entrypoint configuration
COPY --chown=appuser:appuser ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]