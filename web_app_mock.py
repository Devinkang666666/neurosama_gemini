import os
import webbrowser
import threading
import time
import random
from flask import Flask, render_template_string, request, jsonify
from dotenv import load_dotenv

# 从 .env 文件加载 API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# 模拟回复列表
MOCK_RESPONSES = [
    "你好呀！我是神经酱！很高兴认识你！(*^▽^*)",
    "哎呀，这个问题有点难回答呢...让我想想...",
    "啊哈哈！这真的很有趣！我喜欢和你聊天！",
    "嗯...这个嘛...我不太确定，但我觉得应该是这样的！",
    "哇！这个问题真的很有深度呢！让我好好思考一下...",
    "我最喜欢玩游戏了！虽然我玩得不是很好，但是很开心！",
    "有时候我会唱歌，虽然不是很好听，但是很有感情！",
    "你知道吗？我觉得人工智能和人类可以成为很好的朋友！",
    "我有时候会说一些奇怪的话，但这就是我的风格！",
    "今天天气怎么样？我希望你有一个美好的一天！"
]

# 创建Flask应用
app = Flask(__name__)

# HTML模板
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>神经酱 Gemini | Neuro-sama Chat (模拟版)</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            color: #333;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            margin-bottom: 20px;
        }
        
        .header h1 {
            color: #6200ee;
            margin-bottom: 10px;
        }
        
        .chat-container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }
        
        .chat-messages {
            height: 400px;
            overflow-y: auto;
            padding: 20px;
        }
        
        .message {
            margin-bottom: 15px;
            max-width: 80%;
            clear: both;
        }
        
        .user-message {
            float: right;
        }
        
        .bot-message {
            float: left;
        }
        
        .message-content {
            padding: 10px 15px;
            border-radius: 18px;
            display: inline-block;
            word-break: break-word;
        }
        
        .user-message .message-content {
            background-color: #6200ee;
            color: white;
            border-top-right-radius: 5px;
        }
        
        .bot-message .message-content {
            background-color: #e0e0e0;
            color: black;
            border-top-left-radius: 5px;
        }
        
        .chat-input {
            display: flex;
            padding: 10px;
            border-top: 1px solid #eee;
        }
        
        .chat-input input {
            flex: 1;
            padding: 10px 15px;
            border: 1px solid #ddd;
            border-radius: 20px;
            font-size: 16px;
            outline: none;
        }
        
        .chat-input button {
            background-color: #6200ee;
            color: white;
            border: none;
            border-radius: 20px;
            padding: 10px 20px;
            margin-left: 10px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        
        .chat-input button:hover {
            background-color: #5000d6;
        }
        
        .typing-indicator {
            display: none;
            padding: 10px 15px;
            background-color: #e0e0e0;
            border-radius: 18px;
            margin-bottom: 15px;
            width: 60px;
            float: left;
            clear: both;
        }
        
        .typing-indicator span {
            height: 8px;
            width: 8px;
            float: left;
            margin: 0 1px;
            background-color: #9E9E9E;
            display: block;
            border-radius: 50%;
            opacity: 0.4;
            animation: typing 1s infinite;
        }
        
        .typing-indicator span:nth-of-type(1) {
            animation-delay: 0s;
        }
        
        .typing-indicator span:nth-of-type(2) {
            animation-delay: 0.2s;
        }
        
        .typing-indicator span:nth-of-type(3) {
            animation-delay: 0.4s;
        }
        
        @keyframes typing {
            0% { opacity: 0.4; }
            50% { opacity: 1; }
            100% { opacity: 0.4; }
        }
        
        .error {
            color: #d32f2f;
            text-align: center;
            margin-top: 10px;
            display: none;
        }
        
        .notice {
            background-color: #fff3cd;
            color: #856404;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 20px;
            text-align: center;
        }
        
        /* 响应式设计 */
        @media (max-width: 600px) {
            .container {
                padding: 10px;
            }
            
            .message {
                max-width: 90%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>神经酱 Gemini | Neuro-sama Chat</h1>
            <p>与神经酱聊天吧！她是一个古怪而有时不可预测的AI主播。</p>
        </div>
        
        <div class="notice">
            <strong>注意：</strong> 当前使用模拟回复模式，神经酱的回复是预设的，不是实时生成的。
        </div>
        
        <div class="chat-container">
            <div class="chat-messages" id="chat-messages">
                <div class="message bot-message">
                    <div class="message-content">
                        你好呀！我是神经酱！今天想聊些什么呢？(*^▽^*)
                    </div>
                </div>
                <div class="typing-indicator" id="typing-indicator">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
            
            <div class="chat-input">
                <input type="text" id="user-input" placeholder="在这里输入消息..." autocomplete="off">
                <button id="send-button">发送</button>
            </div>
        </div>
        
        <div class="error" id="error-message"></div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const chatMessages = document.getElementById('chat-messages');
            const userInput = document.getElementById('user-input');
            const sendButton = document.getElementById('send-button');
            const errorMessage = document.getElementById('error-message');
            const typingIndicator = document.getElementById('typing-indicator');

            // Focus on input when page loads
            userInput.focus();

            // Send message when button is clicked
            sendButton.addEventListener('click', sendMessage);

            // Send message when Enter key is pressed
            userInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    sendMessage();
                }
            });

            function sendMessage() {
                const message = userInput.value.trim();
                if (!message) return;

                // Add user message to chat
                addMessage(message, 'user');

                // Clear input
                userInput.value = '';

                // Disable input and button while waiting for response
                userInput.disabled = true;
                sendButton.disabled = true;

                // Show typing indicator
                typingIndicator.style.display = 'block';
                chatMessages.scrollTop = chatMessages.scrollHeight;

                // Hide any previous error
                errorMessage.style.display = 'none';

                // Send message to API
                fetch('/api/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ message: message })
                })
                .then(response => response.json())
                .then(data => {
                    // Hide typing indicator
                    typingIndicator.style.display = 'none';
                    
                    if (data.error) {
                        // Show error message
                        errorMessage.textContent = data.message;
                        errorMessage.style.display = 'block';
                    } else {
                        // Add bot message
                        addMessage(data.message, 'bot');
                    }
                    
                    // Re-enable input and button
                    userInput.disabled = false;
                    sendButton.disabled = false;
                    userInput.focus();
                })
                .catch(error => {
                    // Hide typing indicator
                    typingIndicator.style.display = 'none';
                    
                    // Show error message
                    errorMessage.textContent = '连接服务器时出错，请稍后再试。';
                    errorMessage.style.display = 'block';
                    
                    // Re-enable input and button
                    userInput.disabled = false;
                    sendButton.disabled = false;
                    userInput.focus();
                    
                    console.error('Error:', error);
                });
            }

            function addMessage(text, sender) {
                const messageDiv = document.createElement('div');
                messageDiv.className = `message ${sender}-message`;

                const messageContent = document.createElement('div');
                messageContent.className = 'message-content';
                messageContent.textContent = text;

                messageDiv.appendChild(messageContent);

                // Insert before typing indicator
                chatMessages.insertBefore(messageDiv, typingIndicator);

                // Scroll to bottom
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """提供聊天界面"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/chat', methods=['POST'])
def chat():
    """处理聊天请求（使用模拟回复）"""
    data = request.json
    user_input = data.get('message', '')

    if not user_input:
        return jsonify({
            'error': True,
            'message': '请输入消息'
        }), 400

    try:
        # 模拟思考时间
        time.sleep(1)
        
        # 随机选择一个回复
        response = random.choice(MOCK_RESPONSES)
        
        return jsonify({
            'error': False,
            'message': response
        })
    except Exception as e:
        return jsonify({
            'error': True,
            'message': f'发生错误: {str(e)}'
        }), 500

def open_browser_after_delay(url, delay=1.0):
    """等待一段时间后打开浏览器，确保服务器已经启动"""
    def _open_browser():
        time.sleep(delay)
        print(f"\n正在打开浏览器: {url}")
        webbrowser.open(url)
    
    # 在后台线程中打开浏览器
    threading.Thread(target=_open_browser, daemon=True).start()

def start_server(host='127.0.0.1', port=5000, debug=False, open_browser=True):
    """启动Flask服务器"""
    url = f"http://{host}:{port}"
    
    print("\n神经酱 Gemini Web聊天界面 (模拟版)")
    print("============================")
    print(f"服务器地址: {url}")
    print("按 Ctrl+C 停止服务器")
    
    # 延迟打开浏览器，确保服务器已经启动
    if open_browser:
        open_browser_after_delay(url)
    
    # 启动服务器
    app.run(host=host, port=port, debug=debug)

if __name__ == "__main__":
    try:
        start_server(debug=True)
    except KeyboardInterrupt:
        print("\n服务器已停止")
    except Exception as e:
        print(f"\n启动服务器时出错: {e}")
        import traceback
        traceback.print_exc()
        
        # 保持窗口打开
        input("\n按Enter键退出...")
