# Issue

**环境**：待确认（操作系统、Python版本）
**复现命令**：`sdt-greet --name " "`
**期望结果**：程序应以退出码 2 终止，不输出任何内容。
**实际结果**：输出 `Hello, !`，退出码 0。

**说明**：当前未对仅含空白字符的 `--name` 做校验，导致空姓名仍被视为合法输入，与预期行为不符。

---

# 提交信息
fix: exit with code 2 when name is blank

The program currently outputs "Hello, !" and exits with 0 when the
--name argument consists solely of whitespace. This violates the
specification that blank names should be rejected with a non-zero exit
code.

Add a check using str.isspace() and call sys.exit(2) in that case.


---

# 评审意见

**Blocking** – `cli.py` 中的 `main()` 未对 `a.name` 进行空白校验。
**行为**：`" "` 直接传入 `print(f"Hello, {a.name}!")`，输出空值且退出码为0。
**风险**：依赖退出码的脚本（如 CI/CD）无法检测到无效输入，可能引发后续流程错误。
**建议**：在打印前添加 `if not a.name or a.name.isspace(): sys.exit(2)`，并导入 `sys`。
