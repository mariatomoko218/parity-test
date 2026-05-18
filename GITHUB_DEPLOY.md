# 把 parity-test 发布到 GitHub（10 分钟，零成本）

## 步骤 1：注册 GitHub 组织账号
- 如果还没有，注册 https://github.com/join
- 推荐**直接创建组织** `token998`（免费版组织即可）
- 组织页：https://github.com/token998

## 步骤 2：创建 Repo
1. 组织页 → New repository
2. 名称：`parity-test`
3. 描述：`Open-source proof that token998.com does not swap models or harvest prompts.`
4. **Public**（必须公开，这是信任锚的核心）
5. 不要勾选 Initialize（我们已有文件）
6. Create repository

## 步骤 3：上传文件（最简单方式）

进入新建的 `token998/parity-test` repo 页面 → 点 **uploading an existing file** 链接 → 把以下文件全部拖进去：

```
parity_test.py
requirements.txt
README.md
SLA.md
LICENSE
CONTRIBUTING.md
.gitignore
```

Commit message：`Initial release: parity test v1.0`

点 Commit。

## 步骤 4：配置 Repo 元信息
1. 进入 repo → 右侧 ⚙️ 设置 About:
   - Description: `Open-source parity test for token998.com — proving no model substitution`
   - Website: `https://token998.com`
   - Topics: 添加 `openai-api`, `claude-api`, `deepseek`, `openrouter-alternative`, `ai-relay`, `transparency`

2. Settings → Discussions → Enable（让用户公开提问）

## 步骤 5：钉一条 README Star 引导
- README 顶部已经有徽章和说明，无需额外操作
- 第一周可以在 Reddit /r/LocalLLaMA 和 /r/ChatGPTCoding 发一条："I open-sourced my AI relay's parity test, audit me"，自然获得 30-100 star

## 步骤 6：在主站和落地页放上 GitHub 链接
- 中文主站 footer：「开源审计 → github.com/token998/parity-test」
- 英文落地页：已经内置 ✅

---

## 进阶（第二周）：加 GitHub Actions 自动化测试
让 CI 每天自动运行 parity-test，结果发到 README 徽章。
这一步等首月 MVP 数据出来后再做，现在不是优先级。

---

## 期望效果

| 时间 | 预期指标 |
|------|---------|
| 第 1 周 | 5-15 star，3-5 个 issue（用户来玩） |
| 第 1 月 | 30-100 star，被 OpenRouter 替代者列表收录 |
| 第 3 月 | 200+ star，成为"中国 AI relay 中可信赖者"的参考标杆 |

**这是你和"灰产中转"切割开的最关键资产。**
