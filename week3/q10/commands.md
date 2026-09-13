# q10 执行命令记录

## 1. 先运行失败测试

```powershell
PS week3\q10> python -m unittest discover -s tests -v
```

结果：失败（`AssertionError: SystemExit not raised`），原程序输出 `Hello,    !`。

## 2. 修复后运行测试与退出码验证

```powershell
PS week3\q10> python -m unittest discover -s tests -v
PS week3\q10> python -c "import sys; sys.path.insert(0, 'src'); from greetlab.cli import main; sys.argv=['sdt-greet','--name','   ']; main()"
PS week3\q10> echo $LASTEXITCODE
```

结果：单元测试通过；第二条命令打印 argparse 错误信息，并以退出码 `2` 结束。

## 3. 人工检查

```powershell
PS week3\q10> git diff --no-index -- ..\q09\q09\src\greetlab\cli.py src\greetlab\cli.py
```

结果：只有空白名称校验的两行新增，未发现无关改动。
