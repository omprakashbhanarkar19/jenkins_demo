
# Define provider
provider "jenkins" {
  url     = "http://54.87.147.137:8080/"
  username = "admin"
  password = "11390f232fcee633ff7fc863ec99e41da1"
}

# Create Jenkins job
resource "jenkins_job" "pipeline_job" {
  name     = "sample_pipeline"
  pipeline = <<EOF
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                // Your build steps here
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Your test steps here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Your deployment steps here
            }
        }
    }
}
EOF
}

# Create Jenkins job GitHub webhook
resource "jenkins_job_webhook" "github_webhook" {
  job_name = jenkins_job.pipeline_job.name
  endpoint = "http://54.87.147.137:8080/github-webhook/"
  source   = "github"
  secret   = "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"
}
