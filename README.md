# DevOps Capstone Project

[![Build Status](https://github.com/yogeshbamane16/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/yogeshbamane16/devops-capstone-project/actions)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](https://shields.io/)

This repository contains the capstone project implementation for the **IBM DevOps and Software Engineering Professional Certificate**.

## Project Overview
This project demonstrates complete end-to-end DevOps practices:
- **Agile Planning & Scrum:** User stories and backlog grooming on Kanban board.
- **TDD (Test-Driven Development):** High code coverage unit testing with `nosetests` and `coverage`.
- **Security & CORS:** Flask Talisman security headers and cross-origin resource sharing policies.
- **CI Pipeline:** Automated build, linting (`flake8`), and testing using GitHub Actions.
- **Containerization:** Multi-stage Docker image build exposed on port 8080.
- **Kubernetes Deployment:** Declarative manifests deployed to Kubernetes/OpenShift.
- **Tekton CD Pipeline:** Cloud-native continuous delivery automation.

## Project Structure
- `service/`: Flask application models and REST routes (`/accounts`).
- `tests/`: TDD test suite for models and REST endpoints.
- `deploy/`: Kubernetes deployment, service, and ingress manifests.
- `tekton/`: Tekton CD tasks, pipeline, and pipelinerun definitions.
- `.github/workflows/ci-build.yaml`: GitHub Actions CI workflow.

---
© IBM Corporation 2026. All rights reserved.
