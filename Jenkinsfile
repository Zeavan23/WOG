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
                    docker.build("my-flask-app")
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    // Démarrer les services nécessaires avec Docker Compose
                    sh 'docker-compose up -d'
                    sh 'sleep 10'  // Attendre que l'application démarre

                    // Récupérer l'adresse IP de l'hôte Docker
                    def dockerHostIp = sh(script: "docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-flask-app_web_1", returnStdout: true).trim()

                    // Construire l'URL de l'application Flask
                    def appUrl = "http://${dockerHostIp}:5000"

                    // Exécuter les tests d'end-to-end avec e2e.py
                    sh "python e2e.py ${appUrl}"
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    // Arrêter les services après les tests
                    sh 'docker-compose down'
                    // Pousser l'image Docker construite
                    docker.image('my-flask-app').push()
                }
            }
        }
    }
}

