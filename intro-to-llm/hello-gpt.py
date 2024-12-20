import os

from openai import OpenAI
from dotenv import load_dotenv      # 讀取環境變數
from rich import print  

load_dotenv() # 讀取環境變數

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY')) # 設定 OpenAI API

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "你覺得海狸大師怎麼樣？"}
    ]
)

print(response.choices[0].message.content)