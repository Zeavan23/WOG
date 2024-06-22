pipeline {
    agent any

    environment {
        appUrl = 'http://localhost:5000' // Définissez ici votre URL d'application
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build("my-flask-app")
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    docker.withRun('-p 5000:5000 --name my-app my-flask-app:latest') { c ->
                        sh 'sleep 10'  // Attendre que l'application démarre
                        sh "python e2e.py ${env.appUrl}" // Utilisation de l'URL définie dans l'environnement
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    docker.image('my-flask-app').push()
                }
            }
        }
    }
}
