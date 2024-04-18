from neo4j import AsyncGraphDatabase
from crawler2vec.abc import DataSource
from argparse import ArgumentParser


async def get_papers(tx, query):
    papers = []
    for record in await (await tx.run(query)).values():
        if "title" not in record[0]:
            continue
        paper = "Title: " + record[0]["title"]
        if "abstract" in record[0]:
            paper += " Abstract: " + record[0]["abstract"]
        papers.append(paper)
    return papers


class GraphQuery(DataSource):
    @staticmethod
    def add_arguements(parser: ArgumentParser):
        parser.add_argument("--username", type=str, default=None, help=f'Auth username to neo4j database.')
        parser.add_argument("--password", type=str, default=None, help=f'Auth password to neo4j database.')
        parser.add_argument("--uri", type=str, required=True, help=f'URI to neo4j database.')
        parser.add_argument("--query", type=str,
                            default="MATCH (n:Publication) RETURN n LIMIT 25",
                            help=f'Query to get data.')

    def __init__(self, args):
        self.uri = args.uri
        self.username = args.username
        self.password = args.password
        self.query = args.query

    async def get_contents(self):
        async with AsyncGraphDatabase.driver(self.uri, auth=(self.username, self.password)) as driver:
            async with driver.session() as session:
                for paper in await session.execute_read(get_papers, self.query):
                    yield paper
