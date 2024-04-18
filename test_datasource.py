import asyncio
from crawler2vec.datasource.neo4j import GraphQuery
from crawler2vec.abc import DataSource
from argparse import ArgumentParser

parser = ArgumentParser()
GraphQuery.add_arguements(parser)


async def main():
    args = parser.parse_args()
    datasource: DataSource = GraphQuery(args)
    async for content in datasource.get_contents():
        print(content)

if __name__ == "__main__":
    asyncio.run(main())
