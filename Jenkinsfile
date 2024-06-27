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
                        sh 'docker-compose down'
                        sh 'docker-compose up --build -d'
                    } else {
                        bat 'docker-compose down'
                        bat 'docker-compose up --build -d'
                    }
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    // Vérifiez si le conteneur est en cours d'exécution
                    if (isUnix()) {
                        sh 'docker ps | grep wog-web'
                    } else {
                        bat 'docker ps | findstr wog-web'
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                if (isUnix()) {
                    sh 'docker-compose down'
                } else {
                    bat 'docker-compose down'
                }
            }
        }
    }
}
