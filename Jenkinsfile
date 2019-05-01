pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'Start tests'
        sh 'cd /Users/viktortyulikov/my_poc/bin;source activate;'
        sh 'cd /Users/viktortyulikov/PycharmProjects/prototype/my_poc; pwd; pytest -v'
      }
    }
  }
}
