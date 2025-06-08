pipeline {
    agent any

    environment {
        IMAGE_NAME = "gigamind/flask-api"
    }

    stages {

        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Lint inside Docker Image') {
            steps {
                sh 'docker run --rm $IMAGE_NAME flake8 app/'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push $IMAGE_NAME
                    '''
                }
            }
        }

        stage('Deploy to Production Server') {
            steps {
                sshagent (credentials: ['prod-server-ssh']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@your-server-ip '
                    cd /opt/flask-api &&
                    docker compose pull &&
                    docker compose up -d'
                    '''
                }
            }
        }
    }
}
