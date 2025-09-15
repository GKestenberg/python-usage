FROM python:3.9-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy requirements and install dependencies
COPY requirements.txt .
RUN uv pip install --system -r requirements.txt

# Copy application code
COPY app.py .

# Expose port
EXPOSE 3000

# Run the application
CMD ["python", "app.py"]