import jenkins

# Jenkins URL and credentials
JENKINS_URL = 'http://54.87.147.137:8080/'
USERNAME = 'admin'
PASSWORD = '11390f232fcee633ff7fc863ec99e41da1'
JOB_NAME = 

# Job definition XML
JOB_CONFIG = """
<flow-definition plugin="workflow-job@2.40">
  <actions/>
  <description>Sample Pipeline Job</description>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <definition class="org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition" plugin="workflow-cps@2.85">
    <scm class="hudson.plugins.git.GitSCM" plugin="git@4.0.0">
      <configVersion>2</configVersion>
      <userRemoteConfigs>
        <hudson.plugins.git.UserRemoteConfig>
          <url>https://github.com/omprakashbhanarkar19/jenkins_demo.git</url>
          <credentialsId>your-credentials-id</credentialsId>
        </hudson.plugins.git.UserRemoteConfig>
      </userRemoteConfigs>
      <branches>
        <hudson.plugins.git.BranchSpec>
          <name>*/main</name>
        </hudson.plugins.git.BranchSpec>
      </branches>
      <doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations>
      <extensions/>
    </scm>
    <scriptPath>Jenkinsfile</scriptPath>
    <lightweight>true</lightweight>
  </definition>
  <triggers/>
</flow-definition>
"""



# Function to create Jenkins pipeline job
def create_pipeline_job():
    server = jenkins.Jenkins(JENKINS_URL, username=USERNAME, password=PASSWORD)
    server.create_job(JOB_NAME, JOB_CONFIG)


# Function to enable the "GitHub hook trigger for GITScm polling"
def enable_github_webhook_trigger():
    server = jenkins.Jenkins(JENKINS_URL, username=USERNAME, password=PASSWORD)
    job_config_xml = server.get_job_config(JOB_NAME)

    # Parse job configuration XML
    root = ET.fromstring(job_config_xml)

    # Find and enable the GitHub webhook trigger
    properties = root.find('.//properties')
    github_trigger = ET.SubElement(properties, 'jenkins.triggers.SCMTriggerJobProperty')
    spec = ET.SubElement(github_trigger, 'spec')
    spec.text = '* * * * *'  # Example polling schedule (every minute)

    # Update the job with modified configuration
    updated_config_xml = ET.tostring(root, encoding='unicode')
    server.reconfig_job(JOB_NAME, updated_config_xml)

# Main function
def main():
    enable_github_webhook_trigger()


# Main function
def main():
    create_pipeline_job()

if __name__ == "__main__":
    main()
