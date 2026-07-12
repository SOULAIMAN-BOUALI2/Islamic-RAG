import chromadb
import ollama

import time
import psutil

from sentence_transformers import SentenceTransformer

# Client Ollama
ollama_client = ollama.Client(
    host="http://localhost:11434"
)

# Modèle d'embeddings
embedding_model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
)

# Client ChromaDB
chroma_client = chromadb.PersistentClient(path="./db")

collection = chroma_client.get_collection("sirah")

# Choix du modèle
MODELS = [
    "qwen2.5:7b",
    "gemma3:4b",
    "llama3.1:8b"
]

while True:

    question = input("\nQuestion : ")

    if question.lower() == "exit":
        break

    query_embedding = embedding_model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    context = "\n\n".join(results["documents"][0])
    

    prompt = f"""
You are an assistant specialized in the biography of Prophet Muhammad (pbuh).

Answer ONLY using the context below.

If the answer is not in the context, say:

"I don't know."

Give a short answer.

Context:

{context}

Question:

{question}
"""

    for model_name in MODELS:

        print("\n" + "=" * 50)
        print(f"MODEL : {model_name}")

        start_time = time.time()

        ram_before = psutil.virtual_memory().used / (1024 ** 3)

        response = ollama_client.chat(
            model=model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        ram_after = psutil.virtual_memory().used / (1024 ** 3)

        end_time = time.time()

        answer = response["message"]["content"]

        print("\nAnswer:\n")
        print(answer)

        print("\nMetrics:")
        print(f"Response time: {end_time - start_time:.2f} sec")
        print(f"RAM used: {ram_after - ram_before:.2f} GB")
        print(f"Characters: {len(answer)}")