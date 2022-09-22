pipeline{
        agent any
        stages{
            stage('update'){
                steps{
                    sh "git pull"
                }
            }

            stage('test'){
                steps{
                    sh "cd driving_accompany && python3 -m pytest --cov=app"
                }
            }

            stage('Run the test'){
                steps{
                    sh "echo 'test1'"
                    sh "echo 'test2'"
                }
            }
            
        }
}