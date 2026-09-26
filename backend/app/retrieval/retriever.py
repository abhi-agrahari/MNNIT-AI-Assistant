from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue
)

from app.embedding.service import EmbeddingService
from app.vectorstore.qdrant import QdrantService


class Retriever:

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

        return results.points