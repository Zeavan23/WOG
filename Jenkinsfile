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

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\pip install --upgrade pip'
                bat '.venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Download geckodriver') {
            steps {
                powershell '''
                    $geckoDriverUrl = "https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-win64.zip"
                    $downloadPath = "C:\\Users\\nizar\\Downloads\\geckodriver.zip"
                    $extractPath = "C:\\Users\\nizar\\Downloads\\geckodriver"

                    Invoke-WebRequest -Uri $geckoDriverUrl -OutFile $downloadPath

                    If (-Not (Test-Path $extractPath)) {
                        New-Item -ItemType Directory -Path $extractPath
                    }

                    Expand-Archive -Path $downloadPath -DestinationPath $extractPath

                    $env:Path = "$env:Path;$extractPath"

                    Write-Output "geckodriver installé et ajouté au PATH avec succès."
                '''
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

        stage('Run') {
            steps {
                script {
                    bat 'docker-compose up -d'
                    bat 'timeout /t 10' // Attendre quelques secondes pour s'assurer que le service Flask est démarré
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests'
                script {
                    bat '.venv\\Scripts\\python.exe C:\\Users\\nizar\\PycharmProjects\\WOG\\test\\e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    bat 'docker-compose down'
                }
                echo 'Pipeline completed.'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up'
            script {
                bat 'docker-compose down'
            }
        }
        success {
            echo 'Pipeline succeeded.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
