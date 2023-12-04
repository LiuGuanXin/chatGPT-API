import requests
import json

proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}
# Set the API endpoint and access token
api_endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"
access_token = "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"

# Set the prompt text and parameters
prompt_text = "Hello, how are you today?"
params = {
    "prompt": prompt_text,
    "temperature": 0.7,
    "max_tokens": 60,
    "top_p": 1,
    "frequency_penalty": 0.5,
    "presence_penalty": 0.0
}

# Send the API request
headers = {"Content-Type": "application/json",
           "Authorization": f"Bearer {access_token}"}
response = requests.post(api_endpoint, headers=headers, json=params, proxies=proxies)

# Process the API response
if response.status_code == 200:
    response_text = json.loads(response.text)["choices"][0]["text"]
    print(f"ChatGPT response: {response_text}")
else:
    print(f"Error: {response.status_code} - {response.text}")