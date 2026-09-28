from app.embedding.service import EmbeddingService
from app.retrieval.similarity import cosine_similarity


embedding_service = EmbeddingService()

texts = [
    "MNNIT provides hostel accommodation to students.",
    "The institute has several departments offering undergraduate programs.",
    "Students are provided mess facilities inside the hostels.",
    "MNNIT organizes placement activities through the TPO.",
    "The institute has various sports facilities."
]

query = "What accommodation and mess facilities are available?"

text_embeddings = embedding_service.embed_texts(texts)
query_embedding = embedding_service.embed_text(query)

results = []

for text, embedding in zip(texts, text_embeddings):

    score = cosine_similarity(
        query_embedding,
        embedding
    )

    results.append({
        "text": text,
        "score": score
    })


results.sort(
    key=lambda result: result["score"],
    reverse=True
)


for result in results:
    print(
        f"{result['score']:.4f} -> {result['text']}"
    )