# Use a base image with Python
FROM python:3.9-slim

# Install Ansible and Kubernetes collection
RUN pip install ansible
RUN ansible-galaxy collection install community.kubernetes

# Set the working directory
WORKDIR /ansible

# Command to keep the container running
CMD ["sleep", "infinity"]
