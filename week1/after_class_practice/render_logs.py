from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
LOG_DIR = ROOT / "logs"
OUTPUT_DIR = ROOT.parent / "report" / "assets"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

EXERCISES = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
TITLES = {
    1: "确认 Unix Shell 环境",
    2: "读取 ls -l 权限字段",
    3: "测试 Shell glob 模式",
    4: "比较三种引号",
    5: "重定向标准输出与错误",
    6: "退出状态与条件执行",
    7: "验证 cd 是 Shell 内建命令",
    8: "用脚本检查文件是否存在",
    10: "使用 set -x 跟踪命令",
    11: "生成带日期的备份文件名",
}

WIDTH = 1720
PAD_X = 66
TOP_BAR = 82
LINE_GAP = 12
FONT_SIZE = 29
FONT_PATH = Path(r"C:\Windows\Fonts\msyh.ttc")
BOLD_PATH = Path(r"C:\Windows\Fonts\msyhbd.ttc")
font = ImageFont.truetype(str(FONT_PATH), FONT_SIZE)
bold = ImageFont.truetype(str(BOLD_PATH), 31)
small = ImageFont.truetype(str(FONT_PATH), 23)


def wrap_line(draw: ImageDraw.ImageDraw, line: str, max_width: int) -> list[str]:
    if not line:
        return [""]
    chunks: list[str] = []
    remaining = line
    prefix = ""
    while remaining:
        lo, hi = 1, len(remaining)
        best = 1
        while lo <= hi:
            mid = (lo + hi) // 2
            candidate = prefix + remaining[:mid]
            if draw.textlength(candidate, font=font) <= max_width:
                best = mid
                lo = mid + 1
            else:
                hi = mid - 1
        chunks.append(prefix + remaining[:best])
        remaining = remaining[best:]
        prefix = "    "
    return chunks


for number in EXERCISES:
    log_path = LOG_DIR / f"ex{number:02d}.log"
    raw_lines = log_path.read_text(encoding="utf-8").rstrip().splitlines()

    measuring = Image.new("RGB", (WIDTH, 200), "#0d1117")
    measure_draw = ImageDraw.Draw(measuring)
    lines: list[str] = []
    for raw in raw_lines:
        lines.extend(wrap_line(measure_draw, raw, WIDTH - 2 * PAD_X))

    line_height = FONT_SIZE + LINE_GAP
    height = TOP_BAR + 38 + len(lines) * line_height + 52
    image = Image.new("RGB", (WIDTH, height), "#0d1117")
    draw = ImageDraw.Draw(image)

    draw.rounded_rectangle((18, 18, WIDTH - 18, height - 18), radius=22,
                           fill="#111820", outline="#34485c", width=3)
    draw.rounded_rectangle((18, 18, WIDTH - 18, TOP_BAR), radius=22,
                           fill="#1c2733")
    draw.rectangle((18, TOP_BAR - 22, WIDTH - 18, TOP_BAR), fill="#1c2733")
    for x, color in [(50, "#ff5f57"), (82, "#febc2e"), (114, "#28c840")]:
        draw.ellipse((x, 43, x + 16, 59), fill=color)
    draw.text((150, 35), f"Bash · 实例 {number} · {TITLES[number]}", font=bold,
              fill="#e6edf3")
    draw.text((WIDTH - 245, 40), "运行结果", font=small, fill="#8b949e")

    y = TOP_BAR + 28
    for line in lines:
        if line.startswith("$"):
            color = "#79c0ff"
        elif line.startswith("+"):
            color = "#d2a8ff"
        elif "not found" in line.lower() or "cannot access" in line.lower():
            color = "#ff7b72"
        elif line in {"success", "fallback", "identical"} or line.startswith("File exists"):
            color = "#7ee787"
        else:
            color = "#e6edf3"
        draw.text((PAD_X, y), line, font=font, fill=color)
        y += line_height

    out_path = OUTPUT_DIR / f"practice-ex{number:02d}.png"
    image.save(out_path, optimize=True)
    print(out_path)
