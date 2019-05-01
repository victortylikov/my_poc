pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'Start tests'
        sh 'pytest -v'
      }
    }
  }
}
