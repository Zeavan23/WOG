pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('dockerhub-credentials')  // Assurez-vous d'avoir configuré vos identifiants DockerHub dans Jenkins
        DOCKER_HUB_REPO = 'your_dockerhub_username/wog-web'
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
                    // Construire l'image Docker
                    bat 'docker-compose down || true'
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
                    bat 'docker tag wog-web:latest ${DOCKER_HUB_REPO}:latest'
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USERNAME')]) {
                        bat 'docker login -u %DOCKER_HUB_USERNAME% -p %DOCKER_HUB_PASSWORD%'
                        bat 'docker push ${DOCKER_HUB_REPO}:latest'
                    }
                }
            }
        }
    }
}
