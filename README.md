# GDG on Campus NCKU 2024 AI 課程 - 第一次課程
> 使用 Gemini 介紹大型語言模型

GDG on Campus NCKU 2024 AI 課程第一次課程的材料，介紹大型語言模型 (LLMs) 和以及 RAG (Retrieval Augmented Generation)。

## 先決條件

- Python 3.8 或更高版本
- Gemini 和 OpenAI 的 API 金鑰（社課會提供）
- 基本的 Python 程式設計知識

## 設置說明

### 1. 複製儲存庫

```bash
git clone <repository-url>
cd ai-course-2024-1
```

### 2. API Key 配置

複製範例環境文件並配置您的 API Key：

```bash
cp .env.example .env
```

編輯 `.env` 文件並填入您的 API Key:
```plaintext
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. 虛擬環境設置

選擇以下方法之一：

#### 選項 A：使用 venv（Python 的內建虛擬環境）
```bash
python3 -m venv .venv
source .venv/bin/activate  # 在 Unix/macOS/Linux 上
# 或
.venv\Scripts\activate  # 在 Windows 上
```

#### 選項 B：使用 Poetry
```bash
poetry shell
```

### 4. 安裝套件

選擇以下方法之一：

#### 選項 A：使用 Poetry (推薦)
```bash
poetry install
```

#### 選項 B：使用 pip
```bash
pip install -r requirements.txt
```

## 課程材料

- [第一次課程投影片：Introduction to Gemini (LLM)](https://docs.google.com/presentation/d/1LXKqWzpgjugIcKHAHQlcdx3Kci4dpo5PUWq1vQgEBOY/edit?usp=sharing)
- [第一次課程投影片：RAG (Retrieval Augmented Generation)](https://docs.google.com/presentation/d/1QKaewHsrM75AQWOIliJLm3S8zrJZwR9E5-KW1VwWV2w/edit?usp=sharing)