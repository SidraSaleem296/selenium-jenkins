# Use Python 3.9 slim as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip and install virtualenv
RUN pip install --upgrade pip && \
    pip install virtualenv

# Create a virtual environment in /app/venv
RUN virtualenv venv

# Install the Python dependencies in the virtual environment
RUN /app/venv/bin/pip install -r requirements.txt

# Expose the application port
EXPOSE 5000

# Set the entry point to use the virtual environment's Python interpreter
CMD ["/app/venv/bin/python", "index.py"]
