# Use the official Jenkins LTS (Long-Term Support) image as the base
FROM jenkins/jenkins:lts

# Switch to the root user to install additional tools
USER root

# Install Docker CLI
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get install -y docker-ce-cli && \
    rm -rf /var/lib/apt/lists/*

# Set the Jenkins home directory
ENV JENKINS_HOME /var/jenkins_home

# Expose the Jenkins default port
EXPOSE 8080

# Switch back to the Jenkins user
USER jenkins

# (Optional) Disable the setup wizard
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

# Define the default command to start Jenkins
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/jenkins.sh"]
