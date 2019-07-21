# Birthday Application

Its Python Flask microservice REST application for demo.

# For local building & test Birthday Application:
Run the following command from the source code root directory
  
  ```
  $ docker build -t bday .
  $ docker run --rm --name=bday -d -p 80:80 bday
  ```
# Docker Hub Image

Application image is deployed on docker hub : https://hub.docker.com/r/anandnevase/bday

Using this image you can start using this application on docker/kubernetes/openshift infra.

To run app on docker, used following command
  ```
  $ docker run --name=bday -p 80:80 -d -v /database:/bday-app/database:z anandnevase/bday
  ```
# Application Deployment using Ansible

Run following ansible command to deployment on Remote linux machine:
```
  $ ansible-playbook -i ",<VM-hostname>" deployment-playbook.yml -u ec2-user --key-file=/tmp/key.pem
```
# Application Deployment on Kubernetes using kubectl & Helm

Run following ansible command to deployment on Remote linux machine
```
  $ kubectl create ns bday
```
For install app using helm
```
  $ sudo helm install --name bday-app ./k8s-deployment/bday-app --namespace bday-app
```
For Upgrading app using helm
```
  $ sudo helm upgrade --wait bday-app ./k8s-deployment/bday-app --namespace bday-app
```

# CI-CD - Using helm on Kubernetes

For building jenkins CI/CD, import __jenkinsfile-k8s__  in Jenkin. 

Following prerequisites required for jenkins build:
- Kubenetes Cluster
- helm & kubectl configure with Kubenetes Cluster

Following software required:
- Docker : Application is bundle in docker_image and same is used for test and production.
- Ansible: Required to deploy application AWS.
- Inspec: Inspec is used for REST API Automation testing.
- kubectl: Kubectl required to connect to k8s server
- helm: Helm is required to install/upgrade application on kubenetes 

Sample Pipeline:
![Alt text](ci-cd-pipeline-k8s.PNG?raw=true)

# CI-CD - Using Ansible on AWS

For building jenkins CI/CD, import __jenkinsfile__  in Jenkin. 

Following prerequisites required for jenkins build:
- EC2 Instance
- EC2 instance PEM key

Following software required:
- Docker : Application is bundle in docker_image and same is used for test and production.
- Ansible: Required to deploy application AWS.
- Inspec: Inspec is used for REST API Automation testing.

Sample Pipeline:
![Alt text](ci-cd-pipeline.PNG?raw=true)

# System Diagram

Currently this application is deployed on AWS EC2 as docker container. But same can be extend or deployed to Kubernetes/Openshift.

![Alt text](system-diagram.png?raw=true)
