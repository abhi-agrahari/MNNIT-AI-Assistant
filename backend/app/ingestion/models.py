from pydantic import BaseModel

class DocumentChunk(BaseModel):
    college_id: str
    document_id: str
    document_type: str
    page_number: int
    chunk_index: int
    text: str