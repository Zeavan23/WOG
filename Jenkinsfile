pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build('my-flask-app')
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    docker.image('my-flask-app').run('-p 5000:5000 --name my-app')
                }
            }
        }
    }
}
