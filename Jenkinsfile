pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                script {
                    try {
                        checkout([$class: 'GitSCM', branches: [[name: '*/main']],
                            userRemoteConfigs: [[url: 'https://github.com/SidraSaleem296/selenium-jenkins.git']]
                        ])
                    } catch (Exception e) {
                        echo "Error during Git checkout: ${e}"
                        currentBuild.result = 'FAILURE'
                        error "Stopping pipeline due to checkout failure."
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image from the Dockerfile
                    sh 'docker build -t simple-web-app .'
                }
            }
        }
        stage('Run Application') {
            steps {
                script {
                    // Run the container in detached mode, mapping port 5000
                    sh 'docker run -d -p 5000:5000 --name simple-web-app-container simple-web-app'
                }
            }
        }
        stage('Test Application') {
            steps {
                script {
                    // Run tests inside the running container
                    sh 'docker exec simple-web-app-container python3 -m unittest test_app.py'
                }
            }
        }
        stage('Clean Up') {
            steps {
                script {
                    // Remove the container after the tests have finished
                    sh 'docker rm -f simple-web-app-container'
                }
            }
        }
    }
}
