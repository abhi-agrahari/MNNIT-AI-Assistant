from app.ingestion.pdf_loader import load_pdf
from app.ingestion.chunker import chunk_text
from app.ingestion.models import DocumentChunk


pdf_path = "../data/colleges/mnnit/hostel-brochure/hostel Rules.pdf"

college_id = "mnnit"
document_id = "hostel-rules"
document_type = "HOSTEL"

pages = load_pdf(pdf_path)

all_chunks = []

for page in pages:

    chunks = chunk_text(page["text"])

    for index, chunk in enumerate(chunks, start=1):

        document_chunk = DocumentChunk(
            college_id=college_id,
            document_id=document_id,
            document_type=document_type,
            page_number=page["page_number"],
            chunk_index=index,
            text=chunk
        )

        all_chunks.append(document_chunk)


print(f"Total chunks: {len(all_chunks)}")

for chunk in all_chunks[:3]:
    print("\n--------------------")
    print(chunk.model_dump())