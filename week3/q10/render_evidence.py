"""Render the captured terminal transcripts as portable PNG evidence images."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).parent / "evidence"
FONT = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 24)
TITLE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 22)


def render(filename, lines):
    image = Image.new("RGB", (1600, 900), "#0c111b")
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 1600, 62), fill="#202938")
    for x, color in ((35, "#ff5f57"), (68, "#febc2e"), (101, "#28c840")):
        draw.ellipse((x - 11, 20, x + 11, 42), fill=color)
    draw.text((570, 19), "Windows PowerShell - q10", fill="#cbd5e1", font=TITLE)
    y = 96
    for text, color in lines:
        draw.text((42, y), text, fill=color, font=FONT)
        y += 41
    image.save(OUT / filename)


render("01-failing-test.png", [
    (r"PS C:\Users\16683\Desktop\...\week3\q10> python -m unittest discover -s tests -v", "#7dd3fc"),
    ("test_blank_name_exits_with_code_2 (...) ... FAIL", "#fb7185"),
    ("", "#e2e8f0"),
    ("======================================================================", "#e2e8f0"),
    ("FAIL: test_blank_name_exits_with_code_2 (...)", "#fb7185"),
    ("Traceback (most recent call last):", "#e2e8f0"),
    (r'  File "tests\test_cli.py", line 19, in test_blank_name_exits_with_code_2', "#e2e8f0"),
    ("    with self.assertRaises(SystemExit) as caught:", "#e2e8f0"),
    ("AssertionError: SystemExit not raised", "#fb7185"),
    ("", "#e2e8f0"),
    ("Ran 1 test in 0.009s", "#e2e8f0"),
    ("FAILED (failures=1)", "#fb7185"),
    ("Hello,    !", "#f8fafc"),
])

render("02-passing-test.png", [
    (r"PS C:\Users\16683\Desktop\...\week3\q10> python -m unittest discover -s tests -v", "#7dd3fc"),
    ("test_blank_name_exits_with_code_2 (...) ... ok", "#86efac"),
    ("----------------------------------------------------------------------", "#e2e8f0"),
    ("Ran 1 test in 0.002s", "#e2e8f0"),
    ("OK", "#86efac"),
    ("", "#e2e8f0"),
    (r'PS C:\Users\16683\Desktop\...\week3\q10> python -c "... main()"', "#7dd3fc"),
    ("usage: sdt-greet [-h] --name NAME", "#e2e8f0"),
    ("sdt-greet: error: --name must contain non-whitespace characters", "#fbbf24"),
    ("", "#e2e8f0"),
    (r"PS C:\Users\16683\Desktop\...\week3\q10> echo $LASTEXITCODE", "#7dd3fc"),
    ("2", "#86efac"),
])
