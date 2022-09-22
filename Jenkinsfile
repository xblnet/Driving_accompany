pipeline{
        agent any
        environment{
            COMMIT_ID = "foo"
        }     

        stages{
            stage('update'){
                steps{
                    sh "COMMIT_ID=docker ps"
                }
            }

            stage('test'){
                steps{
                    sh "python3 -m pytest --cov=app"
                }
            }

            stage('Deploy'){
                steps{
                    sh "echo $COMMIT_ID"
                }
            }            
        }
}