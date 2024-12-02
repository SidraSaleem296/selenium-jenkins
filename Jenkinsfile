pipeline {
    agent any
    environment {
        IMAGE_NAME = "flask-app"
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t ${IMAGE_NAME} .'
                }
            }
        }

        stage('Run Application') {
            steps {
                script {
                    // Run the Docker container in detached mode
                    def containerId = sh(script: "docker run -d -p 5000:5000 ${IMAGE_NAME}", returnStdout: true).trim()
                    // Store the container ID for later use
                    env.CONTAINER_ID = containerId
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Wait for the container to be fully ready (you can customize this sleep time as needed)
                    sleep 10
                    
                    // Run tests inside the running container
                    sh "docker exec ${env.CONTAINER_ID} /app/venv/bin/pip install pytest"
                    sh "docker exec ${env.CONTAINER_ID} /app/venv/bin/pytest"
                }
            }
        }

        stage('Post Actions') {
            steps {
                script {
                    // Stop and remove the container after the tests
                    sh "docker stop ${env.CONTAINER_ID} || true"
                    sh "docker rm ${env.CONTAINER_ID} || true"
                }
            }
        }
    }
    post {
        always {
            // Cleanup, ensure Docker system is not cluttered
            sh 'docker system prune -f'
        }
    }
}
