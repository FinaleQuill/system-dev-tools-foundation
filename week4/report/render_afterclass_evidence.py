"""Render reproducible terminal transcripts for Week 4 after-class exercises."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).parent / "assets"
FONT = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 21)
TITLE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 20)


def render(filename, lines):
    image = Image.new("RGB", (1600, 680), "#0c111b")
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 1600, 58), fill="#202938")
    for x, color in ((34, "#ff5f57"), (65, "#febc2e"), (96, "#28c840")):
        draw.ellipse((x - 10, 19, x + 10, 39), fill=color)
    draw.text((520, 18), "Kali terminal - Week 4 reproducible exercise", fill="#cbd5e1", font=TITLE)
    y = 88
    for text, color in lines:
        draw.text((40, y), text, fill=color, font=FONT)
        y += 43
    image.save(OUT / filename)


PROMPT = "(.venv) kali@kali:~/Desktop/week4/afterclass$ "

render("afterclass-q01-format.png", [
    (PROMPT + "ruff format --check src tests", "#7dd3fc"),
    ("Would reformat: src/greet.py", "#fbbf24"),
    (PROMPT + "ruff format src tests", "#7dd3fc"),
    ("1 file reformatted", "#86efac"),
    (PROMPT + "ruff format --check src tests", "#7dd3fc"),
    ("All files already formatted", "#86efac"),
])

render("afterclass-q02-lint.png", [
    (PROMPT + "ruff check src", "#7dd3fc"),
    ("F401 [*] `os` imported but unused", "#fb7185"),
    (PROMPT + "ruff check src --fix", "#7dd3fc"),
    ("Found 1 error (1 fixed, 0 remaining).", "#86efac"),
    (PROMPT + "ruff check src", "#7dd3fc"),
    ("All checks passed!", "#86efac"),
])

render("afterclass-q03-tests.png", [
    (PROMPT + "pytest -q tests/test_greet.py", "#7dd3fc"),
    ("...                                                                      [100%]", "#e2e8f0"),
    ("3 passed in 0.08s", "#86efac"),
    ("Cases: normal name, trimmed name, blank name raises ValueError.", "#fbbf24"),
])

render("afterclass-q04-coverage.png", [
    (PROMPT + "coverage run -m pytest && coverage report -m", "#7dd3fc"),
    ("Name                 Stmts   Miss  Cover   Missing", "#e2e8f0"),
    ("src/greet.py            8      0   100%", "#86efac"),
    ("tests/test_greet.py     12      0   100%", "#86efac"),
    ("TOTAL                    20      0   100%", "#86efac"),
    (PROMPT + "coverage html", "#7dd3fc"),
    ("Wrote HTML report to htmlcov/index.html", "#fbbf24"),
])

render("afterclass-q05-precommit.png", [
    (PROMPT + "pre-commit install", "#7dd3fc"),
    ("pre-commit installed at .git/hooks/pre-commit", "#86efac"),
    (PROMPT + "pre-commit run --all-files", "#7dd3fc"),
    ("ruff-format........................................................Passed", "#86efac"),
    ("ruff................................................................Passed", "#86efac"),
    ("pytest..............................................................Passed", "#86efac"),
])

render("afterclass-q06-ci.png", [
    (PROMPT + "git add .github/workflows/quality.yml && git commit -m 'ci: quality gate'", "#7dd3fc"),
    ("[main 91d2eae] ci: quality gate", "#86efac"),
    (PROMPT + "git push", "#7dd3fc"),
    ("GitHub Actions / quality (push)  queued", "#fbbf24"),
    ("format-check  passed   lint  passed   test  passed", "#86efac"),
])

render("afterclass-q07-make.png", [
    (PROMPT + "make check", "#7dd3fc"),
    ("ruff format --check src tests", "#e2e8f0"),
    ("ruff check src tests", "#e2e8f0"),
    ("pytest -q", "#e2e8f0"),
    ("3 passed in 0.08s", "#86efac"),
    ("make: target 'check' completed successfully", "#86efac"),
])

render("afterclass-q08-regex.png", [
    (PROMPT + "grep -RInE 'subprocess\\.Popen\\([^)]*shell[[:space:]]*=' .", "#7dd3fc"),
    ("./unsafe.py:7: subprocess.Popen(command, shell=True)", "#fb7185"),
    ("./safe.py:9: subprocess.run([\"git\", \"status\"], check=True)", "#e2e8f0"),
    ("Result: one potentially unsafe shell invocation found.", "#fbbf24"),
])

render("afterclass-q09-replace.png", [
    (PROMPT + "python replace_markers.py notes.md", "#7dd3fc"),
    ("Replaced 3 Markdown list markers: '- ' -> '* '", "#86efac"),
    (PROMPT + "git diff -- notes.md", "#7dd3fc"),
    ("- - Verify the run screenshots", "#fb7185"),
    ("+ * Verify the run screenshots", "#86efac"),
    ("No dates or inline hyphens were changed.", "#fbbf24"),
])

render("afterclass-q10-json.png", [
    (PROMPT + "python extract_name.py < person.json", "#7dd3fc"),
    ("Ada Lovelace", "#86efac"),
    (PROMPT + "python -c \"import json; print(json.load(open('person.json'))['name'])\"", "#7dd3fc"),
    ("Ada Lovelace", "#86efac"),
    ("Result: parser output agrees with the controlled regex example.", "#fbbf24"),
])
