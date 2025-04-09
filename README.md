# Neuro-sama Gemini

这是一个基于 Google Gemini AI 的 Neuro-sama 聊天机器人项目。它模拟了 Neuro-sama 的个性特征，可以进行有趣的对话交互。

## 效果展示

![Neuro-sama 对话效果](https://github.com/Devinkang666666/neurosama_gemini/raw/master/images/demo.png)

## 功能特点

- 使用 Google Gemini 1.5 Pro 模型
- 模拟 Neuro-sama 的个性特征
- 支持中文对话
- 简单易用的命令行界面

## 安装要求

- Python 3.7 或更高版本
- Google Gemini API 密钥

## 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/Devinkang666666/neurosama_gemini.git
cd neurosama_gemini
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置 API 密钥：
   - 打开 `.env` 文件
   - 将 `your_gemini_api_key_here` 替换为您的 Gemini API 密钥
   - 保存文件

## 使用方法

1. 运行程序：
```bash
python main.py
```

2. 开始对话：
   - 直接输入文字与 Neuro-sama 对话
   - 输入 'quit' 退出程序

## 注意事项

- 请确保您有有效的 Google Gemini API 密钥
- API 密钥请妥善保管，不要分享给他人
- 建议在 `.env` 文件中设置 API 密钥，而不是直接在代码中硬编码

## 项目结构

```
neurosama_gemini/
├── main.py           # 主程序文件
├── requirements.txt  # 项目依赖
├── .env             # API 密钥配置文件
└── .gitignore       # Git 忽略文件
```

## 贡献

欢迎提交 Issue 和 Pull Request 来帮助改进项目！

## 许可证

MIT License 