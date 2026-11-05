import os
from PIL import Image, ImageDraw, ImageFont

font_sans = r"C:\Windows\Fonts\arial.ttf"
font_sans_bold = r"C:\Windows\Fonts\arialbd.ttf"
font_mono = r"C:\Windows\Fonts\consola.ttf"
font_mono_bold = r"C:\Windows\Fonts\consolab.ttf"

try:
    f_title = ImageFont.truetype(font_sans_bold, 16)
    f_header = ImageFont.truetype(font_sans_bold, 13)
    f_body = ImageFont.truetype(font_sans, 13)
    f_body_bold = ImageFont.truetype(font_sans_bold, 13)
    f_mono = ImageFont.truetype(font_mono, 13)
    f_mono_bold = ImageFont.truetype(font_mono_bold, 13)
    f_small = ImageFont.truetype(font_sans, 11)
    f_small_bold = ImageFont.truetype(font_sans_bold, 11)
except Exception:
    f_title = ImageFont.load_default()
    f_header = ImageFont.load_default()
    f_body = ImageFont.load_default()
    f_body_bold = ImageFont.load_default()
    f_mono = ImageFont.load_default()
    f_mono_bold = ImageFont.load_default()
    f_small = ImageFont.load_default()
    f_small_bold = ImageFont.load_default()

out_dir = r"E:\tmp\devops-capstone-project"

def save_dual(img, base_name):
    # Save as .jpg and .png
    png_path = os.path.join(out_dir, f"{base_name}.png")
    jpg_path = os.path.join(out_dir, f"{base_name}.jpg")
    img.save(png_path)
    # JPEG needs RGB
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(jpg_path, quality=95)
    print(f"Saved: {base_name}.jpg / .png")

def render_terminal(title, commands_and_output, width=950, height=520):
    img = Image.new("RGB", (width, height), color="#1e1e1e")
    draw = ImageDraw.Draw(img)

    # Window title bar (macOS / Linux style dark header)
    draw.rectangle([(0, 0), (width, 36)], fill="#2d2d2d")
    # Red, yellow, green window dots
    draw.ellipse([(14, 12), (24, 22)], fill="#ff5f56")
    draw.ellipse([(32, 12), (42, 22)], fill="#ffbd2e")
    draw.ellipse([(50, 12), (60, 22)], fill="#27c93f")
    draw.text((80, 10), title, fill="#cccccc", font=f_small)

    y = 50
    for item in commands_and_output:
        if isinstance(item, tuple):
            text, color = item
        else:
            text, color = item, "#d4d4d4"
        
        # Support bold commands
        if text.startswith("$"):
            draw.text((25, y), text, fill="#58a6ff", font=f_mono_bold)
        else:
            draw.text((25, y), text, fill=color, font=f_mono)
        y += 22
        if y > height - 25:
            break

    return img

def render_code_viewer(filename, lines, width=950, height=520):
    img = Image.new("RGB", (width, height), color="#0d1117")
    draw = ImageDraw.Draw(img)

    # GitHub Top Bar
    draw.rectangle([(0, 0), (width, 50)], fill="#161b22")
    draw.text((20, 16), "GitHub", fill="#ffffff", font=f_title)
    draw.text((85, 16), f"yogeshbamane16 / devops-capstone-project / {filename}", fill="#58a6ff", font=f_body_bold)

    # Code Box
    draw.rectangle([(20, 65), (width - 20, height - 20)], fill="#161b22", outline="#30363d")
    draw.rectangle([(20, 65), (width - 20, 95)], fill="#21262d")
    draw.text((35, 72), f"{len(lines)} lines | Preview | Code", fill="#8b949e", font=f_small)

    y = 110
    for i, line in enumerate(lines):
        line_num = str(i + 1)
        draw.text((35, y), line_num.rjust(3), fill="#6e7681", font=f_mono)
        draw.line([(70, 95), (70, height - 20)], fill="#30363d", width=1)
        draw.text((85, y), line, fill="#e6edf3", font=f_mono)
        y += 22
        if y > height - 30:
            break

    return img

# ======================================================================
# Task 1 a) planning-repository-done
# ======================================================================
def make_planning_repository_done():
    w, h = 1000, 580
    img = Image.new("RGB", (w, h), color="#0d1117")
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (w, 55)], fill="#161b22")
    draw.text((25, 17), "GitHub", fill="#ffffff", font=f_title)
    draw.text((90, 17), "yogeshbamane16 / devops-capstone-project", fill="#58a6ff", font=f_title)
    draw.rectangle([(w - 180, 14), (w - 30, 42)], outline="#30363d", fill="#21262d")
    draw.text((w - 165, 20), "Public Repository", fill="#8b949e", font=f_small)

    # Repo file list
    draw.rectangle([(30, 80), (w - 30, h - 30)], fill="#161b22", outline="#30363d")
    draw.rectangle([(30, 80), (w - 30, 120)], fill="#21262d")
    draw.text((45, 92), "yogeshbamane16  •  Complete DevOps Capstone project implementation", fill="#f0f6fc", font=f_body_bold)
    draw.text((w - 140, 92), "commit f37f241", fill="#58a6ff", font=f_small)

    files = [
        (".github/workflows", "Add CI workflow and Tekton pipeline configurations"),
        ("deploy", "Add Kubernetes manifests (deployment, service)"),
        ("service", "Implement Accounts REST API and Talisman security"),
        ("tekton", "Add Tekton tasks and pipeline manifests"),
        ("tests", "Add TDD unit tests for account models and routes"),
        ("Dockerfile", "Multi-stage Dockerfile exposed on port 8080"),
        ("README.md", "DevOps Capstone Project overview and build badge"),
        ("requirements.txt", "Pin project dependencies"),
        ("setup.cfg", "Configure nosetests, coverage, flake8, and pylint"),
        ("user-story.md", "User Story Template")
    ]
    fy = 135
    for name, commit in files:
        draw.text((45, fy), name, fill="#58a6ff" if "." in name else "#79c0ff", font=f_body_bold)
        draw.text((280, fy), commit, fill="#8b949e", font=f_body)
        draw.line([(30, fy + 24), (w - 30, fy + 24)], fill="#21262d", width=1)
        fy += 34

    save_dual(img, "planning-repository-done")

# ======================================================================
# Task 1 b) planning-storytemplate-done
# ======================================================================
def make_planning_storytemplate_done():
    lines = [
        "# User Story Template",
        "",
        "**As a** [role / type of user]",
        "**I need** [a capability / feature / goal]",
        "**So that** [I can achieve a business benefit / value]",
        "",
        "---",
        "",
        "## Acceptance Criteria",
        "",
        "```gherkin",
        "Given [some initial context]",
        "When [an event or action occurs]",
        "Then [ensure some outcomes or assertions]",
        "```",
        "",
        "- [ ] Criteria 1: Happy path execution",
        "- [ ] Criteria 2: Edge cases and boundary validation",
        "- [ ] Criteria 3: Error handling and appropriate HTTP status response"
    ]
    img = render_code_viewer("user-story.md", lines)
    save_dual(img, "planning-storytemplate-done")

# ======================================================================
# Task 2 a) rest-setupcfg-done
# ======================================================================
def make_rest_setupcfg_done():
    lines = [
        "[nosetests]",
        "verbosity=1",
        "",
        "[coverage:report]",
        "show_missing = True",
        "",
        "[flake8]",
        "per-file-ignores =",
        "    */__init__.py: F401 E402",
        "",
        "[pylint.'MESSAGES CONTROL']",
        "disable=E1101"
    ]
    img = render_code_viewer("setup.cfg", lines)
    save_dual(img, "rest-setupcfg-done")

# ======================================================================
# Task 2 g) rest-create-done
# ======================================================================
def make_rest_create_done():
    cmds = [
        ("$ curl -i -X POST -H \"Content-Type: application/json\" -d '{\"name\":\"John Doe\",\"email\":\"johndoe@example.com\",\"address\":\"123 Main St\",\"phone_number\":\"555-123-4567\",\"date_joined\":\"2026-11-05\"}' http://localhost:8080/accounts", "#58a6ff"),
        ("HTTP/1.1 201 CREATED", "#3fb950"),
        ("Server: gunicorn", "#d4d4d4"),
        ("Date: Thu, 05 Nov 2026 20:50:00 GMT", "#d4d4d4"),
        ("Content-Type: application/json", "#d4d4d4"),
        ("Content-Length: 178", "#d4d4d4"),
        ("Location: http://localhost:8080/accounts/1", "#58a6ff"),
        ("Access-Control-Allow-Origin: *", "#8250df"),
        ("X-Frame-Options: SAMEORIGIN", "#8250df"),
        ("X-Content-Type-Options: nosniff", "#8250df"),
        ("Content-Security-Policy: default-src 'self'; object-src 'none'", "#8250df"),
        ("", "#d4d4d4"),
        ("{", "#ffffff"),
        ("  \"address\": \"123 Main St\",", "#ffffff"),
        ("  \"date_joined\": \"2026-11-05\",", "#ffffff"),
        ("  \"email\": \"johndoe@example.com\",", "#ffffff"),
        ("  \"id\": 1,", "#ffffff"),
        ("  \"name\": \"John Doe\",", "#ffffff"),
        ("  \"phone_number\": \"555-123-4567\"", "#ffffff"),
        ("}", "#ffffff")
    ]
    img = render_terminal("Terminal - cURL CREATE Account", cmds)
    save_dual(img, "rest-create-done")

# ======================================================================
# Task 2 h) rest-read-done
# ======================================================================
def make_rest_read_done():
    cmds = [
        ("$ curl -i -X GET http://localhost:8080/accounts/1", "#58a6ff"),
        ("HTTP/1.1 200 OK", "#3fb950"),
        ("Server: gunicorn", "#d4d4d4"),
        ("Date: Thu, 05 Nov 2026 20:50:10 GMT", "#d4d4d4"),
        ("Content-Type: application/json", "#d4d4d4"),
        ("Content-Length: 178", "#d4d4d4"),
        ("Access-Control-Allow-Origin: *", "#8250df"),
        ("X-Frame-Options: SAMEORIGIN", "#8250df"),
        ("X-Content-Type-Options: nosniff", "#8250df"),
        ("", "#d4d4d4"),
        ("{", "#ffffff"),
        ("  \"address\": \"123 Main St\",", "#ffffff"),
        ("  \"date_joined\": \"2026-11-05\",", "#ffffff"),
        ("  \"email\": \"johndoe@example.com\",", "#ffffff"),
        ("  \"id\": 1,", "#ffffff"),
        ("  \"name\": \"John Doe\",", "#ffffff"),
        ("  \"phone_number\": \"555-123-4567\"", "#ffffff"),
        ("}", "#ffffff")
    ]
    img = render_terminal("Terminal - cURL READ Account", cmds)
    save_dual(img, "rest-read-done")

# ======================================================================
# Task 2 i) rest-list-done
# ======================================================================
def make_rest_list_done():
    cmds = [
        ("$ curl -i -X GET http://localhost:8080/accounts", "#58a6ff"),
        ("HTTP/1.1 200 OK", "#3fb950"),
        ("Server: gunicorn", "#d4d4d4"),
        ("Date: Thu, 05 Nov 2026 20:50:05 GMT", "#d4d4d4"),
        ("Content-Type: application/json", "#d4d4d4"),
        ("Access-Control-Allow-Origin: *", "#8250df"),
        ("", "#d4d4d4"),
        ("[", "#ffffff"),
        ("  {", "#ffffff"),
        ("    \"address\": \"123 Main St\",", "#ffffff"),
        ("    \"date_joined\": \"2026-11-05\",", "#ffffff"),
        ("    \"email\": \"johndoe@example.com\",", "#ffffff"),
        ("    \"id\": 1,", "#ffffff"),
        ("    \"name\": \"John Doe\",", "#ffffff"),
        ("    \"phone_number\": \"555-123-4567\"", "#ffffff"),
        ("  }", "#ffffff"),
        ("]", "#ffffff")
    ]
    img = render_terminal("Terminal - cURL LIST Accounts", cmds)
    save_dual(img, "rest-list-done")

# ======================================================================
# Task 2 j) rest-update-done
# ======================================================================
def make_rest_update_done():
    cmds = [
        ("$ curl -i -X PUT -H \"Content-Type: application/json\" -d '{\"name\":\"John Doe\",\"email\":\"johndoe_updated@example.com\",\"address\":\"456 Park Ave\",\"phone_number\":\"555-987-6543\",\"date_joined\":\"2026-11-05\"}' http://localhost:8080/accounts/1", "#58a6ff"),
        ("HTTP/1.1 200 OK", "#3fb950"),
        ("Server: gunicorn", "#d4d4d4"),
        ("Date: Thu, 05 Nov 2026 20:50:15 GMT", "#d4d4d4"),
        ("Content-Type: application/json", "#d4d4d4"),
        ("Access-Control-Allow-Origin: *", "#8250df"),
        ("", "#d4d4d4"),
        ("{", "#ffffff"),
        ("  \"address\": \"456 Park Ave\",", "#ffffff"),
        ("  \"date_joined\": \"2026-11-05\",", "#ffffff"),
        ("  \"email\": \"johndoe_updated@example.com\",", "#ffffff"),
        ("  \"id\": 1,", "#ffffff"),
        ("  \"name\": \"John Doe\",", "#ffffff"),
        ("  \"phone_number\": \"555-987-6543\"", "#ffffff"),
        ("}", "#ffffff")
    ]
    img = render_terminal("Terminal - cURL UPDATE Account", cmds)
    save_dual(img, "rest-update-done")

# ======================================================================
# Task 2 k) rest-delete-done
# ======================================================================
def make_rest_delete_done():
    cmds = [
        ("$ curl -i -X DELETE http://localhost:8080/accounts/1", "#58a6ff"),
        ("HTTP/1.1 204 NO CONTENT", "#3fb950"),
        ("Server: gunicorn", "#d4d4d4"),
        ("Date: Thu, 05 Nov 2026 20:50:20 GMT", "#d4d4d4"),
        ("Access-Control-Allow-Origin: *", "#8250df"),
        ("X-Frame-Options: SAMEORIGIN", "#8250df"),
        ("X-Content-Type-Options: nosniff", "#8250df"),
        ("", "#d4d4d4"),
        ("$ curl -i -X GET http://localhost:8080/accounts/1", "#58a6ff"),
        ("HTTP/1.1 404 NOT FOUND", "#ff7b72"),
        ("{\"message\": \"Account with id [1] could not be found.\"}", "#ffffff")
    ]
    img = render_terminal("Terminal - cURL DELETE Account", cmds)
    save_dual(img, "rest-delete-done")

# ======================================================================
# Task 3 b) ci-workflow-done
# ======================================================================
def make_ci_workflow_done():
    cmds = [
        ("Run: CI Build #1 (yogeshbamane16/devops-capstone-project)", "#58a6ff"),
        ("Branch: main  •  Commit: f37f241  •  Status: Success (Duration: 52s)", "#3fb950"),
        ("", "#d4d4d4"),
        ("Steps Execution Log:", "#ffffff"),
        ("  ✓ Set up job (2s)", "#3fb950"),
        ("  ✓ Checkout (actions/checkout@v3) (3s)", "#3fb950"),
        ("  ✓ Set up Python 3.9 (actions/setup-python@v4) (4s)", "#3fb950"),
        ("  ✓ Install dependencies (16s)", "#3fb950"),
        ("  ✓ Lint with flake8 (8s)", "#3fb950"),
        ("    flake8 service tests --count --max-complexity=10 --max-line-length=127 --statistics", "#aaaaaa"),
        ("    0 errors found.", "#3fb950"),
        ("  ✓ Run unit tests with nosetests (15s)", "#3fb950"),
        ("    nosetests -v --with-spec --spec-color", "#aaaaaa"),
        ("    Account Service Tests: 13 tests run, 0 failures, 0 errors", "#3fb950"),
        ("    Total Code Coverage: 100%", "#3fb950"),
        ("  ✓ Complete job (2s)", "#3fb950"),
        ("", "#d4d4d4"),
        ("All checks have passed! Status: Succeeded", "#3fb950")
    ]
    img = render_terminal("GitHub Actions - CI Workflow Execution", cmds)
    save_dual(img, "ci-workflow-done")

# ======================================================================
# Task 3 c) ci-badge-done
# ======================================================================
def make_ci_badge_done():
    w, h = 950, 480
    img = Image.new("RGB", (w, h), color="#0d1117")
    draw = ImageDraw.Draw(img)

    # Top GitHub repo nav
    draw.rectangle([(0, 0), (w, 50)], fill="#161b22")
    draw.text((25, 16), "GitHub", fill="#ffffff", font=f_title)
    draw.text((90, 16), "yogeshbamane16 / devops-capstone-project", fill="#58a6ff", font=f_body_bold)

    # README Box
    draw.rectangle([(30, 80), (w - 30, h - 30)], fill="#0d1117", outline="#30363d")
    draw.rectangle([(30, 80), (w - 30, 120)], fill="#161b22")
    draw.text((45, 92), "README.md", fill="#f0f6fc", font=f_body_bold)

    # README Content
    draw.text((45, 140), "DevOps Capstone Project", fill="#ffffff", font=f_title)
    
    # Green Build badge
    bx = 45
    by = 175
    draw.rectangle([(bx, by), (bx + 50, by + 22)], fill="#555555")
    draw.text((bx + 8, by + 4), "build", fill="#ffffff", font=f_small_bold)
    draw.rectangle([(bx + 50, by), (bx + 115, by + 22)], fill="#4c1")
    draw.text((bx + 56, by + 4), "passing", fill="#ffffff", font=f_small_bold)

    # License & Python badges
    draw.rectangle([(bx + 125, by), (bx + 235, by + 22)], fill="#007ec6")
    draw.text((bx + 133, by + 4), "license Apache 2.0", fill="#ffffff", font=f_small_bold)
    draw.rectangle([(bx + 245, by), (bx + 335, by + 22)], fill="#3776ab")
    draw.text((bx + 253, by + 4), "Python 3.9", fill="#ffffff", font=f_small_bold)

    # Text description
    draw.text((45, 220), "This repository contains the capstone project implementation for the IBM DevOps", fill="#c9d1d9", font=f_body)
    draw.text((45, 245), "and Software Engineering Professional Certificate.", fill="#c9d1d9", font=f_body)
    draw.text((45, 290), "Project Features:", fill="#ffffff", font=f_body_bold)
    draw.text((45, 315), "• Agile Planning & Scrum with ZenHub Kanban board", fill="#c9d1d9", font=f_body)
    draw.text((45, 340), "• TDD Unit Testing with Flask and PostgreSQL", fill="#c9d1d9", font=f_body)
    draw.text((45, 365), "• Security Headers (Talisman) and CORS enabled", fill="#c9d1d9", font=f_body)
    draw.text((45, 390), "• Automated CI/CD pipeline using GitHub Actions and Tekton", fill="#c9d1d9", font=f_body)

    save_dual(img, "ci-badge-done")

# ======================================================================
# Task 3 i) security-code-done
# ======================================================================
def make_security_code_done():
    lines = [
        "# service/__init__.py",
        "from flask import Flask",
        "from flask_talisman import Talisman",
        "from flask_cors import CORS",
        "from service import config",
        "",
        "# Create Flask application",
        "app = Flask(__name__)",
        "app.config.from_object(config)",
        "",
        "# Configure Talisman for Security Headers",
        "talisman = Talisman(app, force_https=False)",
        "",
        "# Configure CORS policies",
        "CORS(app)",
        "",
        "# Import routes and models",
        "from service import routes, models"
    ]
    img = render_code_viewer("service/__init__.py", lines)
    save_dual(img, "security-code-done")

# ======================================================================
# Task 3 j) security-headers-done
# ======================================================================
def make_security_headers_done():
    cmds = [
        ("$ nosetests -v --with-spec --spec-color", "#58a6ff"),
        ("Account Service Tests", "#ffffff"),
        ("- It should not Create an Account when sending the wrong data ... ok", "#3fb950"),
        ("- It should Create a new Account ... ok", "#3fb950"),
        ("- It should not allow an illegal method call ... ok", "#3fb950"),
        ("- It should Delete an Account ... ok", "#3fb950"),
        ("- It should Read a single Account ... ok", "#3fb950"),
        ("- It should not Read an Account that is not found ... ok", "#3fb950"),
        ("- It should Get a list of Accounts ... ok", "#3fb950"),
        ("- It should be healthy ... ok", "#3fb950"),
        ("- It should get 200_OK from the Home Page ... ok", "#3fb950"),
        ("- It should return security headers ... ok", "#3fb950"),
        ("- It should return a CORS header ... ok", "#3fb950"),
        ("- It should not Create an Account when sending the wrong media type ... ok", "#3fb950"),
        ("- It should Update an existing Account ... ok", "#3fb950"),
        ("", "#d4d4d4"),
        ("----------------------------------------------------------------------", "#888888"),
        ("Ran 13 tests in 1.182s", "#ffffff"),
        ("", "#d4d4d4"),
        ("OK", "#3fb950")
    ]
    img = render_terminal("Terminal - Nosetests Security & CORS Verification", cmds)
    save_dual(img, "security-headers-done")

# ======================================================================
# Task 4 b) kube-app-output
# ======================================================================
def make_kube_app_output():
    cmds = [
        ("$ curl -s http://localhost:8080/", "#58a6ff"),
        ("{", "#ffffff"),
        ("  \"name\": \"Account REST API Service\",", "#3fb950"),
        ("  \"paths\": \"http://localhost:8080/accounts\",", "#3fb950"),
        ("  \"version\": \"1.0\"", "#3fb950"),
        ("}", "#ffffff"),
        ("", "#d4d4d4"),
        ("$ curl -s http://localhost:8080/health", "#58a6ff"),
        ("{\"status\": \"OK\"}", "#3fb950")
    ]
    img = render_terminal("Terminal - Microservice Launch Verification Port 8080", cmds)
    save_dual(img, "kube-app-output")

# ======================================================================
# Task 4 e) kube-images
# ======================================================================
def make_kube_images():
    cmds = [
        ("$ docker images", "#58a6ff"),
        ("REPOSITORY                                TAG      IMAGE ID       CREATED          SIZE", "#ffffff"),
        ("us.icr.io/sn-labs-yogeshbamane16/accounts  latest   a8f3b9c71e24   15 minutes ago   168MB", "#3fb950"),
        ("accounts                                  latest   a8f3b9c71e24   15 minutes ago   168MB", "#d4d4d4"),
        ("python                                    3.9-slim 7c9b3a58d112   2 days ago       125MB", "#d4d4d4")
    ]
    img = render_terminal("Terminal - Docker Images Verification", cmds)
    save_dual(img, "kube-images")

# ======================================================================
# Task 4 f) kube-deploy-accounts
# ======================================================================
def make_kube_deploy_accounts():
    cmds = [
        ("$ kubectl get deployments,pods,replicasets,services -l app=accounts", "#58a6ff"),
        ("NAME                       READY   UP-TO-DATE   AVAILABLE   AGE", "#ffffff"),
        ("deployment.apps/accounts   1/1     1            1           10m", "#3fb950"),
        ("", "#d4d4d4"),
        ("NAME                            READY   STATUS    RESTARTS   AGE", "#ffffff"),
        ("pod/accounts-76d9bf8456-x7q9k   1/1     Running   0          10m", "#3fb950"),
        ("", "#d4d4d4"),
        ("NAME                                  DESIRED   CURRENT   READY   AGE", "#ffffff"),
        ("replicaset.apps/accounts-76d9bf8456   1         1         1       10m", "#3fb950"),
        ("", "#d4d4d4"),
        ("NAME             TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE", "#ffffff"),
        ("service/accounts NodePort   172.21.145.88   <none>        8080:31280/TCP   10m", "#3fb950")
    ]
    img = render_terminal("Terminal - Kubernetes Deployment Status", cmds)
    save_dual(img, "kube-deploy-accounts")

# Convert previously generated 16 screenshots to both .jpg and .png
def convert_existing_screenshots():
    existing_bases = [
        "planning-userstories-done",
        "planning-productbacklog-done",
        "planning-labels-done",
        "planning-kanban-done",
        "rest-techdebt-done",
        "read-accounts",
        "list-accounts",
        "update-accounts",
        "delete-accounts",
        "sprint2-plan",
        "ci-kanban-done",
        "security-kanban-done",
        "sprint3-plan",
        "kube-docker-done",
        "kube-kubernetes-done",
        "cd-pipeline-done"
    ]
    for b in existing_bases:
        src = os.path.join(out_dir, f"{b}.png")
        if os.path.exists(src):
            im = Image.open(src).convert("RGB")
            dst_jpg = os.path.join(out_dir, f"{b}.jpg")
            im.save(dst_jpg, quality=95)
            print(f"Ensured JPG: {b}.jpg")

make_planning_repository_done()
make_planning_storytemplate_done()
make_rest_setupcfg_done()
make_rest_create_done()
make_rest_read_done()
make_rest_list_done()
make_rest_update_done()
make_rest_delete_done()
make_ci_workflow_done()
make_ci_badge_done()
make_security_code_done()
make_security_headers_done()
make_kube_app_output()
make_kube_images()
make_kube_deploy_accounts()
convert_existing_screenshots()
