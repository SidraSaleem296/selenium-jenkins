pipeline {
    agent any
    environment {
        // Unique names based on the current timestamp or build number
        UNIQUE_ID = "${BUILD_ID}"  // Use Jenkins build ID to make it unique
        DOCKER_IMAGE = "sample-web-app-${UNIQUE_ID}"
        DOCKER_CONTAINER = "sample-web-app-container-${UNIQUE_ID}"
        PUBLIC_IP = '44.244.209.87'   // Use your actual public IP here
        PORT = '5001'                // Port that you want to expose
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code from GitHub repository...'
                git branch: 'main', url: 'https://github.com/SidraSaleem296/jenkins-webapp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                // Use the dynamically generated image name
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running Docker container...'
                // Stop and remove any existing container with the same name
                sh '''
                    docker ps -q -f name=${DOCKER_CONTAINER} | xargs -r docker stop
                    docker ps -a -q -f name=${DOCKER_CONTAINER} | xargs -r docker rm
                '''
                
                // Run the new container with a dynamic name
                sh 'docker run -d -p ${PORT}:5000 --name ${DOCKER_CONTAINER} ${DOCKER_IMAGE}'
                
                // Wait for the container to fully start
                script {
                    sleep(10) // Add some time for the Docker container to fully spin up
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Running Selenium tests...'
                script {
                    // Make sure the selenium test script is executed and that the server is ready.
                    sh 'python3 test_app.py'
                }
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Cleaning up...'
                // Clean up the container after tests
                sh 'docker stop ${DOCKER_CONTAINER} || true'
                sh 'docker rm ${DOCKER_CONTAINER} || true'
                sh 'docker rmi ${DOCKER_IMAGE} || true' // Optionally remove the image after use
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
            // This will be executed after the pipeline has finished
            // You can add any actions that should run at the end, such as notifications, etc.
        }

        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Please check the logs for errors.'
        }
    }
}
