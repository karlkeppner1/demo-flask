pipeline {
  agent any
  environment {
    SSH_KEY = credentials('flask-ec2-instance')
    IP_ADDR = '54.81.11.214'
  }
  stages {
    stage('deploy') {
      steps {
        sh 'echo "Hello World"'
        sh 'scp -o StrictHostKeyChecking=no -i $SSH_KEY api.py $SSH_KEY_USR@$IP_ADDR://home/ec2-user/api.py'
        // sh 'ssh -o StrictHostKeyChecking=no -i $SSH_KEY $SSH_KEY_USR@$IP_ADDR "python3 api.py"'
      }
    }
  }
}