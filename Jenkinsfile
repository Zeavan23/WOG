pipeline {
    agent any

    stages {
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
                script {
                    // Libérer le port 8777 s'il est occupé
                    bat 'netstat -ano | findstr :8777 | findstr LISTENING && for /f "tokens=5" %a in (\'netstat -ano ^| findstr :8777 ^| findstr LISTENING\') do taskkill /f /pid %a || echo Port 8777 is not in use'
                }
                bat 'docker-compose up -d'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests'
                bat ".venv\\Scripts\\python C:\\Users\\nizar\\PycharmProjects\\WOG\\test\\e2e.py"
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
