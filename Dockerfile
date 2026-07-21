# Use Python 3.11 slim image
FROM python:3.11-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure logs appear immediately
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy dependency files first (better Docker layer caching)
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy the application
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Start the application
CMD ["uv", "run", "streamlit", "run", "app.py", "--server.address=0.0.0.0"]