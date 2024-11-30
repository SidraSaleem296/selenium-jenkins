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
                    sh 'docker build -t simple-web-app .'
                }
            }
        }
        stage('Run Application') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 simple-web-app'
                }
            }
        }
        stage('Test Application') {
            steps {
                script {
                    sh 'python3 -m unittest test_app.py'
                }
            }
        }
    }
}
