pipeline{
        agent any
        environment{
            COMMIT_ID = "foo"
        }     

        stages{

            stage('test'){
                steps{
                    sh "python3 -m pytest --cov=app"
                }
            }

            stage('Deploy'){
                steps{
                    sh "cd driving_accompany && python3 app.py"
                }
            }            
        }
}