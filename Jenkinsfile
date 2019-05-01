pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'Start tests'
        sh 'cd /Users/viktortyulikov/PycharmProjects/prototype/my_poc; pytest -v'
      }
    }
  }
}
