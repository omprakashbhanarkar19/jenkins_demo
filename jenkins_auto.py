import jenkins

# Jenkins URL and credentials
JENKINS_URL = 'http://your-jenkins-url'
USERNAME = 'your-username'
PASSWORD = 'your-password'

# Function to create Jenkins pipeline job
def create_pipeline_job():
    server = jenkins.Jenkins(JENKINS_URL, username=USERNAME, password=PASSWORD)
    server.create_job('SamplePipelineJob', JOB_CONFIG)

# Main function
def main():
    create_pipeline_job()

if __name__ == "__main__":
    main()
