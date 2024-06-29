pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'liorn23/wog-web'  // Utilisez votre nom d'utilisateur Docker Hub
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']],
                         doGenerateSubmoduleConfigurations: false, extensions: [],
                         submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/Zeavan23/WOG']]])
            }
        }

        stage('Build') {
            steps {
                script {
                    // Supprimer les conteneurs orphelins
                    bat 'docker-compose down --remove-orphans || true'
                    // Construire l'image Docker
                    bat 'docker-compose up --build -d'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    // Exécuter le conteneur Docker et exposer le port 8777
                    bat 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Exécuter les tests end-to-end
                    bat 'python test/e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    // Arrêter le conteneur Docker
                    bat 'docker-compose down'

                    // Tagger et pousser l'image Docker vers DockerHub
                    bat "docker tag wog-web:latest ${DOCKER_HUB_REPO}:latest"
                    withCredentials([usernamePassword(credentialsId: '790f7c8d-b10a-4676-86f8-23b4d854c7ecc', passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USERNAME')]) {
                        bat "docker login -u %DOCKER_HUB_USERNAME% -p %DOCKER_HUB_PASSWORD%"
                        bat "docker push ${DOCKER_HUB_REPO}:latest"
                    }
                }
            }
        }
    }
}
