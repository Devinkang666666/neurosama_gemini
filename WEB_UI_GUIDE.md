# 秒神酱 Gemini Web UI 使用指南

本文档提供了秒神酱 Gemini Web 聊天界面的详细安装和使用说明。

## 功能特点

- 美观的聊天界面
- 实时响应
- 自动打开浏览器
- 支持中文交流
- 秒神酱人格设定
- 模拟版本（无需API密钥）

## 安装

### 前提条件

- Python 3.7 或更高版本
- pip 包管理器

### 安装依赖

```bash
pip install -r requirements.txt
```

或者手动安装：

```bash
pip install flask google-generativeai python-dotenv
```

### 设置API密钥

1. 获取 Google Gemini API 密钥：
   - 访问 [Google AI Studio](https://makersuite.google.com/app/apikey)
   - 登录您的Google账户
   - 点击"创建API密钥"按钮
   - 复制生成的API密钥

2. 设置环境变量：
   - 在项目根目录创建 `.env` 文件
   - 添加以下内容：
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```
   - 将 `your_gemini_api_key_here` 替换为您的 Google Gemini API 密钥
   - 保存文件

## 使用方法

### 启动Web界面

#### 方法1：使用Python命令

```bash
python web_app.py
```

#### 方法2：使用批处理文件（Windows）

双击 `run_web_app.bat` 文件

### 使用模拟版本（无需API密钥）

如果您没有API密钥或想快速测试界面，可以运行模拟版本：

#### 方法1：使用Python命令

```bash
python web_app_mock.py
```

#### 方法2：使用批处理文件（Windows）

双击 `run_web_app_mock.bat` 文件

### 与秒神酱交流

1. 启动应用后，浏览器将自动打开，显示聊天界面
2. 在底部输入框中输入您的消息
3. 点击"发送"按钮或按Enter键发送消息
4. 等待秒神酱的回复

## 界面说明

![Web UI界面](images/web_ui.png)

1. **标题栏**：显示"秒神酱 Gemini | Neuro-sama Chat"
2. **聊天区域**：显示您与秒神酱的对话历史
3. **输入框**：输入您想发送的消息
4. **发送按钮**：点击发送消息
5. **打字指示器**：显示秒神酱正在输入的动画

## 常见问题

### 浏览器没有自动打开

如果浏览器没有自动打开，请手动访问：http://localhost:5000

### API密钥无效

如果您收到"API key not valid"错误，请检查：
1. `.env` 文件中的API密钥是否正确
2. API密钥是否已启用 Google Generative AI (Gemini) API
3. API密钥是否已过期或达到使用限制

您可以使用 `test_api_key.py` 工具测试API密钥是否有效：

```bash
python test_api_key.py
```

或双击 `test_api_key.bat` 文件

### 无法连接到服务器

如果您看到"无法连接到服务器"错误，请检查：
1. 应用程序是否正在运行
2. 端口5000是否被其他应用程序占用
3. 防火墙是否阻止了应用程序

### 使用模拟版本

如果您遇到API相关问题，可以使用模拟版本进行测试：

```bash
python web_app_mock.py
```

模拟版本使用预设的回复列表，不需要API密钥。

## 自定义

### 修改端口

如果端口5000被占用，您可以修改 `web_app.py` 或 `web_app_mock.py` 文件中的端口号：

```python
start_server(host='127.0.0.1', port=8080, debug=True)
```

### 修改秒神酱人格

您可以修改 `web_app.py` 或 `web_app_mock.py` 文件中的 `MIAOSHEN_PERSONA` 变量来自定义秒神酱的人格设定。

## 技术细节

- 前端：HTML, CSS, JavaScript
- 后端：Flask (Python)
- API：Google Gemini API
- 通信：AJAX (fetch API)

## 注意事项

- API密钥有使用限制，请合理使用
- 不要在公共场合分享您的API密钥
- 应用程序仅供个人使用，请遵守Google Gemini API的使用条款
