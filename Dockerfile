# Use a slim version of Python 3.9 as base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local files into the container
COPY . /app

# Install Flask and Selenium
RUN pip install flask selenium

# Expose port 5000 (this is the port Flask runs on by default)
EXPOSE 5000

# Command to run the Flask application when the container starts
CMD ["python", "index.py"]
