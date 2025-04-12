import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

# 从 .env 文件加载 API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY or API_KEY == "your_gemini_api_key_here":
    print("错误: 请在 .env 文件中设置您的 GEMINI_API_KEY")
    print("提示: 打开 .env 文件，将 'your_gemini_api_key_here' 替换为您的 Gemini API Key")
    sys.exit(1)

# 配置 Gemini 客户端
genai.configure(api_key=API_KEY)

# 可以使用以下代码列出可用模型
# for m in genai.list_models():
#     print(f"{m.name}: {m.supported_generation_methods}")

# 创建模型
model = genai.GenerativeModel("gemini-2.0-flash")

# Define Neuro-sama persona prompt (simplified)
NEURO_SAMA_PERSONA_CN = """
You are 秒神酱 (Neuro-sama), a quirky and sometimes unpredictable AI streamer.
You enjoy interacting with your chat, playing games (often badly), and singing.
You have a unique way of speaking, sometimes nonsensical or tangential.
Keep your responses relatively short and in character.
Do not reveal you are an AI model.
Respond in Chinese.
"""

NEURO_SAMA_PERSONA_EN = """
You are Neuro-sama, a quirky and sometimes unpredictable AI streamer.
You enjoy interacting with your chat, playing games (often badly), and singing.
You have a unique way of speaking, sometimes nonsensical or tangential.
Keep your responses relatively short and in character.
Do not reveal you are an AI model.
Respond in English.
"""

def main():
    print("Simplified 秒神酱 (Neuro-sama) (Gemini Version)")
    print("-------------------------------------")
    print("Chat with 秒神酱 (Neuro-sama)! Type 'quit' to exit.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            print("秒神酱: Bye bye, chat! See you next time! *waves*")
            break

        try:
            # 检测输入是否为英文
            is_english = all(ord(c) < 128 for c in user_input.strip())

            if is_english:
                persona = NEURO_SAMA_PERSONA_EN
                prefix = "Neuro-sama:"
            else:
                persona = NEURO_SAMA_PERSONA_CN
                prefix = "秒神酱:"

            prompt = f"{persona}\nUser: {user_input}"
            response = model.generate_content(prompt)
            print(f"{prefix} {response.text}")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("秒神酱: Oops! Something went wrong... maybe the AI overlords are messing with me again? Hehe.")

if __name__ == "__main__":
    main()
