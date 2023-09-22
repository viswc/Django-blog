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
                    sudo su
                    sudo git clone https://github.com/viswc/Django-blog.git /blog
                    sudo chmod +x /blog/init.sh
                    sudo /blog/init.sh
                    echo 'Deploy the file to the server'
                '''
            }
        }
    }
}