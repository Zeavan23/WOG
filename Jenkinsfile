pipeline {
    agent any

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
                    bat 'docker-compose down || true'
                    bat 'docker-compose up --build -d'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    bat 'python -m pip install --upgrade pip'
                    bat 'pip install selenium'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    bat 'python C:\\Users\\nizar\\PycharmProjects\\WOG\\test\\e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    bat 'docker-compose down'
                    bat 'docker tag wog-web:latest liorn23/wog-web:latest'
                    bat 'docker push liorn23/wog-web:latest'
                }
            }
        }
    }

    post {
        always {
            script {
                bat 'docker-compose down'
            }
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
