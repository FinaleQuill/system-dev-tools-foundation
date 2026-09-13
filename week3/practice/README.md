# 第 3 周课后练习记录

本目录保存报告中选做的 10 个课后练习的输入、命令或结果。练习按课程网页的编号选择：

| 实例 | 来源练习 | 内容 | 结果 |
|---|---|---|---|
| 1 | Packaging 1 | 比较虚拟环境激活前后的环境变量 | .venv\Scripts 置于 PATH 前，VIRTUAL_ENV 已设置 |
| 2 | Packaging 2 | 从本地 Wheel 安装包并生成依赖锁定记录 | 安装成功，requirements.lock 记录本地 Wheel 与哈希 |
| 3 | Packaging 4 | 为简单 Python 服务编写 Dockerfile 和 Compose 配置 | 配置文件完成；本机未安装 Docker，未执行容器 |
| 4 | Agentic 1 | 比较手写、补全、内联聊天和智能体实现小功能的体验 | 见报告中的对比结论 |
| 5 | Agentic 2 | 让智能体阅读陌生的 greetlab 包并概括入口流程 | 确认 pyproject.toml 将 sdt-greet 指向 greetlab.cli:main |
| 6 | Agentic 3 | 使用智能体氛围编程一个小型问候页 | ex06-vibe-greeting/index.html 可直接在浏览器打开 |
| 7 | Agentic 5 | 不直接改写 Markdown，以 rg 提取无序列表项 | 输出保存在 ex07-markdown/list-items.txt |
| 8 | Beyond Code 2 | 对比仓库中较强与较弱的提交信息 | 见 ex08-git-history.md |
| 9 | Beyond Code 5 | 用 q10 的空白名称场景整理最小可复现示例 | 测试先失败后通过，退出码为 2 |
| 10 | Beyond Code 3 | 对比三个知名项目的 README 信息结构 | 见 ex10-readme-comparison.md |

练习 4、5、8、9、10 的分析结论已写入实验报告，相关源文件保留在 q09、q10 和本目录中。
