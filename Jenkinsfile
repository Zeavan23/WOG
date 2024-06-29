pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'liorn23/wog-web'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']],
                         doGenerateSubmoduleConfigurations: false, extensions: [],
                         submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/Zeavan23/WOG']]])
            }
        }

        stage('Install Python') {
            steps {
                script {
                    bat 'choco install python --version=3.9.0 -y'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    bat 'docker-compose down --remove-orphans || true'
                    bat 'docker-compose up --build -d'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    bat 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "Running tests"
                    bat '"C:\\Users\\nizar\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" C:\\Users\\nizar\\PycharmProjects\\WOG\\test\\e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    bat 'docker-compose down'
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
