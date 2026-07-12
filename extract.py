import fitz

doc = fitz.open(
    "data/English_ArRaheeq_AlMakhtum_THE_SEALED_NECTAR.pdf"
)

text = ""

# Commencer à la page 8
for i, page in enumerate(doc[7:]):

    page_text = page.get_text("text")

    text += f"\n\n--- PAGE {i+8} ---\n\n"
    text += page_text

with open("book.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Extraction terminée.")