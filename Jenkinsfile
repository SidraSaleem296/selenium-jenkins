pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git 'https://github.com/SidraSaleem296/selenium-jenkins.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t sample-web-app-1 .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running Docker container...'
                sh 'docker run -d -p 5001:5000 --name sample-web-app-container-1 sample-web-app-1'
                script {
                    // Allow some time for the container to start
                    sleep 10
                }
            }
        }

        stage('List Files') {
            steps {
                echo 'Listing files in the workspace...'
                sh 'ls -la'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    pip3 install selenium
                    # Install ChromeDriver and related dependencies
                    apt-get update && apt-get install -y chromium-driver
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Running Selenium tests...'
                sh 'python3 test_app.py'  // Ensure the test script is at the root level
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Cleaning up Docker container...'
                sh 'docker stop sample-web-app-container-1'
                sh 'docker rm sample-web-app-container-1'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
