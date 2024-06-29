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

        stage('Download and Setup Chrome and ChromeDriver') {
            steps {
                script {
                    def chromeUrl = 'https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/win64/chrome-win64.zip'
                    def chromeDriverUrl = 'https://storage.googleapis.com/chromium-browser-snapshots/Win/126.0.6478.126/chromedriver_win32.zip'
                    def downloadDir = "${pwd()}/downloads"
                    def extractDir = "${pwd()}/chrome"

                    bat "powershell -Command \"if (!(Test-Path -Path ${downloadDir})) { New-Item -ItemType Directory -Path ${downloadDir} }\""
                    bat "powershell -Command \"Invoke-WebRequest -Uri ${chromeUrl} -OutFile ${downloadDir}/chrome-win64.zip\""
                    bat "powershell -Command \"Expand-Archive -Path ${downloadDir}/chrome-win64.zip -DestinationPath ${extractDir} -Force\""

                    bat "powershell -Command \"Invoke-WebRequest -Uri ${chromeDriverUrl} -OutFile ${downloadDir}/chromedriver_win32.zip\""
                    bat "powershell -Command \"Expand-Archive -Path ${downloadDir}/chromedriver_win32.zip -DestinationPath ${extractDir} -Force\""

                    bat "setx PATH \"%PATH%;${extractDir}\\chrome-win64\\chrome-win64;${extractDir}\\chromedriver_win32\""
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

