import jenkins

# Jenkins URL and credentials
JENKINS_URL = 'http://54.87.147.137:8080/'
USERNAME = 'admin'
PASSWORD = '11390f232fcee633ff7fc863ec99e41da1'
JOB_NAME = 'sample_job'

# Job definition XML
JOB_CONFIG = """
<flow-definition plugin="workflow-job@2.40">
  <actions/>
  <description>Sample Pipeline Job</description>
  <keepDependencies>false</keepDependencies>
  <properties>
    <pipelineTriggers>
      <triggers class="vector">
        <jenkins.triggers.SCMTrigger>
          <spec></spec>
          <ignorePostCommitHooks>True</ignorePostCommitHooks>
        </jenkins.triggers.SCMTrigger>
        <org.jenkinsci.plugins.gitea.GiteaPushTrigger plugin="gitea@1.2.0">
          <spec></spec>
          <triggerOnEvents>
            <org.jenkinsci.plugins.gitea.push.PushEvent/>
          </triggerOnEvents>
        </org.jenkinsci.plugins.gitea.GiteaPushTrigger>
      </triggers>
    </pipelineTriggers>
  </properties>
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


# Main function
def main():
    create_pipeline_job()

if __name__ == "__main__":
    main()
