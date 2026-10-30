pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Install & Test') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                pytest -v
                '''
            }
        }
        stage('Docker Build') {
            steps { sh 'docker build -t hello-mlops:1.0 .' }
        }
        stage('Docker Run') {
            steps { sh 'docker run --rm hello-mlops:1.0' }
        }
    }
    post {
        success { echo 'PIPELINE PASSED' }
        failure { echo 'PIPELINE FAILED' }
    }
}