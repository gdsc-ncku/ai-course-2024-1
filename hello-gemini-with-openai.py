import os

from openai import OpenAI
from dotenv import load_dotenv      # 讀取環境變數
from rich import print  

load_dotenv() # 讀取環境變數

# 使用 google generative ai
client = OpenAI(
    api_key=os.getenv('GEMINI_API_KEY'),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-1.5-flash", # 記得改模型
    messages=[
        {"role": "user", "content": "你覺得海狸大師怎麼樣？"}
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end="")