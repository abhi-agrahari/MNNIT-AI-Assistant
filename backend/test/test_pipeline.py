from app.ingestion.pipeline import IngestionPipeline


pipeline = IngestionPipeline()

pipeline.ingest_document(
    pdf_path="data/colleges/mnnit/hostel-brochure/hostel Rules.pdf",
    college_id="mnnit",
    document_id="hostel-rules",
    document_type="HOSTEL"
)