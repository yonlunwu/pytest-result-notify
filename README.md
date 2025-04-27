# pytest-result-notify

一个用于将 Pytest 测试结果通知到 Slack 的工具。

## 安装

使用 `pdm` 进行依赖管理。请确保你已经安装了 `pdm`，然后运行以下命令来安装项目依赖：

```bash
pdm install
```

- 如果尚未安装 pdm，可以通过以下命令安装：

```bash
pip install pdm
```

## 使用
### 格式化
```bash
pdm format
```

### 检查
```bash
pdm check
```

### 测试
```bash
pdm test -s
```

## 配置 slack 通知
1. 获取你的 Slack API Token。你需要在 Slack 上创建一个应用并获取一个有效的 API Token。
2. 设置环境变量 SLACK_API_TOKEN，将你的 Slack API Token 和 Slack URL 添加到环境变量中：
```bash
export SLACK_API_TOKEN='your_slack_api_token_here'
export SLACK_URL='your_slack_url_here'
```

## 完成示例
```bash
# 安装依赖
pdm install

# 格式化代码
pdm run format

# 检查代码
pdm run check

# 设置 Slack API 环境变量
export SLACK_API_TOKEN='your_slack_api_token_here'
export SLACK_URL='your_slack_url_here'

# 运行测试并发送结果到 Slack
pdm run test -s
```