from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

with open("clean_book.txt", "r", encoding="utf-8") as f:
    text = f.read()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1200,
    chunk_overlap=250
)

chunks = splitter.split_text(text)

print(f"Nombre de chunks : {len(chunks)}")

os.makedirs("chunks", exist_ok=True)

for i, chunk in enumerate(chunks):

    with open(
        f"chunks/chunk_{i}.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(chunk)