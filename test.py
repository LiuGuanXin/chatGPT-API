import requests
import json
from dotenv import load_dotenv
import os


class Chat:
    def __init__(self):
        load_dotenv()
        self.prompt_text = prompt_text
        self.api_key = os.getenv('OPENAI_API_KEY')
        proxy = os.getenv('PROXY')
        self.proxies = {
            'http': proxy,
            'https': proxy,
        }
        # API 请求的头部信息
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        # 指定模型的 API 端点
        self.api_endpoint = os.getenv('API_ENDPOINT')

    def chat(self, prompt_text, headers=None):
        if headers is None:
            headers = self.headers
        params = {
            "prompt": prompt_text,
            "temperature": 0.7,
            "max_tokens": 60,
            "top_p": 1,
            "frequency_penalty": 0.5,
            "presence_penalty": 0.0
        }
        # 发送 API 请求
        response = requests.post(self.api_endpoint, headers=headers, json=params, proxies=self.proxies)
        # 处理 API 响应
        if response.status_code == 200:
            response_text = json.loads(response.text)["choices"][0]["text"]
            print(f"ChatGPT 响应: {response_text}")
        else:
            print(f"错误: {response.status_code} - {response.text}")


if __name__ == '__main__':
    # 提示文本和参数
    prompt_text = "我给你发一段描述，你帮我翻译成AI绘画能识别的单词；一个漂亮的女孩在沙滩晒太阳，天空晴朗，大海湛蓝色，卷起朵朵浪花"
    textChat = Chat()
    textChat.chat(prompt_text)
