pipeline {
    agent any 
    stages {
        stage('First step') {
            steps {
                echo 'Executing the first step.' 
            }
        }
        stage('Compile') {
            steps {
                echo 'Compile the source code.' 
            }
        }
        stage('Deploy file') {
            steps {
                sh '''
                    sudo su
                    sudo rm -rf /blog
                    sudo git clone https://github.com/viswc/Django-blog.git /blog
                    sudo chmod +x /blog/init.sh
                    sudo /blog/init.sh
                    echo 'Deploy the file to the server'
                '''
            }
        }
    }
}