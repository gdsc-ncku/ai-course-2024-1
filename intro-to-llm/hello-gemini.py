import os

import google.generativeai as genai # Google Generative AI
from dotenv import load_dotenv      # 讀取環境變數
from rich import print              # 讓輸出變漂亮

# 讀取環境變數
load_dotenv()

# 設定 Generative AI，包含模型
genai.configure(api_key=os.getenv('GEMINI_API_KEY')) 
model = genai.GenerativeModel(
    model_name='models/gemini-pro' # 這邊也可以改ㄡ
)

# 產生內容
response = model.generate_content(
    "你知道海狸大師是誰嗎？" # 修改這邊，隨便改
)

# 看看他說了什麼吧！
print(response)
print('=================================================')
print(response.text)