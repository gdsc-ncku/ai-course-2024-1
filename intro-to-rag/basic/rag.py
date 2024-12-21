# 本程式碼參考 《讓你的文件活起來 - RAG 實作》文章，並做一些更動
# 連結網址：https://pythonbook.cc/articles/2024/9/11/rag-workshop

import os
import json

import openai
from numpy import linalg, dot
from rich import print
from dotenv import load_dotenv

# 設定 OpenAI API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_paragraph(filename: str, chunk_size: int = 100, overlap: int = 50) -> list:
    file_content = ""
    with open(filename, encoding="utf-8") as f:
        file_content = f.read()

    paragraphs = []
    for i in range(0, len(file_content), chunk_size - overlap):
        paragraphs.append(file_content[i:i+chunk_size])
    return paragraphs

def get_embedding(data: str) -> list:
    response = openai.embeddings.create(
        model="text-embedding-3-small",  # OpenAI 的 embedding 模型
        input=data
    )
    return response.data[0].embedding

def calc_embedings(paragraphs: list) -> list:
    """
    使用 OpenAI 的 Embedding API 生成向量
    """
    embeddings = []
    for data in paragraphs:
        embeddings.append(get_embedding(data))
    return embeddings

def cache_embeddings(filename: str, paragraphs: list) -> list:
    """
    將計算好的向量存在一個 JSON 檔案中，下次就不用重新計算
    """
    embedding_file = f"cache/{filename}.json"

    if os.path.isfile(embedding_file):
        with open(embedding_file) as f:
            return json.load(f)

    os.makedirs("cache", exist_ok=True)

    embeddings = calc_embedings(paragraphs)

    with open(embedding_file, "w") as f:
        json.dump(embeddings, f)

    return embeddings

def calc_similar_vectors(v: list, vectors: list) -> list:
    """
    計算相似度，使用餘弦相似度公式，並且返回最相似的段落
    """
    v_norm = linalg.norm(v) # 就是長度
    
    def cosine_similarity(vector: list) -> float:
        return dot(v, vector) / (v_norm * linalg.norm(vector))
    
    scores = [cosine_similarity(vector) for vector in vectors]

    return sorted(enumerate(scores), key=lambda x: x[1], reverse=True)

def find_top_k(prompt_embedding: list, embeddings: list, top_k: int) -> list:
    similar_vectors = calc_similar_vectors(prompt_embedding, embeddings)
    return [paragraphs[i] for i, _ in similar_vectors[:top_k]]

def format_context(contexts: list[str]) -> str:
    if not contexts:
        return "上下文: 無"
    formatted = "\n".join(f"{i+1}. {ctx}" for i, ctx in enumerate(contexts))
    return f"上下文:\n{formatted}"

def generate_system_prompt(contexts: list[str]) -> str: # 為了好看
    return (
        "你是一個很好的助手，只能使用台灣人熟悉的繁體中文，並且根據上下文 (context) 來回答"
        "如果提供的上下文不足以讓你有自信回答，就請使用者提供更多的上下文。"
        f"上下文: {format_context(contexts)}"
    )

def inference(query: str, context: list[str]) -> str:
    system_prompt = generate_system_prompt(context)
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query},
        ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    doc = "about_me.txt" # 改成你要用的文件
    top_k = 3
    print(f"使用文件: {doc}")
    paragraphs = parse_paragraph(doc)
    print(f"段落數量: {len(paragraphs)}")
    embeddings = cache_embeddings(doc, paragraphs)

    input_prompt = input("您想問什麼問題？\n>>> ")

    while input_prompt.lower() != "bye":
        # 取得用戶輸入的 prompt 的 embedding
        prompt_embedding = get_embedding(input_prompt)

        # 找到最相似的段落
        contexts = find_top_k(prompt_embedding, embeddings, top_k)

        # inference
        response = inference(input_prompt, contexts)

        print(response)
        input_prompt = input(">>> ")
