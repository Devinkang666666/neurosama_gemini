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
    "你好呀！我是秒神酱！很高兴认识你！(*^▽^*)",
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
    <title>秒神酱 Gemini | Neuro-sama Chat (模拟版)</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
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

        .chat-buttons {
            display: flex;
            margin-left: 5px;
        }

        .chat-input button {
            background-color: #6200ee;
            color: white;
            border: none;
            border-radius: 20px;
            padding: 10px 15px;
            margin-left: 5px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }

        .chat-input button:hover {
            background-color: #5000d6;
        }

        .chat-input button:disabled {
            background-color: #9e9e9e;
            cursor: not-allowed;
        }

        #voice-input-button {
            background-color: #4caf50;
        }

        #voice-input-button:hover {
            background-color: #388e3c;
        }

        #voice-input-button.recording {
            background-color: #f44336;
            animation: pulse 1.5s infinite;
        }

        #voice-output-toggle {
            background-color: #2196f3;
        }

        #voice-output-toggle:hover {
            background-color: #1976d2;
        }

        #voice-output-toggle.voice-disabled {
            background-color: #9e9e9e;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
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
            <h1>秒神酱 Gemini | Neuro-sama Chat</h1>
            <p>与秒神酱聊天吧！她是一个古怪而有时不可预测的AI主播。</p>
        </div>

        <div class="notice">
            <strong>注意：</strong> 当前使用模拟回复模式，秒神酱的回复是预设的，不是实时生成的。
        </div>

        <div class="chat-container">
            <div class="chat-messages" id="chat-messages">
                <div class="message bot-message">
                    <div class="message-content">
                        你好呀！我是秒神酱！今天想聊些什么呢？(*^▽^*)
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
                <div class="chat-buttons">
                    <button id="voice-input-button" title="语音输入"><i class="fas fa-microphone"></i></button>
                    <button id="send-button">发送</button>
                    <button id="voice-output-toggle" title="语音输出" class="voice-enabled"><i class="fas fa-volume-up"></i></button>
                </div>
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
            const voiceInputButton = document.getElementById('voice-input-button');
            const voiceOutputToggle = document.getElementById('voice-output-toggle');

            // 语音识别相关变量
            let recognition = null;
            let isRecording = false;

            // 语音合成相关变量
            let speechSynthesis = window.speechSynthesis;
            let voiceOutputEnabled = true;
            let voices = [];

            // 初始化语音合成
            function initSpeechSynthesis() {
                if (speechSynthesis) {
                    // Chrome需要等待onvoiceschanged事件
                    speechSynthesis.onvoiceschanged = function() {
                        voices = speechSynthesis.getVoices();
                    };

                    // 首次加载获取可用语音
                    voices = speechSynthesis.getVoices();
                }
            }

            // 初始化语音合成
            initSpeechSynthesis();

            // 检查浏览器是否支持语音识别
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (SpeechRecognition) {
                recognition = new SpeechRecognition();
                recognition.continuous = false;
                recognition.interimResults = false;

                // 根据浏览器语言设置语音识别语言
                const isChineseLanguage = /^zh/.test(navigator.language);
                recognition.lang = isChineseLanguage ? 'zh-CN' : 'en-US';

                recognition.onresult = function(event) {
                    const transcript = event.results[0][0].transcript;
                    userInput.value = transcript;
                    stopRecording();
                };

                recognition.onerror = function(event) {
                    console.error('Speech recognition error', event.error);
                    stopRecording();
                    errorMessage.textContent = '语音识别出错，请再试一次。';
                    errorMessage.style.display = 'block';
                };

                recognition.onend = function() {
                    stopRecording();
                };
            } else {
                voiceInputButton.style.display = 'none';
                console.warn('Browser does not support speech recognition.');
            }

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

            // 语音输入按钮点击事件
            if (voiceInputButton) {
                voiceInputButton.addEventListener('click', function() {
                    if (isRecording) {
                        stopRecording();
                    } else {
                        startRecording();
                    }
                });
            }

            // 语音输出开关点击事件
            voiceOutputToggle.addEventListener('click', function() {
                voiceOutputEnabled = !voiceOutputEnabled;
                if (voiceOutputEnabled) {
                    voiceOutputToggle.classList.remove('voice-disabled');
                    voiceOutputToggle.innerHTML = '<i class="fas fa-volume-up"></i>';
                } else {
                    voiceOutputToggle.classList.add('voice-disabled');
                    voiceOutputToggle.innerHTML = '<i class="fas fa-volume-mute"></i>';
                    // 停止正在进行的语音输出
                    speechSynthesis.cancel();
                }
            });

            // 开始语音输入
            function startRecording() {
                if (!recognition) return;

                try {
                    recognition.start();
                    isRecording = true;
                    voiceInputButton.classList.add('recording');
                    voiceInputButton.innerHTML = '<i class="fas fa-stop"></i>';
                    errorMessage.style.display = 'none';
                } catch (error) {
                    console.error('Error starting speech recognition:', error);
                }
            }

            // 停止语音输入
            function stopRecording() {
                if (!recognition) return;

                try {
                    recognition.stop();
                } catch (error) {
                    console.error('Error stopping speech recognition:', error);
                }

                isRecording = false;
                voiceInputButton.classList.remove('recording');
                voiceInputButton.innerHTML = '<i class="fas fa-microphone"></i>';
            }

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

                        // 语音输出机器人的回复
                        if (voiceOutputEnabled && speechSynthesis) {
                            speakText(data.message);
                        }
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

            // 语音合成函数
            function speakText(text) {
                if (!speechSynthesis) return;

                // 停止正在进行的语音输出
                speechSynthesis.cancel();

                // 处理文本，增加情感表达
                text = addEmotionToText(text);

                const utterance = new SpeechSynthesisUtterance(text);

                // 检测语言
                const isChineseText = /[\u4e00-\u9fa5]/.test(text);

                // 使用初始化时获取的voices变量
                // 如果还没有加载完成，再次尝试获取
                if (voices.length === 0) {
                    const availableVoices = speechSynthesis.getVoices();
                    if (availableVoices.length > 0) {
                        voices = availableVoices;
                    }
                }

                // 输出可用的语音列表，便于调试
                console.log('Available voices:', voices.map(v => `${v.name} (${v.lang})`));

                if (isChineseText) {
                    // 中文文本处理
                    // 尝试找到最适合的中文女声
                    let chineseVoice = voices.find(voice =>
                        (voice.lang === 'zh-CN' || voice.lang === 'zh_CN') &&
                        (voice.name.includes('Female') || voice.name.includes('女') ||
                         voice.name.includes('Xiaoxiao') || voice.name.includes('Yaoyao') ||
                         voice.name.includes('Huihui')));

                    // 如果没有找到精确匹配，尝试寻找包含'zh'的任何女声
                    if (!chineseVoice) {
                        chineseVoice = voices.find(voice =>
                            voice.lang.includes('zh') &&
                            (voice.name.includes('Female') || voice.name.includes('女')));
                    }

                    // 如果还是没有找到，尝试任何中文语音
                    if (!chineseVoice) {
                        chineseVoice = voices.find(voice => voice.lang.includes('zh'));
                    }

                    if (chineseVoice) {
                        utterance.voice = chineseVoice;
                        console.log('Using voice:', chineseVoice.name, chineseVoice.lang);
                    } else {
                        console.warn('No suitable Chinese voice found');
                    }

                    utterance.lang = 'zh-CN';

                    // 中文语音参数调整
                    utterance.volume = 1.0;   // 音量最大
                    utterance.rate = 0.9;     // 说话速度稍慢，更自然
                    utterance.pitch = 1.3;    // 高一点的音调更可爱
                } else {
                    // 英文文本处理
                    // 尝试找到最适合的英文女声
                    let englishVoice = voices.find(voice =>
                        (voice.lang === 'en-US' || voice.lang === 'en_US') &&
                        (voice.name.includes('Female') || voice.name.includes('Samantha') ||
                         voice.name.includes('Zira') || voice.name.includes('Hazel') ||
                         voice.name.includes('Siri')));

                    // 如果没有找到精确匹配，尝试寻找包含'en'的任何女声
                    if (!englishVoice) {
                        englishVoice = voices.find(voice =>
                            voice.lang.includes('en') &&
                            (voice.name.includes('Female') || voice.name.includes('female')));
                    }

                    // 如果还是没有找到，尝试任何英文语音
                    if (!englishVoice) {
                        englishVoice = voices.find(voice => voice.lang.includes('en'));
                    }

                    if (englishVoice) {
                        utterance.voice = englishVoice;
                        console.log('Using voice:', englishVoice.name, englishVoice.lang);
                    } else {
                        console.warn('No suitable English voice found');
                    }

                    utterance.lang = 'en-US';

                    // 英文语音参数调整
                    utterance.volume = 1.0;   // 音量最大
                    utterance.rate = 0.95;    // 说话速度稍慢，更自然
                    utterance.pitch = 1.2;    // 高一点的音调更可爱
                }

                // 添加语音事件处理
                utterance.onstart = function(event) {
                    console.log('Speech started');
                };

                utterance.onerror = function(event) {
                    console.error('Speech error:', event.error);
                };

                utterance.onend = function(event) {
                    console.log('Speech ended');
                };

                // 开始语音合成
                speechSynthesis.speak(utterance);
            }

            // 增加文本情感表达
            function addEmotionToText(text) {
                // 检测是否为中文
                const isChineseText = /[\u4e00-\u9fa5]/.test(text);

                if (isChineseText) {
                    // 为中文添加语气词和停顿
                    text = text.replace(/\!+/g, '! <break time="0.3s"/>');
                    text = text.replace(/\?+/g, '? <break time="0.3s"/>');
                    text = text.replace(/\~+/g, '~ <break time="0.2s"/>');
                    text = text.replace(/\.\.\./g, '... <break time="0.5s"/>');

                    // 添加情感标记
                    text = text.replace(/\*\^\u25bd\^\*/g, '<emphasis level="strong">哈哈哈</emphasis> <break time="0.2s"/>');
                    text = text.replace(/\(\*\^\u25bd\^\*\)/g, '<emphasis level="strong">哈哈哈</emphasis> <break time="0.2s"/>');

                    // 在句子结尾添加停顿
                    text = text.replace(/([\u4e00-\u9fa5])\s*([\u3002\uff01\uff1f])/g, '$1$2 <break time="0.4s"/>');

                    // 在逗号处添加短停顿
                    text = text.replace(/([\u4e00-\u9fa5])\s*([\uff0c\u3001])/g, '$1$2 <break time="0.2s"/>');

                    // 将文本包裹在SSML标记中
                    text = `<speak>${text}</speak>`;
                } else {
                    // 为英文添加语气词和停顿
                    text = text.replace(/\!+/g, '! <break time="0.3s"/>');
                    text = text.replace(/\?+/g, '? <break time="0.3s"/>');
                    text = text.replace(/\~+/g, '~ <break time="0.2s"/>');
                    text = text.replace(/\.\.\./g, '... <break time="0.5s"/>');

                    // 添加情感标记
                    text = text.replace(/haha/gi, '<emphasis level="strong">haha</emphasis> <break time="0.2s"/>');
                    text = text.replace(/lol/gi, '<emphasis level="strong">lol</emphasis> <break time="0.2s"/>');

                    // 在句子结尾添加停顿
                    text = text.replace(/([a-zA-Z])\s*([.!?])/g, '$1$2 <break time="0.4s"/>');

                    // 在逗号处添加短停顿
                    text = text.replace(/([a-zA-Z])\s*,/g, '$1, <break time="0.2s"/>');

                    // 将文本包裹在SSML标记中
                    text = `<speak>${text}</speak>`;
                }

                return text;
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
