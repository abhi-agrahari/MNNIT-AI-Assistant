from fastapi import FastAPI
from pydantic import BaseModel

from app.rag_service import RAGService

# create FastAPI app
app = FastAPI(
    title="College RAG API"
)

rag_service = RAGService()

class ChatRequest(BaseModel):
    question: str
    college_id: str

@app.get("/")
def root():
    return {
        "message": "College RAG API is running"
    }


# api endpoint for chat
@app.post("/api/chat")
def chat(request: ChatRequest):

    result = rag_service.answer(
        question=request.question,
        college_id=request.college_id
    )

    return result