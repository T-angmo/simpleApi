pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t api-image .'
                    sh 'docker push your-registry/api-image'
                }
            }
        }
        stage('Unit Test') {
            steps {
                sh 'python -m unittest discover -s tests'
            }
        }
        stage('Deploy to Test') {
            steps {
                script {
                    sh 'ssh user@test-server "docker run -d -p 5000:5000 api-image"'
                }
            }
        }
        stage('Run Robot Tests') {
            steps {
                git 'https://github.com/your-robot-test-repo.git'
                sh 'robot robot_tests'
            }
        }
        stage('Deploy to Pre-Prod') {
            steps {
                script {
                    sh 'ssh user@pre-prod-server "docker run -d -p 5000:5000 api-image"'
                }
            }
        }
    }
}
