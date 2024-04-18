from qdrant_client import AsyncQdrantClient
from qdrant_client.models import PointStruct
from crawler2vec.abc import DataDestination, Point
from argparse import ArgumentParser


class QdrantDatabase(DataDestination):
    @staticmethod
    def add_arguements(parser: ArgumentParser):
        parser.add_argument("--url", type=str, required=True, help="URL to your Qdrant instance.")
        parser.add_argument("--collection", type=str, required=True, help="Name of your Qdrant collection.")

    def __init__(self, args):
        self.client = AsyncQdrantClient(url=args.url)
        self.collection_name = args.collection

    async def write_vectors(self, *vectors: Point):
        operation_info = await self.client.upsert(
            collection_name=self.collection_name,
            wait=True,
            points=[
                PointStruct(id=point.id, vector=point.vector, payload=point.payload) for point in vectors
            ]
        )
