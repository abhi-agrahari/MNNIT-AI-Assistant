import math

def cosine_similarity(
        vector_a: list[float], vector_b: list[float]
)-> float:
    
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must be of the same length")

    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

    magnitude_a = math.sqrt(sum(a ** 2 for a in vector_a))

    magnitude_b = math.sqrt(sum(b ** 2 for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Zero vector is not allowed")

    return dot_product / (magnitude_a * magnitude_b)