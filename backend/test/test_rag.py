from app.rag_service import RAGService

rag = RAGService()

result = rag.answer(
    question="What are the hostel rules?",
    college_id="mnnit"
)

print("\nAnswer:")
print(result["answer"])

print("\nSources:")

for source in result["sources"]:
    print(
        f'- {source["document_id"]} '
        f'- Page {source["page_number"]}'
    )