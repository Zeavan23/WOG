pipeline {
    agent any

    stages {
        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\pip install --upgrade pip --user'
                bat '.venv\\Scripts\\pip install selenium webdriver_manager --user'
            }
        }

        stage('Download geckodriver') {
            steps {
                script {
                    def geckoDriverUrl = "https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-win64.zip"
                    def downloadPath = "${WORKSPACE}\\geckodriver.zip"
                    def extractPath = "${WORKSPACE}\\geckodriver"
                    powershell """
                    Invoke-WebRequest -Uri ${geckoDriverUrl} -OutFile ${downloadPath}
                    if (-Not (Test-Path ${extractPath})) {
                        New-Item -ItemType Directory -Path ${extractPath}
                    }
                    Expand-Archive -Path ${downloadPath} -DestinationPath ${extractPath}
                    """
                }
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
