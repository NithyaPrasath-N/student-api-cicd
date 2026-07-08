# 🚀 Production-Ready GitOps CI/CD Pipeline with Jenkins, Docker, SonarQube, Argo CD & Amazon EKS

## 📌 Project Overview

This project demonstrates a complete **Production-Style GitOps CI/CD Pipeline** that automatically builds, tests, analyzes, containerizes, and deploys a Flask application to **Amazon EKS** using **Jenkins**, **Docker**, **Argo CD**, and **GitOps** principles.

The pipeline is fully automated from **Git Push → Production Deployment**.

---

# 🏗️ Architecture

```
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Webhook
    │
    ▼
Jenkins Pipeline
    │
    ├── Checkout Source Code
    ├── Install Dependencies
    ├── Run Unit Tests
    ├── SonarQube Code Analysis
    ├── Build Docker Image
    ├── Push Docker Image to Docker Hub
    └── Update GitOps Repository
                    │
                    ▼
            GitHub (GitOps Repo)
                    │
                    ▼
                Argo CD
                    │
                    ▼
              Amazon EKS Cluster
                    │
                    ▼
          Kubernetes Rolling Update
                    │
                    ▼
            AWS Load Balancer
                    │
                    ▼
             Flask Application
```

---

# 🛠️ Technologies Used

- Python (Flask)
- PyTest
- Jenkins
- SonarQube
- Docker
- Docker Hub
- GitHub
- GitHub Webhooks
- GitOps
- Argo CD
- Kubernetes
- Amazon EKS
- AWS EC2
- ngrok

---

# 📁 Project Structure

```
student-api-cicd/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── sonar-project.properties
├── tests/
│     └── test_app.py
│
└── k8s/
      ├── deployment.yaml
      └── service.yaml
```

---

# ⚙️ CI/CD Pipeline Stages

## 1️⃣ Source Code Checkout

- Pulls latest code from GitHub.

---

## 2️⃣ Environment Verification

Verifies

- Python
- Git
- Docker
- Pip

---

## 3️⃣ Install Dependencies

Installs all required Python packages.

---

## 4️⃣ Unit Testing

Runs automated tests using **PyTest**.

---

## 5️⃣ SonarQube Analysis

Performs static code quality analysis.

---

## 6️⃣ Docker Build

Builds Docker Image

```
imnithii/student-api:<BUILD_NUMBER>
```

---

## 7️⃣ Docker Push

Pushes Docker Image to Docker Hub.

---

## 8️⃣ GitOps Repository Update

Jenkins automatically updates

```
k8s/deployment.yaml
```

with the newly built Docker image.

Example

```yaml
image: imnithii/student-api:24
```

---

## 9️⃣ Argo CD Deployment

Argo CD continuously watches the GitOps repository.

Whenever deployment.yaml changes,

Argo CD automatically performs a rolling update on Amazon EKS.

---

# 🔄 GitOps Workflow

```
Developer

↓

Git Push

↓

GitHub Webhook

↓

Jenkins

↓

Docker Build

↓

Docker Hub

↓

Update GitOps Repository

↓

Argo CD

↓

Amazon EKS

↓

Application Updated
```

---

# ☁️ Kubernetes Resources

- Deployment
- ReplicaSet
- Pods
- Service
- LoadBalancer

---

# 🐳 Docker

Image Repository

```
imnithii/student-api
```

Tagged using Jenkins Build Number.

Example

```
imnithii/student-api:24
```

---

# 🔥 Features

- Automated CI/CD Pipeline
- GitHub Webhook Integration
- Automated Unit Testing
- Static Code Analysis
- Docker Image Versioning
- GitOps Deployment
- Automatic Kubernetes Rolling Updates
- Continuous Deployment with Argo CD
- Production-style Deployment Workflow

---

# 📸 Screenshots

Include screenshots of

- Jenkins Pipeline
- SonarQube Dashboard
- Docker Hub Repository
- Argo CD Dashboard
- Kubernetes Pods
- Load Balancer
- Running Flask Application

---

# 🚀 How to Run

Clone Repository

```bash
git clone https://github.com/NithyaPrasath-N/student-api-cicd.git
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Flask App

```bash
python app.py
```

Run Tests

```bash
pytest
```

Build Docker Image

```bash
docker build -t student-api .
```

Run Docker Container

```bash
docker run -p 5000:5000 student-api
```

---

# 🎯 Future Enhancements

- Trivy Security Scanning
- Prometheus Monitoring
- Grafana Dashboards
- Horizontal Pod Autoscaler (HPA)
- NGINX Ingress Controller
- Argo Rollouts (Blue/Green Deployment)
- Slack Notifications
- AWS Secrets Manager Integration

---

# 📚 Key Learnings

- GitOps Workflow
- Kubernetes Deployments
- Docker Image Management
- CI/CD Automation
- Jenkins Pipelines
- GitHub Webhooks
- SonarQube Integration
- Amazon EKS
- Argo CD
- Rolling Updates
- Production Deployment Strategy

---

# 👨‍💻 Author

**Nithya Prasath**

Electronics and Communication Engineering

Cloud | DevOps | AWS | Kubernetes | Jenkins | Terraform | Docker | GitOps Enthusiast

GitHub:

https://github.com/NithyaPrasath-N
