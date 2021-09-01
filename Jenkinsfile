pipeline {
    environment {
        registry = "maxitosh/devops"
        app_dir = "app_python"
    }

    agent {
        docker {
            image 'python:3.9.6-alpine3.14'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install packages') {
            steps {
                sh 'apk add gcc musl-dev'
            }
        }

        stage('Install Dependencies') {
            steps {
                withPythonEnv('python') {
                    sh 'pip install -r $app_dir/requirements.txt'
                }
            }
        }

        stage('Linting and Testing') {
            steps {
                parallel (
                    'linting': {
                        withPythonEnv('python') {
                            sh 'flake8 $app_dir'
                        }
                    },
                    'unit testing': {
                        withPythonEnv('python') {
                            sh 'pytest $app_dir/tests'
                        }
                    }
                )
            }
        }

        stage('Build and Deploy') {
            steps {
                dir("${app_dir}") {
                    script {
                        def dockerImage = docker.build('$registry:jenkins_ci-$BUILD_NUMBER')
                        docker.withRegistry('', 'dockerhub') {
                            dockerImage.push()
                        }
                    }
                }
            }
        }

        stage('Cleaning up') {
            steps {
                sh "docker rmi $registry:jenkins_ci-$BUILD_NUMBER"
            }
        }
    }
}
