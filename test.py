import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
proxy = os.getenv('PROXY')
proxies = {
    'http': proxy,
    'https': proxy,
}
# 指定模型的 API 端点
api_endpoint = os.getenv('API_ENDPOINT')

# 提示文本和参数
prompt_text = "我给你发一段描述，你帮我翻译成AI绘画能识别的单词；一个漂亮的女孩在沙滩晒太阳，天空晴朗，大海湛蓝色，卷起朵朵浪花"
params = {
    "prompt": prompt_text,
    "temperature": 0.7,
    "max_tokens": 60,
    "top_p": 1,
    "frequency_penalty": 0.5,
    "presence_penalty": 0.0
}

# API 请求的头部信息
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# 发送 API 请求
response = requests.post(api_endpoint, headers=headers, json=params, proxies=proxies)

# 处理 API 响应
if response.status_code == 200:
    response_text = json.loads(response.text)["choices"][0]["text"]
    print(f"ChatGPT 响应: {response_text}")
else:
    print(f"错误: {response.status_code} - {response.text}")