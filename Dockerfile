# Multi-stage Dockerfile for Accounts Microservice

# Stage 1: Build stage
FROM python:3.9-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Final runtime stage
FROM python:3.9-slim

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Copy installed Python packages from builder stage
COPY --from=builder /root/.local /root/.local
COPY . .

# Set environment variables
ENV PATH=/root/.local/bin:$PATH \
    PORT=8080 \
    FLASK_APP=service:app

# Expose microservice port
EXPOSE 8080

# Create non-root user for security best practice
RUN useradd -u 1000 theia && chown -R theia:theia /app
USER theia

# Start Gunicorn server
CMD ["gunicorn", "--bind=0.0.0.0:8080", "--log-level=info", "service:app"]
