import os

import google.generativeai as genai # Google Generative AI
from dotenv import load_dotenv      # 讀取環境變數
from rich import print              # 讓輸出變漂亮

# 讀取環境變數
load_dotenv()

# 設定 Generative AI，包含模型
genai.configure(api_key=os.getenv('GEMINI_API_KEY')) 
model = genai.GenerativeModel(
    model_name='models/gemini-pro'
)

# 產生內容
response = model.generate_content(
    contents="介紹一下氣候變遷？", # 修改這邊，隨便改
    stream=True
)

# 看看他說了什麼吧！
for chunk in response:
    print(chunk.text)