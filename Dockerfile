FROM jenkins/jenkins:lts

USER root

# ---------------------------------------------------------
# Install Python3, pip, venv, curl, unzip, and Java (for Allure)
# ---------------------------------------------------------
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    unzip \
    default-jre \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------------------------------------
# Install Allure CLI
# ---------------------------------------------------------
RUN curl -o allure.zip -L \
    https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.24.0/allure-commandline-2.24.0.zip \
    && unzip allure.zip -d /opt/allure \
    && ln -s /opt/allure/allure-2.24.0/bin/allure /usr/bin/allure \
    && rm allure.zip

# Allow Jenkins to run Docker commands (optional)
RUN usermod -aG docker jenkins

# Switch back to Jenkins user
USER jenkins