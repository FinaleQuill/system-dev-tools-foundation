# q10 AI 修复记录
- 核心提示：空白 `--name` 必须令 `main()` 以 `SystemExit(2)` 结束；先让测试失败，再修复并复跑。
- 智能体改动：新增 `tests/test_cli.py`，并在参数解析后用 `a.name.strip()` 判断空白名称、调用 `p.error(...)`。
- 失败验证：`python -m unittest discover -s tests -v` 报 `AssertionError: SystemExit not raised`。
- 人工验证：检查与 q09 的 diff 仅含该校验；复跑测试为 `OK`，直接调用的退出码为 `2`。
