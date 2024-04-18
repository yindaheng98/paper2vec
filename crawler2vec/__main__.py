import asyncio
from crawler2vec.vectorize.openai import TextEmbedding
from argparse import ArgumentParser

parser = ArgumentParser()
TextEmbedding.add_arguements(parser)


async def main():
    args = parser.parse_args()
    vectorizer = TextEmbedding(args)
    vector = await vectorizer.vectorize("Who am I?")
    print(vector)

if __name__ == "__main__":
    asyncio.run(main())
