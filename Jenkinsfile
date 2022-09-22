pipeline{
        agent any
        environment{
            COMMIT_ID = "foo"
        }     

        stages{
            stage('update'){
                steps{
                    sh "docker ps"
                    sh "COMMIT_ID="chicken""
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