pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'Start tests'
        sh 'cd /Users/viktortyulikov/PycharmProjects/prototype/my_poc;pwd; python -m pytest -v'
      }
    }
  }
}
