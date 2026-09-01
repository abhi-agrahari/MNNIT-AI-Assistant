from app.retrieval.similarity import cosine_similarity


vector_a = [1, 0, 0]
vector_b = [1, 0, 0]
vector_c = [0, 1, 0]

print(
    "A vs B:",
    cosine_similarity(vector_a, vector_b)
)

print(
    "A vs C:",
    cosine_similarity(vector_a, vector_c)
)