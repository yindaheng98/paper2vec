import asyncio
from crawler2vec.vectorizer.openai import TextEmbedding
from .abc import Vectorizer
from argparse import ArgumentParser

parser = ArgumentParser()
TextEmbedding.add_arguements(parser)


async def main():
    args = parser.parse_args()
    vectorizer: Vectorizer = TextEmbedding(args)
    vector = await vectorizer.vectorize("Who am I?")
    print(vector)

if __name__ == "__main__":
    asyncio.run(main())
