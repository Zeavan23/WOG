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

        stage('Download geckodriver') {
            steps {
                powershell """
                \$geckoDriverUrl = 'https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-win64.zip'
                \$downloadPath = 'C:\\ProgramData\\Jenkins\\geckodriver.zip'
                \$extractPath = 'C:\\ProgramData\\Jenkins\\geckodriver'

                Invoke-WebRequest -Uri \$geckoDriverUrl -OutFile \$downloadPath
                If (-Not (Test-Path \$extractPath)) {
                    New-Item -ItemType Directory -Path \$extractPath
                }
                Expand-Archive -Path \$downloadPath -DestinationPath \$extractPath -Force
                \$env:Path += ';' + \$extractPath
                Write-Output "geckodriver installed and added to PATH."
                """
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


