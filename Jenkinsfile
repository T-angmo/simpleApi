pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    sh 'docker kill $(docker ps -q) || true'
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
                sh 'docker network create my_network || true'
                sh 'docker run -d --network my_network --name api-container -p 5000:5000 api-image'
            }
        }
        stage('Run Robot Tests') {
            steps {
                git branch: 'main', url: 'https://github.com/KowMunGai/robotTest.git'
                sh 'docker run --rm --network my_network -v /var/lib/jenkins/workspace/simpleApi:/tests api-image robot /tests/robotTest.robot'
            }
        }
        stage('Deploy to Pre-Prod') {
            steps {
                script {
                    sh 'docker run -d -p 5001:5000 api-image'
                }
            }
        }
    }

    post {
        always {
            sh 'docker stop api-container || true'
            sh 'docker rm api-container || true'
        }
    }
}
