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

            stage('Run the test'){
                steps{
                    sh "echo $COMMIT_ID"
                }
            }            
        }
}