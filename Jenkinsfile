pipeline {
    agent any 
    stages {
        stage('Clone step') {
            steps {
                sh '''
                    sudo su
                    sudo rm -rf /blog
                    sudo git clone https://github.com/viswc/Django-blog.git /blog
                    sudo chmod +x /blog/init.sh
                '''
            }
        }
        stage('Deploy script') {
            steps {
                sh '''
                    sudo su
                    sudo /blog/init.sh
                    echo 'Deployed successfully!!'
                '''
            }
        }
    }
}