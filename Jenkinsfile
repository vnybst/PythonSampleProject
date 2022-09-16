pipeline {
    agent {
        docker{
            image 'registry.amarulasolutions.com:443/account-creater-docker:alpha'
            args '-u root --privileged'
        }
    }
    stages {
        stage('Build') {
            steps {
               sh 'python3 test.py'
            }
        }
    }
}