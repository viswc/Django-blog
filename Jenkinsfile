pipeline {
    agent any 
    stages {
        stage('First step') {
            steps {
                echo 'Run the static analysis to the code' 
            }
        }
        stage('Compile') {
            steps {
                echo 'Compile the source code' 
            }
        }
        stage('Deploy file') {
            steps {
                sh '''
                    sudo git clone https://github.com/viswc/Django-blog.git /blog
                    sudo chmod +x /blog/init.sh
                    /blog/init.sh
                '''
            }
        }
    }
}