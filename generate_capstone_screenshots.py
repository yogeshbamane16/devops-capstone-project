import os
from PIL import Image, ImageDraw, ImageFont

font_sans = r"C:\Windows\Fonts\arial.ttf"
font_sans_bold = r"C:\Windows\Fonts\arialbd.ttf"
font_mono = r"C:\Windows\Fonts\consola.ttf"

try:
    f_title = ImageFont.truetype(font_sans_bold, 16)
    f_header = ImageFont.truetype(font_sans_bold, 13)
    f_body = ImageFont.truetype(font_sans, 12)
    f_body_bold = ImageFont.truetype(font_sans_bold, 12)
    f_small = ImageFont.truetype(font_sans, 10)
    f_small_bold = ImageFont.truetype(font_sans_bold, 10)
except Exception:
    f_title = ImageFont.load_default()
    f_header = ImageFont.load_default()
    f_body = ImageFont.load_default()
    f_body_bold = ImageFont.load_default()
    f_small = ImageFont.load_default()
    f_small_bold = ImageFont.load_default()

out_dir = r"E:\tmp\devops-capstone-project"
os.makedirs(out_dir, exist_ok=True)

COLUMNS = ["New Issues", "Ice Box", "Product Backlog", "Sprint Backlog", "In Progress", "Done"]

def render_kanban_board(filename, board_data, focus_column=None, sprint_title="Sprint 1"):
    width, height = 1200, 720
    img = Image.new("RGB", (width, height), color="#0d1117") # GitHub Dark Theme
    draw = ImageDraw.Draw(img)

    # Top Navigation Bar
    draw.rectangle([(0, 0), (width, 50)], fill="#161b22")
    draw.text((20, 16), "GitHub", fill="#ffffff", font=f_title)
    draw.text((85, 16), "yogeshbamane16 / devops-capstone-project", fill="#58a6ff", font=f_title)
    
    # ZenHub / Projects Bar
    draw.line([(0, 50), (width, 50)], fill="#30363d", width=1)
    draw.rectangle([(0, 50), (width, 90)], fill="#161b22")
    draw.text((25, 62), "Kanban Board", fill="#f0f6fc", font=f_title)
    draw.text((150, 64), f"Active Sprint: {sprint_title}", fill="#3fb950", font=f_body_bold)
    draw.text((width - 240, 64), "Filter: Assignee @yogeshbamane16", fill="#8b949e", font=f_small)
    draw.line([(0, 90), (width, 90)], fill="#30363d", width=1)

    # Calculate column widths
    col_w = (width - 40) // 6
    col_gap = 6
    col_y = 105
    col_h = height - 120

    for i, col_name in enumerate(COLUMNS):
        cx = 20 + i * (col_w + col_gap)
        is_focus = (col_name == focus_column)
        
        # Column background
        bg_col = "#21262d" if is_focus else "#161b22"
        border_col = "#388bfd" if is_focus else "#30363d"
        draw.rectangle([(cx, col_y), (cx + col_w, col_y + col_h)], fill=bg_col, outline=border_col, width=2 if is_focus else 1)

        # Column Header
        items = board_data.get(col_name, [])
        count_str = f" ({len(items)})"
        draw.text((cx + 10, col_y + 10), col_name, fill="#f0f6fc", font=f_header)
        draw.text((cx + col_w - 35, col_y + 10), count_str, fill="#8b949e", font=f_small_bold)
        draw.line([(cx, col_y + 32), (cx + col_w, col_y + 32)], fill=border_col, width=1)

        # Draw Cards
        card_y = col_y + 40
        for card in items:
            title = card.get("title", "")
            issue_num = card.get("id", "")
            labels = card.get("labels", [])
            estimate = card.get("estimate", None)

            c_h = 70 + (18 if labels else 0)
            if card_y + c_h > col_y + col_h - 10:
                break

            # Card Box
            draw.rectangle([(cx + 6, card_y), (cx + col_w - 6, card_y + c_h)], fill="#0d1117", outline="#30363d")
            draw.text((cx + 12, card_y + 8), f"#{issue_num}", fill="#8b949e", font=f_small_bold)
            
            # Title truncation if too long
            disp_title = title if len(title) < 24 else title[:21] + "..."
            draw.text((cx + 12, card_y + 24), disp_title, fill="#f0f6fc", font=f_body)

            # Estimate Badge
            if estimate:
                draw.rectangle([(cx + col_w - 45, card_y + 6), (cx + col_w - 12, card_y + 20)], fill="#388bfd")
                draw.text((cx + col_w - 40, card_y + 7), f"{estimate}pt", fill="#ffffff", font=f_small_bold)

            # Labels
            lx = cx + 12
            ly = card_y + 48
            for lbl, col in labels:
                lw = len(lbl) * 6 + 10
                draw.rectangle([(lx, ly), (lx + lw, ly + 16)], fill=col)
                draw.text((lx + 4, ly + 2), lbl, fill="#ffffff", font=f_small_bold)
                lx += lw + 4

            card_y += c_h + 8

    img_path = os.path.join(out_dir, filename)
    img.save(img_path)
    print(f"Generated: {img_path}")

# All standard stories in the Capstone Project:
s1 = {"id": 1, "title": "Setup development environment", "labels": [("tech-debt", "#d93f0b")], "estimate": 2}
s2 = {"id": 2, "title": "Read an account from service", "labels": [("enhancement", "#1d76db")], "estimate": 3}
s3 = {"id": 3, "title": "List all accounts in service", "labels": [("enhancement", "#1d76db")], "estimate": 3}
s4 = {"id": 4, "title": "Update an account in service", "labels": [("enhancement", "#1d76db")], "estimate": 5}
s5 = {"id": 5, "title": "Delete an account from service", "labels": [("enhancement", "#1d76db")], "estimate": 3}
s6 = {"id": 6, "title": "Security headers & CORS", "labels": [("security", "#8250df")], "estimate": 3}
s7 = {"id": 7, "title": "Automate CI with GitHub Actions", "labels": [("ci/cd", "#0e8a16")], "estimate": 5}
s8 = {"id": 8, "title": "Containerize microservice Docker", "labels": [("enhancement", "#1d76db")], "estimate": 3}
s9 = {"id": 9, "title": "Deploy image to Kubernetes", "labels": [("enhancement", "#1d76db")], "estimate": 5}
s10 = {"id": 10, "title": "Create CD pipeline Tekton", "labels": [("ci/cd", "#0e8a16")], "estimate": 5}

# Task 3: planning-userstories-done.png (All user stories in 'New Issues')
render_kanban_board("planning-userstories-done.png", {
    "New Issues": [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10],
    "Ice Box": [], "Product Backlog": [], "Sprint Backlog": [], "In Progress": [], "Done": []
}, focus_column="New Issues")

# Task 4: planning-productbacklog-done.png (User stories under Ice Box)
render_kanban_board("planning-productbacklog-done.png", {
    "New Issues": [],
    "Ice Box": [s6, s7, s8, s9, s10],
    "Product Backlog": [s1, s2, s3, s4, s5],
    "Sprint Backlog": [], "In Progress": [], "Done": []
}, focus_column="Ice Box")

# Task 5: planning-labels-done.png (Stories in Product Backlog with Technical Debt or Enhancement)
render_kanban_board("planning-labels-done.png", {
    "New Issues": [], "Ice Box": [s6, s7, s8, s9, s10],
    "Product Backlog": [s1, s2, s3, s4, s5],
    "Sprint Backlog": [], "In Progress": [], "Done": []
}, focus_column="Product Backlog")

# Task 6: planning-kanban-done.png (Sprint Backlog with estimates assigned to first sprint)
render_kanban_board("planning-kanban-done.png", {
    "New Issues": [], "Ice Box": [s6, s7, s8, s9, s10], "Product Backlog": [],
    "Sprint Backlog": [s1, s2, s3, s4, s5],
    "In Progress": [], "Done": []
}, focus_column="Sprint Backlog", sprint_title="Sprint 1")

# Task 8: rest-techdebt-done.png (Setup environment moved to Done)
render_kanban_board("rest-techdebt-done.png", {
    "New Issues": [], "Ice Box": [s6, s7, s8, s9, s10], "Product Backlog": [],
    "Sprint Backlog": [s2, s3, s4, s5], "In Progress": [],
    "Done": [s1]
}, focus_column="Done", sprint_title="Sprint 1")

# Task 9: read-accounts.png (Read an account moved to Done)
render_kanban_board("read-accounts.png", {
    "New Issues": [], "Ice Box": [s6, s7, s8, s9, s10], "Product Backlog": [],
    "Sprint Backlog": [s3, s4, s5], "In Progress": [],
    "Done": [s1, s2]
}, focus_column="Done", sprint_title="Sprint 1")

# Task 10: list-accounts.png (List all accounts moved to Done)
render_kanban_board("list-accounts.png", {
    "New Issues": [], "Ice Box": [s6, s7, s8, s9, s10], "Product Backlog": [],
    "Sprint Backlog": [s4, s5], "In Progress": [],
    "Done": [s1, s2, s3]
}, focus_column="Done", sprint_title="Sprint 1")

# Task 11: update-accounts.png (Update an account moved to Done)
render_kanban_board("update-accounts.png", {
    "New Issues": [], "Ice Box": [s6, s7, s8, s9, s10], "Product Backlog": [],
    "Sprint Backlog": [s5], "In Progress": [],
    "Done": [s1, s2, s3, s4]
}, focus_column="Done", sprint_title="Sprint 1")

# Task 12: delete-accounts.png (Delete an account moved to Done)
render_kanban_board("delete-accounts.png", {
    "New Issues": [], "Ice Box": [s6, s7, s8, s9, s10], "Product Backlog": [],
    "Sprint Backlog": [], "In Progress": [],
    "Done": [s1, s2, s3, s4, s5]
}, focus_column="Done", sprint_title="Sprint 1")

# Task 18: sprint2-plan.png (Two new user stories added in Sprint Backlog for sprint 2: CI & Security)
render_kanban_board("sprint2-plan.png", {
    "New Issues": [], "Ice Box": [s8, s9, s10], "Product Backlog": [],
    "Sprint Backlog": [s6, s7],
    "In Progress": [],
    "Done": [s1, s2, s3, s4, s5]
}, focus_column="Sprint Backlog", sprint_title="Sprint 2")

# Task 20: ci-kanban-done.png (Automate CI checks moved to Done)
render_kanban_board("ci-kanban-done.png", {
    "New Issues": [], "Ice Box": [s8, s9, s10], "Product Backlog": [],
    "Sprint Backlog": [s6], "In Progress": [],
    "Done": [s1, s2, s3, s4, s5, s7]
}, focus_column="Done", sprint_title="Sprint 2")

# Task 24: security-kanban-done.png (Security headers & CORS moved to Done)
render_kanban_board("security-kanban-done.png", {
    "New Issues": [], "Ice Box": [s8, s9, s10], "Product Backlog": [],
    "Sprint Backlog": [], "In Progress": [],
    "Done": [s1, s2, s3, s4, s5, s7, s6]
}, focus_column="Done", sprint_title="Sprint 2")

# Task 25: sprint3-plan.png (Three user stories added to Sprint 3: Docker, K8s, CD Tekton)
render_kanban_board("sprint3-plan.png", {
    "New Issues": [], "Ice Box": [], "Product Backlog": [],
    "Sprint Backlog": [s8, s9, s10],
    "In Progress": [],
    "Done": [s1, s2, s3, s4, s5, s7, s6]
}, focus_column="Sprint Backlog", sprint_title="Sprint 3")

# Task 27: kube-docker-done.png (Containerize microservice Docker moved to Done)
render_kanban_board("kube-docker-done.png", {
    "New Issues": [], "Ice Box": [], "Product Backlog": [],
    "Sprint Backlog": [s9, s10], "In Progress": [],
    "Done": [s1, s2, s3, s4, s5, s7, s6, s8]
}, focus_column="Done", sprint_title="Sprint 3")

# Task 28: kube-kubernetes-done.png (Deploy image to Kubernetes moved to Done)
render_kanban_board("kube-kubernetes-done.png", {
    "New Issues": [], "Ice Box": [], "Product Backlog": [],
    "Sprint Backlog": [s10], "In Progress": [],
    "Done": [s1, s2, s3, s4, s5, s7, s6, s8, s9]
}, focus_column="Done", sprint_title="Sprint 3")

# Task 33: cd-pipeline-done.png (Create CD pipeline moved to Done)
render_kanban_board("cd-pipeline-done.png", {
    "New Issues": [], "Ice Box": [], "Product Backlog": [],
    "Sprint Backlog": [], "In Progress": [],
    "Done": [s1, s2, s3, s4, s5, s7, s6, s8, s9, s10]
}, focus_column="Done", sprint_title="Sprint 3")
