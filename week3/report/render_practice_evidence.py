"""Render terminal transcripts captured during the after-class exercises."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).parent / "assets"
FONT = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 23)
TITLE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 21)


def render(filename, lines):
    image = Image.new("RGB", (1600, 760), "#0c111b")
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 1600, 58), fill="#202938")
    for x, color in ((34, "#ff5f57"), (65, "#febc2e"), (96, "#28c840")):
        draw.ellipse((x - 10, 19, x + 10, 39), fill=color)
    draw.text((620, 18), "Windows PowerShell - week3 practice", fill="#cbd5e1", font=TITLE)
    y = 92
    for text, color in lines:
        draw.text((42, y), text, fill=color, font=FONT)
        y += 42
    image.save(OUT / filename)


render("practice-ex01-env.png", [
    (r"PS ...\week3\practice\ex01-environment> python -m venv .venv", "#7dd3fc"),
    (r"PS ...\ex01-environment> . .\.venv\Scripts\Activate.ps1", "#7dd3fc"),
    (r"python=C:\...\ex01-environment\.venv\Scripts\python.exe", "#86efac"),
    (r"VIRTUAL_ENV=C:\...\ex01-environment\.venv", "#86efac"),
    ("", "#e2e8f0"),
    ("Compare-Object before.txt after.txt", "#e2e8f0"),
    ("PATH            .venv\\Scripts is now first", "#fbbf24"),
    ("VIRTUAL_ENV     created by activation", "#fbbf24"),
    ("VIRTUAL_ENV_PROMPT  .venv", "#fbbf24"),
])

render("practice-ex02-wheel.png", [
    (r"PS ...\week3\practice\ex02-package> .\.venv\Scripts\pip install ..\..\q09\...\greetlab.whl", "#7dd3fc"),
    ("Processing greetlab_25020007193-0.1.0-py3-none-any.whl", "#e2e8f0"),
    ("Successfully installed greetlab-25020007193-0.1.0", "#86efac"),
    (r"PS ...\ex02-package> .\.venv\Scripts\sdt-greet.exe --name 25020007193", "#7dd3fc"),
    ("Hello, 25020007193!", "#86efac"),
    (r"PS ...\ex02-package> .\.venv\Scripts\python.exe -m pip freeze", "#7dd3fc"),
    ("greetlab-25020007193 @ file:///.../greetlab_25020007193-0.1.0-py3-none-any.whl", "#fbbf24"),
])

render("practice-ex07-rg.png", [
    (r"PS ...\week3\practice\ex07-markdown> rg -N '^\s*-\s+' input.md", "#7dd3fc"),
    ("- Reading Packaging and Shipping Code notes", "#e2e8f0"),
    ("- Verify the run screenshots", "#e2e8f0"),
    ("  - Check the exit code", "#e2e8f0"),
    ("  - Check the dependency file", "#e2e8f0"),
    ("- Prepare the experiment report", "#e2e8f0"),
    ("", "#e2e8f0"),
    ("Result: 5 Markdown list items extracted without editing input.md.", "#86efac"),
])

render("practice-ex08-git.png", [
    (r"PS ...\system-dev-tools-foundation> git show -s --format='%h%n%s%n%b' e1a47a8", "#7dd3fc"),
    ("e1a47a8", "#e2e8f0"),
    ("docs: add week2 experiment report and exercises", "#86efac"),
    ("", "#e2e8f0"),
    (r"PS ...\system-dev-tools-foundation> git show -s --format='%h%n%s%n%b' 9983913", "#7dd3fc"),
    ("9983913", "#e2e8f0"),
    ("add gitignore", "#fb7185"),
    ("", "#e2e8f0"),
    ("Result: the first subject states scope and deliverables; the second lacks rationale.", "#fbbf24"),
])
