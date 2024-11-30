pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'selenium-jenkins-webapp'
        DOCKER_TAG = 'latest'
        PUBLIC_IP = '44.243.227.79'  // Your server's public IP
        PORT = '8081'  // Port on which app will run
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/SidraSaleem296/selenium-jenkins/'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image for your application and tests
                    docker.build("$DOCKER_IMAGE:$DOCKER_TAG")
                }
            }
        }

        stage('Run Web Application in Docker') {
            steps {
                script {
                    // Run the web app in the background on port 8081
                    docker.run("$DOCKER_IMAGE:$DOCKER_TAG", "-d -p $PORT:$PORT")
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    // Run Selenium tests inside the Docker container
                    docker.image("$DOCKER_IMAGE:$DOCKER_TAG").inside {
                        sh 'pytest test_app.py'  // Run the test cases
                    }
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    // Clean up any containers after tests are finished
                    sh 'docker ps -q | xargs docker stop | xargs docker rm'
                }
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean up workspace after each pipeline run
        }
    }
}
