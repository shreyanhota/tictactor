# Base image for Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the game and Flask code
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Start the Flask application
CMD ["python", "flask_app.py"]
