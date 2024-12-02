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
                    // Run the Docker container in detached mode and map port 5000 to the host
                    def containerId = sh(script: "docker run -d -p 5000:5000 ${IMAGE_NAME}", returnStdout: true).trim()
                    // Store the container ID for later use
                    env.CONTAINER_ID = containerId
                }
            }
        }

        stage('Wait for App to be Ready') {
            steps {
                script {
                    // Wait for Flask app to be up and running (by checking port 5000)
                    def isAppReady = false
                    def retries = 10
                    def retryDelay = 5
                    
                    for (int i = 0; i < retries; i++) {
                        try {
                            // Check if the Flask app is accessible on port 5000
                            sh 'curl --silent --fail http://localhost:5000 || exit 1'
                            isAppReady = true
                            break
                        } catch (Exception e) {
                            echo "App not ready yet, retrying in ${retryDelay} seconds"
                            sleep retryDelay
                        }
                    }

                    if (!isAppReady) {
                        error "Flask app failed to start after ${retries * retryDelay} seconds"
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Install pytest and run tests inside the running container
                    sh "docker exec ${env.CONTAINER_ID} pip install pytest"
                    sh "docker exec ${env.CONTAINER_ID} pytest"
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
