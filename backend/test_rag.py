from app.rag_service import RAGService


rag = RAGService()


question = "What are the hostel rules?"


answer = rag.answer(
    question=question,
    college_id="mnnit"
)


print("\nAnswer:")
print(answer)