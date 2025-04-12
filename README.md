# Neuro-sama Gemini | 秒神酱 Gemini

这是一个基于 Google Gemini AI 的秒神酱聊天机器人项目。它模拟了秒神酱的个性特征，可以进行有趣的对话交互。

This is a Neuro-sama chatbot project based on Google Gemini AI. It simulates Neuro-sama's personality traits and enables engaging conversations.

## 效果展示 | Demo

![秒神酱对话效果 | Neuro-sama Chat Demo](https://github.com/Devinkang666666/neurosama_gemini/raw/master/images/demo.png)

![秒神酱 Web界面 | Neuro-sama Web UI](https://github.com/Devinkang666666/neurosama_gemini/raw/master/images/web_ui.png)

## 功能特点 | Features

- 使用 Google Gemini 2.0 Flash 模型 | Uses Google Gemini 2.0 Flash model
- 模拟秒神酱的个性特征 | Simulates Neuro-sama's personality
- 支持中文对话 | Supports Chinese conversation
- 简单易用的命令行界面 | Simple and user-friendly CLI interface
- 美观的Web聊天界面 | Beautiful Web chat interface
- 自动打开浏览器 | Automatically opens browser

## 安装要求 | Requirements

- Python 3.7 或更高版本 | Python 3.7 or higher
- Google Gemini API 密钥 | Google Gemini API key

## 安装步骤 | Installation

1. 克隆仓库 | Clone the repository:
```bash
git clone https://github.com/Devinkang666666/neurosama_gemini.git
cd neurosama_gemini
```

2. 安装依赖 | Install dependencies:
```bash
pip install -r requirements.txt
```

3. 配置 API 密钥 | Configure API key:
   - 打开 `.env` 文件 | Open `.env` file
   - 将 `your_gemini_api_key_here` 替换为您的 Gemini API 密钥 | Replace `your_gemini_api_key_here` with your Gemini API key
   - 保存文件 | Save the file

## 使用方法 | Usage

### 命令行界面 | Command Line Interface

1. 运行程序 | Run the program:
```bash
python main.py
```
或者双击 | Or double-click: `run_chat.bat`

2. 开始对话 | Start chatting:
   - 直接输入文字与 Neuro-sama 对话 | Type directly to chat with Neuro-sama
   - 输入 'quit' 退出程序 | Type 'quit' to exit

### Web界面 | Web Interface

1. 运行 Web 版本 | Run the Web version:
```bash
python web_app.py
```
或者双击 | Or double-click: `run_web_app.bat`

2. 浏览器将自动打开，显示聊天界面 | Browser will automatically open showing the chat interface

3. 在输入框中输入消息，点击“发送”按钮或按Enter键发送 | Type your message in the input box, click "Send" button or press Enter to send

详细说明请参考 [Web UI 使用指南](WEB_UI_GUIDE.md) | For detailed instructions, see [Web UI Guide](WEB_UI_GUIDE.md)

### 模拟版本（无需API密钥） | Mock Version (No API Key Required)

如果您没有API密钥或想快速测试界面，可以运行模拟版本 | If you don't have an API key or want to quickly test the interface, you can run the mock version:

```bash
python web_app_mock.py
```
或者双击 | Or double-click: `run_web_app_mock.bat`

## 注意事项 | Notes

- 请确保您有有效的 Google Gemini API 密钥 | Make sure you have a valid Google Gemini API key
- API 密钥请妥善保管，不要分享给他人 | Keep your API key secure and don't share it with others
- 建议在 `.env` 文件中设置 API 密钥，而不是直接在代码中硬编码 | It's recommended to set the API key in the `.env` file rather than hardcoding it

## 项目结构 | Project Structure

```
neurosama_gemini/
├── main.py           # 命令行主程序文件 | CLI main program file
├── web_app.py        # Web界面程序文件 | Web interface program file
├── web_app_mock.py   # 模拟版Web界面 | Mock version of Web interface
├── test_api_key.py   # API密钥测试工具 | API key testing tool
├── run_chat.bat      # 命令行启动批处理文件 | CLI launcher batch file
├── run_web_app.bat   # Web界面启动批处理文件 | Web interface launcher
├── run_web_app_mock.bat # 模拟版启动文件 | Mock version launcher
├── test_api_key.bat  # API密钥测试启动文件 | API key test launcher
├── requirements.txt  # 项目依赖 | Project dependencies
├── .env             # API 密钥配置文件 | API key configuration file
└── .gitignore       # Git 忽略文件 | Git ignore file
```

## 贡献 | Contributing

欢迎提交 Issue 和 Pull Request 来帮助改进项目！
Welcome to submit Issues and Pull Requests to help improve the project!

## 许可证 | License

MIT License