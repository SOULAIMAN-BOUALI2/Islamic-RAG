# Islamic RAG — The Sealed Nectar QA System

A Retrieval-Augmented Generation (RAG) system designed to answer questions about the biography of Prophet Muhammad ﷺ using *Ar-Raheeq Al-Makhtum (The Sealed Nectar)*.

The project combines semantic search with local Large Language Models (LLMs) running through Ollama and compares their performance in answering Islamic questions.

---

# Features

- PDF text extraction.
- Text cleaning and preprocessing.
- Semantic chunking.
- Embedding generation.
- Vector storage with ChromaDB.
- Semantic retrieval.
- Local inference with Ollama.
- Comparison between multiple LLMs:
  - Qwen 2.5 7B
  - Llama 3.1 8B
  - Gemma 3 4B
- Page source retrieval.
- English, French and Arabic support.

---

# Architecture

```text
PDF
 ↓
extract.py
 ↓
book.txt
 ↓
clean.py
 ↓
clean_book.txt
 ↓
chunk.py
 ↓
chunks/
 ↓
ingest.py
 ↓
ChromaDB
 ↓
rag.py
 ↓
Qwen / Gemma / Llama
 ↓
Answer
```

---

# Project Structure

```text
islamic-rag/

├── data/
│   └── English_ArRaheeq_AlMakhtum_THE_SEALED_NECTAR.pdf
│
├── chunks/
│   ├── chunk_0.txt
│   ├── chunk_1.txt
│   └── ...
│
├── db/
│
├── extract.py
├── clean.py
├── chunk.py
├── ingest.py
├── rag.py
│
├── book.txt
├── clean_book.txt
│
├── requirements.txt
└── README.md
```

---

# Installation

## Clone the repository

```bash
git clone https://github.com/your-username/islamic-rag.git

cd islamic-rag
```

---

## Create a virtual environment

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama with Docker

```bash
docker run -d \
    --name ollama \
    -p 11434:11434 \
    ollama/ollama
```

---

# Download the models

```bash
docker exec -it ollama ollama pull qwen2.5:7b

docker exec -it ollama ollama pull llama3.1:8b

docker exec -it ollama ollama pull gemma3:4b
```

Check the installed models:

```bash
docker exec -it ollama ollama list
```

---

# Build the knowledge base

## 1. Extract the PDF

```bash
python extract.py
```

This generates:

```text
book.txt
```

---

## 2. Clean the text

```bash
python clean.py
```

This generates:

```text
clean_book.txt
```

---

## 3. Create chunks

```bash
python chunk.py
```

This generates:

```text
chunks/
```

---

## 4. Create embeddings and populate ChromaDB

```bash
python ingest.py
```

This generates:

```text
db/
```

---

# Run the RAG

```bash
python rag.py
```

Example:

```text
Question:

Where was Abraham originally from?

Answer:

Abraham was originally from a town called "Ar" near Kufa on the west bank of the Euphrates in Iraq.
```

---

# Compared Models

| Model | Parameters |
|--------|--------|
| Qwen 2.5 | 7B |
| Gemma 3 | 4B |
| Llama 3.1 | 8B |

---

# Evaluation Metrics

The models are compared according to:

- Response time.
- RAM usage.
- Hallucination rate.
- Retrieval quality.
- Faithfulness to sources.
- Arabic support.
- English support.
- French support.

---

# Tech Stack

- Python 3.12
- ChromaDB
- Sentence Transformers
- LangChain
- Ollama
- Docker
- PyMuPDF
- Hugging Face

---

# Future Improvements

- Better chunking strategy.
- Metadata support.
- Streamlit interface.
- Automatic evaluation dataset.
- Docker Compose deployment.
- Support for multiple Islamic books.

---

# License

This project is intended for educational and research purposes only.