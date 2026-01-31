# Stage 1: Use a small footprint Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy only requirements first (best practice for caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py ..

# Flask default port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
