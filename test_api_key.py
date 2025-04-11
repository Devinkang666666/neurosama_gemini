import os
import google.generativeai as genai
from dotenv import load_dotenv

# 从 .env 文件加载 API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

print("测试Google Gemini API密钥")
print("========================")

# 检查API密钥
if not API_KEY:
    print("错误: 未找到API密钥")
    exit(1)

print(f"API密钥: {API_KEY[:5]}*****{API_KEY[-5:]}")

# 配置Gemini客户端
try:
    print("\n正在配置Gemini客户端...")
    genai.configure(api_key=API_KEY)
    print("Gemini客户端配置成功")
except Exception as e:
    print(f"配置Gemini客户端时出错: {e}")
    exit(1)

# 创建模型
try:
    print("\n正在创建模型...")
    model = genai.GenerativeModel("models/gemini-1.5-pro")
    print("模型创建成功")
except Exception as e:
    print(f"创建模型时出错: {e}")
    exit(1)

# 测试生成内容
try:
    print("\n正在测试API...")
    response = model.generate_content("Hello, world!")
    print("API测试成功")
    print(f"响应: {response.text}")
    print("\nAPI密钥有效，可以正常使用。")
except Exception as e:
    print(f"测试API时出错: {e}")
    print("\nAPI密钥无效或出现其他错误。")
    exit(1)

input("\n按Enter键退出...")
