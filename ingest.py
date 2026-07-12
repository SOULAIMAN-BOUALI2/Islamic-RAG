import os
import chromadb

from sentence_transformers import SentenceTransformer

# Charger le modèle d'embeddings
model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
)

# Créer la base vectorielle
client = chromadb.PersistentClient(path="./db")

collection = client.get_or_create_collection(
    name="sirah"
)

# Lire les chunks
for filename in os.listdir("chunks"):

    with open(
        f"chunks/{filename}",
        "r",
        encoding="utf-8"
    ) as f:

        text = f.read()

    embedding = model.encode(text).tolist()

    collection.add(
        ids=[filename],
        documents=[text],
        embeddings=[embedding]
    )

print("Base créée avec succès.")