pipeline {
    agent any
    environment {
        DOCKER_USER = 'baptistamarcelo'
        IMAGE_NAME = 'teste-cicd'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_USER}/${IMAGE_NAME}:latest ."
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-key', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER_CRED')]) {
                        sh "echo \$DOCKER_PASS | docker login -u \$DOCKER_USER_CRED --password-stdin"
                        sh "docker push ${DOCKER_USER}/${IMAGE_NAME}:latest"
                    }
                }
            }
        }
        stage('Deploy Local') {
            steps {
                sh "docker stop my-running-app || true"
                sh "docker rm my-running-app || true"
                sh "docker run -d --name my-running-app ${DOCKER_USER}/${IMAGE_NAME}:latest"
            }
        }
    }
}