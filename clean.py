import re

with open("book.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Supprimer les séparateurs de pages
text = re.sub(r"--- PAGE \d+ ---", "", text)

# Supprimer les numéros de page
text = re.sub(r"\n\d+\n", "\n", text)

# Supprimer "MSA NIU"
text = re.sub(r"MSA NIU", "", text)

# Supprimer les espaces multiples
text = re.sub(r"\s+", " ", text)

with open("clean_book.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Cleaning done!")