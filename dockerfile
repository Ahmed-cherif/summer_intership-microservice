# Base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the required files to the working directory
COPY requirements.txt .
COPY app.py .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the application will run
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
