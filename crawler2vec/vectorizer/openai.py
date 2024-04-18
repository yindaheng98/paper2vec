from openai import AsyncOpenAI
from crawler2vec.abc import Vectorizer
from argparse import ArgumentParser


class TextEmbedding(Vectorizer):
    @staticmethod
    def add_arguements(parser: ArgumentParser):
        parser.add_argument("--api_key", type=str, required=True, help="Your OpenAI API key.")
        parser.add_argument("--model",
                            choices=['text-embedding-3-small', 'text-embedding-3-large', 'text-embedding-ada-002'],
                            default='text-embedding-3-small',
                            help="Which model do you want to use.")

    def __init__(self, args):
        self.client = AsyncOpenAI(api_key=args.api_key)
        self.model = args.model

    async def vectorize(self, *contents):
        sentences = [text.replace("\n", " ") for text in contents]
        resp = await self.client.embeddings.create(input=sentences, model=self.model)
        embeddings = [d.embedding for d in resp.data]
        return embeddings
