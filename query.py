import chromadb

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-mpnet-base-v2"
)

client = chromadb.PersistentClient(path="./db")

collection = client.get_collection("sirah")

question = input("Question : ")

query_embedding = model.encode(question).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

for i, doc in enumerate(results["documents"][0]):
    print(f"\n--- Résultat {i+1} ---\n")
    print(doc)