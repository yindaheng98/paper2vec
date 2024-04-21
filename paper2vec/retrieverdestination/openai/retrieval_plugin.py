from .fast_api_client import AuthenticatedClient
from .fast_api_client.models import Document, DocumentMetadata, UpsertRequest, UpsertResponse
from .fast_api_client.api.default import upsert_upsert_post
from paper2vec.abc import RetrieverDestination, Content
from argparse import ArgumentParser


class ChatGPTRetrievalPlugin(RetrieverDestination):
    @staticmethod
    def add_arguments(parser: ArgumentParser):
        parser.add_argument("--base_url", type=str, required=True, help="URL to your ChatGPT Plugin instance.")
        parser.add_argument("--token", type=str, required=True, help="Bearer of your ChatGPT Plugin.")

    def __init__(self, args):
        self.retriever = AuthenticatedClient(base_url=args.base_url, token=args.token)

    async def upsert(self, *contents: Content) -> None:
        async with self.retriever as client:
            response: UpsertResponse = await upsert_upsert_post.asyncio(
                client=client,
                body=UpsertRequest([
                    Document(id=content.id, text=content.text, metadata=DocumentMetadata(**content.metadata))
                    for content in contents
                ])
            )
            print(response)
