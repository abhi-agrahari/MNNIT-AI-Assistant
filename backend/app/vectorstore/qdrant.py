import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct


class QdrantService:

    COLLECTION_NAME = "college_documents"

    def __init__(self, host: str = "localhost", port: int = 6333):

        try:
            # connect to local Qdrant server
            self.client = QdrantClient(
                host=host,
                port=port
            )

            self.client.get_collections()

            print("Connected to Qdrant server.")

        except Exception as e:

            raise RuntimeError(
                "Could not connect to Qdrant.\n"
                "Make sure Qdrant is running on localhost:6333.\n"
                f"Original error: {e}"
            ) from e

        self.create_collection()

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

            print(
                f"Created Qdrant collection: "
                f"{self.COLLECTION_NAME}"
            )

    def insert_chunks(self, chunks, embeddings):

        if len(chunks) != len(embeddings):
            raise ValueError(
                "Number of chunks and embeddings must be the same."
            )

        points = []

        for chunk, embedding in zip(chunks, embeddings):

            # create ID for each chunk.
            point_id = str(
                uuid.uuid5(
                    uuid.NAMESPACE_DNS,
                    (
                        f"{chunk.college_id}:"
                        f"{chunk.document_id}:"
                        f"{chunk.page_number}:"
                        f"{chunk.chunk_index}"
                    )
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
                    "chunk_index": chunk.chunk_index,
                    "text": chunk.text
                }
            )

            points.append(point)

        if not points:
            return

        self.client.upsert(
            collection_name=self.COLLECTION_NAME,
            points=points
        )

        print(
            f"Inserted {len(points)} chunks into "
            f"'{self.COLLECTION_NAME}'."
        )