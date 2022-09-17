pipeline{
        agent any
        stages{
            stage('Build for docker image'){
                steps{
                    sh "git pull"
                    sh "docker build"
                }
            }
            stage('Test python flask APP'){
                steps{
                    sh "cd /tests"
                    sh "python3 -m pytest --cov"
                }
            }
            stage('Deployment image with APP'){
                steps{
                    sh "sudo docker-compose up -d --build"
                }
            }
            
        }
}