pipeline{
        agent any
        stages{
            stage('locate file'){
                steps{
                    sh "cd /home/azureuser/Driving_accompany/driving_accompany"
                }
            }
            stage('Run the test'){
                steps{
                    sh "python3 -m pytest"
                }
            }
            
        }
}