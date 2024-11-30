# Use the official Python image as the base image for your app
FROM python:3.9-slim

# Install necessary dependencies (Chrome, chromedriver, and Selenium)
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    google-chrome-stable \
    chromium-driver \
    && apt-get clean

# Install Selenium Python bindings
RUN pip install selenium

# Set Chrome and ChromeDriver environment variables
ENV CHROME_BIN="/usr/bin/google-chrome-stable"
ENV CHROME_DRIVER="/usr/bin/chromium-driver"

# Set working directory
WORKDIR /app

# Copy application files into the Docker image
COPY . .

# Expose port 8081
EXPOSE 8081

# Run your web application (e.g., using Flask or any other web server)
CMD ["python", "index.py"]
