pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                git 'https://github.com/Zeavan23/WOG'
            }
        }
        stage('Setup Python Environment') {
            steps {
                // Set up a Python virtual environment
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\pip install --upgrade pip'
                bat '.venv\\Scripts\\pip install selenium webdriver_manager'
            }
        }
        stage('Run Docker') {
            steps {
                script {
                    // Ensure any previous containers are removed
                    bat 'docker-compose down --remove-orphans || true'
                    // Build and start the Docker containers
                    bat 'docker-compose up --build -d'
                }
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests'
                // Run the test script using the virtual environment's Python executable
                bat '.venv\\Scripts\\python C:\\Users\\nizar\\PycharmProjects\\WOG\\test\\e2e.py'
            }
        }
    }
    post {
        always {
            echo 'Cleaning up Docker containers'
            // Always clean up Docker containers
            bat 'docker-compose down'
        }
    }
}
