from app.retrieval.retriever import Retriever


retriever = Retriever()

question = "What are the hostel rules?"

print("Question:", question)
print("Starting retrieval...")

results = retriever.retrieve(
    question=question,
    college_id="mnnit",
    top_k=3
)

print("Number of results:", len(results))

for result in results:

    print("\n-------------------------")

    print("Score:", result.score)

    print("College:", result.payload["college_id"])

    print("Document:", result.payload["document_id"])

    print("Page:", result.payload["page_number"])

    print("Chunk:", result.payload["chunk_index"])

    print("Text:")
    print(result.payload["text"])