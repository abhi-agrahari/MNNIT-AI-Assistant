from app.embedding.service import EmbeddingService


embedding_service = EmbeddingService()

texts = [
    "Where should every student stay?",
    "What are the rules for staying in the hostel?"
]

embeddings = embedding_service.embed_texts(texts)

print("Embedding count:", len(embeddings))

for index, embedding in enumerate(embeddings):
    print(
        f"Text {index + 1} dimension:",
        len(embedding)
    )