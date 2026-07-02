# 🚀 Azure DevOps Notes

A beginner-friendly guide to understanding **DevOps**, **CI/CD**, and **Azure DevOps Pipelines**.

---

# 📚 Table of Contents

- What is DevOps?
- Traditional Software Development vs DevOps
- Azure DevOps Overview
- What is CI/CD?
- Continuous Integration (CI)
- Continuous Delivery (CD)
- Continuous Deployment
- CI vs Continuous Delivery vs Continuous Deployment
- What is a CI/CD Pipeline?
- Benefits of CI/CD Pipelines
- Azure DevOps CI/CD Workflow
- Key Takeaways

---

# 🚀 What is DevOps?

DevOps is formed by combining two terms:

- **Dev** → Development
- **Ops** → Operations

DevOps is a culture, methodology, and collection of tools that encourage Development and Operations teams to collaborate throughout the Software Development Life Cycle (SDLC).

Rather than working separately, both teams work together to build, test, deploy, monitor, and maintain applications efficiently and continuously.

---

# 🎯 Objectives of DevOps

- Deliver software more quickly
- Strengthen collaboration between teams
- Automate repetitive processes
- Reduce deployment failures
- Improve software quality
- Enable continuous monitoring and feedback
- Deliver customer value more frequently

---

# 🔄 Traditional Software Development vs DevOps

## Traditional Software Development

```
Developer writes code
        │
        ▼
Testing Team performs manual testing
        │
        ▼
Operations Team deploys application
        │
        ▼
Issues appear in Production
        │
        ▼
Developer fixes defects
        │
        ▼
Repeat
```

### Challenges

- ❌ Manual deployments
- ❌ Slow software releases
- ❌ Communication gaps between teams
- ❌ Higher possibility of human errors
- ❌ Difficult rollback process
- ❌ Delayed feedback

---

## DevOps Workflow

```
Developer writes code
        │
        ▼
Push Code to Git Repository
        │
        ▼
CI Pipeline
(Build + Test)
        │
        ▼
CD Pipeline
(Deploy)
        │
        ▼
Application
        │
        ▼
Monitoring
        │
        ▼
Feedback
        │
        ▼
Next Release
```

### Benefits

- ✅ Automated deployments
- ✅ Faster software releases
- ✅ Better collaboration
- ✅ Continuous feedback
- ✅ Improved software quality
- ✅ Reliable deployment process

---

# ☁️ Azure DevOps Overview

Azure DevOps is Microsoft's cloud-based DevOps platform that provides services for planning, developing, testing, deploying, and monitoring software applications.

It supports the complete software development lifecycle using integrated DevOps services.

---

# Azure DevOps Services

| Service | Purpose |
|----------|---------|
| Azure Boards | Agile Planning and Work Item Tracking |
| Azure Repos | Git-based Source Code Repository |
| Azure Pipelines | Build and Release Automation |
| Azure Test Plans | Manual and Exploratory Testing |
| Azure Artifacts | Package and Dependency Management |

---

# Azure DevOps Workflow

```
Azure Boards
      │
      ▼
Developer selects User Story
      │
      ▼
Develops Code
      │
      ▼
Pushes Code to Azure Repos
      │
      ▼
Azure Pipelines Triggered
      │
      ├── Build
      ├── Unit Testing
      ├── Code Analysis
      ├── Package Artifact
      ▼
Deploy to Development
      │
      ▼
Deploy to Testing
      │
      ▼
Deploy to Staging
      │
      ▼
Deploy to Production
```

---

# 🔁 What is CI/CD?

CI/CD stands for:

- **CI** → Continuous Integration
- **CD** → Continuous Delivery / Continuous Deployment

CI/CD is a DevOps practice that automates the process of building, testing, packaging, and deploying applications.

This enables organizations to release software more frequently, reliably, and efficiently.

---

# ⚙️ Continuous Integration (CI)

Continuous Integration is the practice of frequently integrating code changes into a shared repository.

Whenever a developer commits or pushes code, an automated pipeline is triggered.

---

## CI Workflow

```
Developer commits code
        │
        ▼
Azure Repos
        │
        ▼
Pipeline Triggered
        │
        ├── Restore Dependencies
        ├── Compile Code
        ├── Execute Unit Tests
        ├── Perform Code Quality Checks
        ▼
Generate Build Artifact
```

### Benefits of Continuous Integration

- Early bug detection
- Automated build process
- Automated testing
- Faster developer feedback
- Improved code quality
- Better collaboration

---

# 🚀 Continuous Delivery (CD)

Continuous Delivery ensures that applications are always ready for deployment.

The application is automatically deployed to multiple environments such as:

- Development
- Testing
- Staging

Before Production deployment, manual approval is usually required.

---

## Workflow

```
Successful Build
        │
        ▼
Deploy to Development
        │
        ▼
Execute Tests
        │
        ▼
Deploy to Testing
        │
        ▼
Approval
        │
        ▼
Deploy to Production
```

---

# ⚡ Continuous Deployment

Continuous Deployment extends Continuous Delivery by automatically deploying every successful build directly to Production.

No manual approval is required once all automated tests pass.

---

## Workflow

```
Commit Code
      │
      ▼
Build
      │
      ▼
Test
      │
      ▼
Deploy to Production
```

---

# 📊 CI vs Continuous Delivery vs Continuous Deployment

| Feature | CI | Continuous Delivery | Continuous Deployment |
|----------|:--:|:------------------:|:---------------------:|
| Build Automation | ✅ | ✅ | ✅ |
| Automated Testing | ✅ | ✅ | ✅ |
| Deploy to Test Environment | ❌ | ✅ | ✅ |
| Manual Approval | ❌ | ✅ | ❌ |
| Automatic Production Deployment | ❌ | ❌ | ✅ |

---

# 🔧 What is a CI/CD Pipeline?

A CI/CD Pipeline is a sequence of automated stages that converts source code into a deployed application.

Instead of manually executing each task, Azure Pipelines automates the complete software delivery process.

---

## Pipeline Flow

```
Source Code
      │
      ▼
Build
      │
      ▼
Unit Testing
      │
      ▼
Static Code Analysis
      │
      ▼
Package Artifact
      │
      ▼
Deploy to Development
      │
      ▼
Deploy to Testing
      │
      ▼
Approval
      │
      ▼
Deploy to Production
```

---

# 🌟 Benefits of CI/CD Pipelines

## 🚀 Faster Software Delivery

Automates the release process, enabling quicker and more frequent deployments.

---

## 🐞 Early Bug Detection

Builds and tests are automatically executed after every code commit, helping identify defects at an early stage.

---

## 🤖 Reduced Human Errors

Automation minimizes manual intervention and ensures consistent deployment processes.

---

## ✅ Improved Code Quality

Only code that successfully passes all automated tests and quality checks progresses to the next stage.

---

## ⚡ Faster Feedback

Developers receive immediate feedback on build failures and test results.

---

## 🔄 Consistent Deployments

The same deployment workflow is used across all environments:

- Development
- Testing
- Staging
- Production

This reduces environment-specific deployment issues.

---

## 🤝 Better Collaboration

Developers, Testers, and Operations teams collaborate using a unified automated workflow.

---

## 🔙 Easier Rollbacks

If deployment issues occur, previous stable versions can be restored quickly.

---

## 📈 Higher Productivity

Automation reduces manual effort, allowing engineers to focus more on development and innovation.

---

## 🚀 Reliable Releases

Smaller and more frequent deployments reduce deployment risks and improve customer satisfaction.

---

# ☁️ Azure DevOps CI/CD Workflow

```
Developer
     │
     ▼
Azure Repos
     │
     ▼
Azure Pipelines
     │
     ├── Restore Packages
     ├── Build
     ├── Execute Unit Tests
     ├── Code Analysis
     ├── Generate Build Artifact
     ▼
Development Environment
     │
     ▼
QA Testing
     │
     ▼
Approval
     │
     ▼
Production
     │
     ▼
Monitoring & Feedback
```

---

# 🎯 Key Takeaways

- DevOps is a culture that brings Development and Operations teams together.
- Azure DevOps offers an end-to-end platform for planning, coding, testing, building, and deploying applications.
- Continuous Integration (CI) automates code building and testing whenever new code is committed.
- Continuous Delivery (CD) keeps applications deployment-ready, usually with approval before production deployment.
- Continuous Deployment automatically deploys validated code directly to production.
- CI/CD Pipelines automate software delivery, reduce manual effort, improve software quality, and enable faster, more reliable releases.

---

# 📌 Summary

**DevOps + Azure DevOps + CI/CD = Faster Software Development + Better Team Collaboration + Reliable Deployments + High-Quality Software**