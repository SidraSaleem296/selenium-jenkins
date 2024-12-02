# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install pipenv or virtualenv (optional, but recommended)
RUN pip install --upgrade pip && \
    pip install virtualenv

# Create a virtual environment
RUN virtualenv venv

# Activate the virtual environment and install dependencies
RUN /app/venv/bin/pip install -r requirements.txt

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["/app/venv/bin/python", "index.py"]
