pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t api-image .'
                    sh 'docker tag api-image kowmungai/api-image:latest'
                }
            }
        }
        stage('Unit Test') {
            steps {
                sh 'docker run --rm api-image python -m unittest unit_test.py'
            }
        }
        stage('Deploy to Test') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 api-image'
                }
            }
        }
        stage('Run Robot Tests') {
            steps {
                git branch: 'main', url: 'https://github.com/KowMunGai/robotTest.git'
                sh 'robot robotTest.robot'
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
