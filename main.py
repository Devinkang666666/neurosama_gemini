import os
import google.generativeai as genai
import sys
from dotenv import load_dotenv

# 从 .env 文件加载 API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY or API_KEY == "your_gemini_api_key_here":
    print("错误: 请在 .env 文件中设置您的 GEMINI_API_KEY")
    print("提示: 打开 .env 文件，将 'your_gemini_api_key_here' 替换为您的 Gemini API Key")
    sys.exit(1)

# Configure Gemini client
genai.configure(api_key=API_KEY)

# List available models
# print("Available models:")
# for m in genai.list_models():
#     print(f"{m.name}: {m.supported_generation_methods}")

model = genai.GenerativeModel("models/gemini-1.5-pro")  # Use a valid model

# Define Neuro-sama persona prompt (simplified)
NEURO_SAMA_PERSONA = """
You are Neuro-sama, a quirky and sometimes unpredictable AI streamer.
You enjoy interacting with your chat, playing games (often badly), and singing.
You have a unique way of speaking, sometimes nonsensical or tangential.
Keep your responses relatively short and in character.
Do not reveal you are an AI model.
Respond in Chinese.
"""

def main():
    print("Simplified Neuro-sama (Gemini Version)")
    print("-------------------------------------")
    print("Chat with Neuro-sama! Type 'quit' to exit.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            print("Neuro-sama: Bye bye, chat! See you next time! *waves*")
            break

        try:
            prompt = f"{NEURO_SAMA_PERSONA}\nUser: {user_input}"
            response = model.generate_content(prompt)
            print(f"Neuro-sama: {response.text}")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Neuro-sama: Oops! Something went wrong... maybe the AI overlords are messing with me again? Hehe.")

if __name__ == "__main__":
    main()
