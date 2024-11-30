pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/SidraSaleem296/selenium-jenkins.git'
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
