from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue
)

from app.embedding.service import EmbeddingService
from app.vectorstore.qdrant import QdrantService


class Retriever:

    # minimum similarity required for a result
    SCORE_THRESHOLD = 0.70

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.qdrant_service = QdrantService()

    def retrieve(
        self,
        question: str,
        college_id: str,
        top_k: int = 5
    ):

        # convert user question into embedding
        question_embedding = self.embedding_service.embed_text(
            question
        )

        # search Qdrant for the most similar chunks
        results = self.qdrant_service.client.query_points(
            collection_name=QdrantService.COLLECTION_NAME,
            query=question_embedding,
            query_filter=Filter(
                must=[
                    FieldCondition(
                        key="college_id",
                        match=MatchValue(
                            value=college_id
                        )
                    )
                ]
            ),
            limit=top_k,
            with_payload=True
        )

        # filter results that are actually similar
        filtered_results = [
            result
            for result in results.points
            if result.score >= self.SCORE_THRESHOLD
        ]

        return filtered_results