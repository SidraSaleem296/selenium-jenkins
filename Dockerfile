# Use a slim Python base image
FROM python:3.8-slim

# Set environment variables for Chrome (optional but can be useful for headless Chrome)
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies for Chrome and Chromium
RUN apt-get update && \
    apt-get install -y \
    wget \
    curl \
    unzip \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libxss1 \
    libasound2 \
    libappindicator3-1 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libnotify4 \
    fonts-liberation \
    xdg-utils \
    ca-certificates \
    && apt-get clean

# Install Google Chrome stable version (for headless mode)
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# Install ChromeDriver (matching the Chrome version)
RUN wget -q "https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip" -P /tmp && \
    unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin && \
    rm /tmp/chromedriver_linux64.zip

# Set Chrome options to run in headless mode
ENV CHROME_BIN=/usr/bin/google-chrome-stable
ENV CHROMEDRIVER=/usr/local/bin/chromedriver

# Set up a working directory
WORKDIR /app

# Copy your requirements file if you have one
COPY requirements.txt /app/

# Install Python dependencies (like Selenium)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and Selenium test script into the container
COPY . /app/

# Command to run your application or tests (you may adjust this based on your needs)
CMD ["python", "test_app.py"]
