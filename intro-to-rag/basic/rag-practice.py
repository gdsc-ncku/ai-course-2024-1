import os
import json

import openai
from numpy import linalg, dot
from rich import print
from dotenv import load_dotenv

# 設定 OpenAI API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 設定 OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")  # 建議將 API Key 存在環境變數中

def parse_paragraph(filename: str) -> list:
    '''
    讀取指定的文件並解析為段落列表
    '''
    pass

def get_embedding(data: str) -> list:
    pass

def calc_embedings(paragraphs: list) -> list:
    '''
    使用 OpenAI 的 Embedding API 生成向量
    '''
    pass

def cache_embeddings(filename: str, paragraphs: list):
    '''
    將計算好的向量存在一個 JSON 檔案中，下次就不用重新計算
    '''
    pass

def calc_similar_vectors(v: list, vectors: list):
    '''
    計算相似度，使用餘弦相似度公式
    '''
    pass

def find_top_k(prompt_embedding: list, paragraphs: list, top_k: int) -> list:
    '''
    找到最相似的段落
    '''
    pass

def inference(query: str, context: list[str]) -> str:
    '''
    使用 OpenAI 的 Chat Completion API 生成回應
    '''
    pass

if __name__ == "__main__":
    # 設定要使用的文件名稱
    doc = "/path/to/your/file.txt"

    # 切割段落
    paragraphs = parse_paragraph(doc)

    # 計算向量
    embeddings = calc_embeddings(paragraphs)

    # 設定要返回的段落數量
    top_k = 3

    # 提示學員輸入他們想要詢問的問題
    prompt = input("您想問什麼問題？\n>>> ")

    # 當用戶輸入的不是 'bye' 時，持續運行
    while prompt.lower() != "bye":
        # 取得用戶輸入的 prompt 的 embedding
        prompt_embedding = get_embedding(input_prompt)

        # 找到最相似的段落
        contexts = find_top_k(prompt_embedding, paragraphs, top_k)

        # inference
        response = inference(input_prompt, contexts)

        # 提示使用者再次輸入問題
        prompt = input(">>> ")
