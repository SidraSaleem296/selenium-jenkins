pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask-app"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                // Checkout the code from the Git repository
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image with the Flask app
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Run Application') {
            steps {
                script {
                    // Run the Docker container in detached mode
                    sh 'docker run -d -p 5000:5000 ${DOCKER_IMAGE}'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests within the container, using the virtual environment
                    // Install pytest in the container's virtual environment (if not installed)
                    sh 'docker exec ${DOCKER_IMAGE} /app/venv/bin/pip install pytest'

                    // Run tests using pytest inside the container's virtual environment
                    sh 'docker exec ${DOCKER_IMAGE} /app/venv/bin/python -m pytest'
                }
            }
        }
    }

    post {
        always {
            // Clean up and stop the container after the pipeline
            sh 'docker stop ${DOCKER_IMAGE} || true'
            sh 'docker rm ${DOCKER_IMAGE} || true'
        }
    }
}
