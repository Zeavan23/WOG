pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Zeavan23/WOG'
            }
        }
        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\pip install --upgrade pip'
                bat '.venv\\Scripts\\pip install selenium webdriver_manager'
            }
        }
        stage('Run Docker') {
            steps {
                script {
                    bat 'docker-compose down --remove-orphans || true'
                    bat 'docker-compose up --build -d'
                }
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests'
                bat '.venv\\Scripts\\python C:\\Users\\nizar\\PycharmProjects\\WOG\\test\\e2e.py'
            }
        }
    }
    post {
        always {
            echo 'Cleaning up Docker containers'
            bat 'docker-compose down'
        }
    }
}
