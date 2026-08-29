from fastapi import FastAPI

app = FastAPI(
    title="College RAG",
    description="RAG based knowledge assistant for colleges",
    version="0.1.0"
)

@app.get("/test")
def root():
    return{
        "message": "College RAG API is running"
    }