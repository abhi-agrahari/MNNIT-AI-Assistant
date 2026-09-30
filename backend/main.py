from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from app.rag_service import RAGService

# create FastAPI app
app = FastAPI(
    title="College RAG API"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rag_service = RAGService()

class ChatRequest(BaseModel):
    question: str
    college_id: str
    history: list[dict] = []

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
        college_id=request.college_id,
        history=request.history
    )

    return result