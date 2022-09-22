pipeline{
        agent any
        stages{
            stage('update'){
                steps{
                    sh "docker ps"
                    sh "$check = 5"
                }
            }

            stage('test'){
                steps{
                    sh "python3 -m pytest --cov=app"
                }
            }

            stage('Run the test'){
                steps{
                    sh "echo $check"
                }
            }            
        }
}