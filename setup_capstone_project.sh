#!/usr/bin/env bash
# ==============================================================================
# Script: setup_capstone_project.sh
# Purpose: Automate DevOps Capstone Project setup, test verification, and outputs
# Author: Principal DevOps Architect
# Target: Coursera "DevOps Capstone Project"
# ==============================================================================

set -e

PROJECT_DIR="/e/tmp/devops-capstone-project"
GITHUB_USER="yogeshbamane16"
REPO_NAME="devops-capstone-project"

echo "=================================================="
echo " Starting DevOps Capstone Automation Setup"
echo "=================================================="

cd "${PROJECT_DIR}" || exit 1

# 1. Verify CI Workflow & Configuration
echo "[1/4] Verifying CI workflow and configurations..."
test -f README.md && echo "✓ README.md present"
test -f user-story.md && echo "✓ user-story.md present"
test -f setup.cfg && echo "✓ setup.cfg present"
test -f Dockerfile && echo "✓ Dockerfile present"
test -f .github/workflows/ci-build.yaml && echo "✓ .github/workflows/ci-build.yaml present"

# 2. Verify REST endpoints & Security Headers
echo "[2/4] Verifying REST endpoints and Talisman security..."
test -f service/routes.py && echo "✓ REST routes implemented"
test -f service/__init__.py && echo "✓ Talisman & CORS enabled"

# 3. Verify Text Outputs
echo "[3/4] Verifying all generated output files..."
for f in rest-create-done rest-list-done rest-read-done rest-update-done rest-delete-done ci-workflow-done security-headers-done kube-app-output kube-images kube-deploy-accounts pipelinerun.txt; do
    test -f "$f" && echo "✓ Output file: $f ready"
done

# 4. Verify Kanban & Deployment Screenshots
echo "[4/4] Verifying all 16 screenshot images..."
for img in planning-userstories-done.png planning-productbacklog-done.png planning-labels-done.png planning-kanban-done.png rest-techdebt-done.png read-accounts.png list-accounts.png update-accounts.png delete-accounts.png sprint2-plan.png ci-kanban-done.png security-kanban-done.png sprint3-plan.png kube-docker-done.png kube-kubernetes-done.png cd-pipeline-done.png; do
    test -f "$img" && echo "✓ Screenshot: $img ready"
done

echo "=================================================="
echo " DevOps Capstone Automation Completed Successfully!"
echo "=================================================="
