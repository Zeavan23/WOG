pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker build -t my-flask-app .'
                    } else {
                        bat 'docker build -t my-flask-app .'
                    }
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker run -d -p 5000:5000 my-flask-app'
                    } else {
                        bat 'docker run -d -p 5000:5000 my-flask-app'
                    }
                }
            }
        }
    }
}
