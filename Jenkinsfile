pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\pip install --upgrade pip'
                bat '.venv\\Scripts\\pip install selenium webdriver_manager'
            }
        }

        stage('Build') {
            steps {
                bat 'docker-compose down --remove-orphans || true'
                bat 'docker-compose up --build -d'
            }
        }

        stage('Run') {
            steps {
                bat 'docker-compose up -d'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests'
                bat '.venv\\Scripts\\python C:\\Users\\nizar\\PycharmProjects\\WOG\\test\\e2e.py'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up'
            bat 'docker-compose down'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
