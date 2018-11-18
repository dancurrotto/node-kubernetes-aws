pipeline {
    agent any 
    
     environment {
                WORKSPACE=pwd()
                ETAG=''
    }
    stages {
        stage('Build'){
            steps{
                sh 'echo This build machine or docker container needs Kubectl, Kops, and aws cli installed.'
                sh 'echo This build machine has to have ssh keys generated using ssh-keygen -t rsa .'
                sh 'echo building...'
                git url: 'https://github.com/dcurrotto/node-jenkins-pl-ec2.git'
            }
        }
        stage('Deploy') {
            steps {
                
                sh 'echo $WORKSPACE'
                sh 'echo $AWS_ACCESS_KEY_ID'
                sh 'echo $PATH'   
                
                sh 'echo Tell kops where to find its config and state.'
                sh 'export KOPS_STATE_STORE=s3://valuesource-kubernetes'
                
                sh 'echo Configuring AWS...'
                sh '~/.local/bin/aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID'
                sh '~/.local/bin/aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY'
                sh '~/.local/bin/aws configure set region us-east-2'
                sh '~/.local/bin/aws configure set output json'                 
                
                sh 'kops get value-source-cloud.com > exists'
                
                //Set permissions on exists file.
                sh 'chmod 777 "$WORKSPACE/exists"'
                
                //Grab the value from exists.
                sh 'does_exist=$(head -1 $WORKSPACE/exists)'      
                sh 'echo $does_exist'
                
                
                sh 'echo Create the cluster.'
                //sh 'kops create cluster --name value-source-cloud.com --state s3://valuesource-kubernetes --zones us-east-2a --node-count=1 --yes'
               
               
               
                //Give it some time and then validate.  Do a loop or something similar.
                //kops validate cluster --name value-source-cloud.com --state s3://valuesource-kubernetes
            }
            
        }
    }
}