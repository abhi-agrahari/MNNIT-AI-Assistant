from app.ingestion.pipeline import IngestionPipeline

pipeline = IngestionPipeline()

pipeline.ingest_document(
    pdf_path="data/colleges/mnnit/hostel-brochure/hostel Rules.pdf",
    college_id="mnnit",
    document_id="hostel-rules",
    document_type="HOSTEL"
)

pipeline.ingest_document(
    pdf_path="data/colleges/mnnit/hostel-brochure/hostel booklet.pdf",
    college_id="mnnit",
    document_id="hostel-booklet",
    document_type="HOSTEL"
)

pipeline.ingest_document(
    pdf_path="data/colleges/mnnit/hostel-brochure/hostel Structure.pdf",
    college_id="mnnit",
    document_id="hostel-structure",
    document_type="HOSTEL"
)

pipeline.ingest_document(
    pdf_path="data/colleges/mnnit/college-brochure/Annual_Report_MNNIT.pdf",
    college_id="mnnit",
    document_id="annual-report",
    document_type="COLLEGE"
)

pipeline.ingest_document(
    pdf_path="data/colleges/mnnit/tpo-brochure/Placement Brochure.pdf",
    college_id="mnnit",
    document_id="placement-brochure",
    document_type="TPO"
)