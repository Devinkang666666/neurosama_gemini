# Neuro-sama Gemini | 神经酱 Gemini

这是一个基于 Google Gemini AI 的 Neuro-sama 聊天机器人项目。它模拟了 Neuro-sama 的个性特征，可以进行有趣的对话交互。

This is a Neuro-sama chatbot project based on Google Gemini AI. It simulates Neuro-sama's personality traits and enables engaging conversations.

## 效果展示 | Demo

![Neuro-sama 对话效果 | Neuro-sama Chat Demo](https://github.com/Devinkang666666/neurosama_gemini/raw/master/images/demo.png)

## 功能特点 | Features

- 使用 Google Gemini 1.5 Pro 模型 | Uses Google Gemini 1.5 Pro model
- 模拟 Neuro-sama 的个性特征 | Simulates Neuro-sama's personality
- 支持中文对话 | Supports Chinese conversation
- 简单易用的命令行界面 | Simple and user-friendly CLI interface

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

1. 运行程序 | Run the program:
```bash
python main.py
```

2. 开始对话 | Start chatting:
   - 直接输入文字与 Neuro-sama 对话 | Type directly to chat with Neuro-sama
   - 输入 'quit' 退出程序 | Type 'quit' to exit

## 注意事项 | Notes

- 请确保您有有效的 Google Gemini API 密钥 | Make sure you have a valid Google Gemini API key
- API 密钥请妥善保管，不要分享给他人 | Keep your API key secure and don't share it with others
- 建议在 `.env` 文件中设置 API 密钥，而不是直接在代码中硬编码 | It's recommended to set the API key in the `.env` file rather than hardcoding it

## 项目结构 | Project Structure

```
neurosama_gemini/
├── main.py           # 主程序文件 | Main program file
├── requirements.txt  # 项目依赖 | Project dependencies
├── .env             # API 密钥配置文件 | API key configuration file
└── .gitignore       # Git 忽略文件 | Git ignore file
```

## 贡献 | Contributing

欢迎提交 Issue 和 Pull Request 来帮助改进项目！
Welcome to submit Issues and Pull Requests to help improve the project!

## 许可证 | License

MIT License 