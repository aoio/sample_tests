pipeline {
    agent { docker { image 'python:2.7.12' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                sh 'python test.py'
            }
        }
    }
    }
}
