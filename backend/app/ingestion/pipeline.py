from app.ingestion.pdf_loader import load_pdf
from app.ingestion.chunker import chunk_text
from app.ingestion.models import DocumentChunk
from app.embedding.service import EmbeddingService
from app.vectorstore.qdrant import QdrantService

class IngestionPipeline:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.qdrant_service = QdrantService()

    def ingest_document(
            self,
            pdf_path: str,
            college_id: str,
            document_id: str,
            document_type: str
    ):
        
        pages = load_pdf(pdf_path)

        chunks = []

        for page in pages:

            page_chunks = chunk_text(page["text"])

            for index, text in enumerate(page_chunks, start=1):

                chunk = DocumentChunk(
                    college_id=college_id,
                    document_id=document_id,
                    document_type=document_type,
                    page_number=page["page_number"],
                    chunk_index=index,
                    text=text
                )

                chunks.append(chunk)

            print(f"Created {len(chunks)} chunks")

            embeddings = self.embedding_service.embed_text(
                [chunk.text for chunk in chunks]
            )

            self.qdrant_service.insert_chunks(chunks, embeddings)

            print("Document successfully ingested")
