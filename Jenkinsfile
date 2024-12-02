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
                    sh 'docker build -t flask-app .'
                }
            }
        }
        stage('Run Application') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 flask-app'
                }
            }
        }
    }
}
