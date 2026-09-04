from app.vectorstore.qdrant import QdrantService


qdrant_service = QdrantService()

collections = qdrant_service.client.get_collections()

print(collections)

from app.vectorstore.qdrant import QdrantService


qdrant_service = QdrantService()

qdrant_service.create_collection()

print("Collection created successfully.")