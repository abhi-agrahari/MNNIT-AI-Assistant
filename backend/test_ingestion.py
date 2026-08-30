from app.ingestion.pdf_loader import load_pdf
from app.ingestion.chunker import chunk_text


pdf_path = "../data/colleges/mnnit/hostel-brochure/hostel Rules.pdf"

pages = load_pdf(pdf_path)

print(f"Total pages: {len(pages)}")

total_chunks = 0

for page in pages:

    chunks = chunk_text(page["text"])

    print(
        f"\nPage {page['page_number']} "
        f"→ {len(chunks)} chunks"
    )

    for index, chunk in enumerate(chunks, start=1):
        print(f"\nChunk {index}:")
        print(chunk[:300])

    total_chunks += len(chunks)

print(f"\nTotal chunks: {total_chunks}")