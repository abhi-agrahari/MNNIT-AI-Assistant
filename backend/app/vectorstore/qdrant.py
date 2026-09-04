import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import (Distance, VectorParams, PointStruct,)

class QdrantService:

    COLLECTION_NAME = "college_documents"

    #creating connection
    def __init__(self, host: str = "localhost", port: int = 6333):

        self.client = QdrantClient(host=host, port=port)

    def create_collection(self):

        if not self.client.collection_exists(
            self.COLLECTION_NAME
        ):
            self.client.create_collection(
                collection_name=self.COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )
            )

    def insert_chunks(self, chunks, embeddings):

        points = []

        for index, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

            point_id = str(
                uuid.uuid5(
                    uuid.NAMESPACE_DNS,
                    (
                        f"{chunk.college_id}:"
                        f"{chunk.document_id}:"
                        f"{chunk.page_number}:"
                        f"{chunk.chunk_index}"
                    ),
                )
            )

            point = PointStruct(
                        id=point_id,
                        vector=embedding,
                        payload={
                            "college_id": chunk.college_id,
                            "document_id": chunk.document_id,
                            "document_type": chunk.document_type,
                            "page_number": chunk.page_number,
                            "text": chunk.text
                        }
                    )

            points.append(point)

        self.client.upsert(
            collection_name=self.COLLECTION_NAME,
            points=points
        )