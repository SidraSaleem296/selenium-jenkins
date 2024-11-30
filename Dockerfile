# Use a Python slim image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask (required for your application)
RUN pip install flask

# Install Selenium for the tests
RUN pip install selenium

# Expose port 5000 for the Flask application
EXPOSE 5000

# Command to run the application
CMD ["python", "index.py"]
