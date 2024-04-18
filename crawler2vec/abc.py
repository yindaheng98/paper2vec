import abc
from typing import List, AsyncGenerator
from argparse import ArgumentParser


class Config(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def add_arguements(parser: ArgumentParser) -> None:
        pass


class DataSource(Config):
    @abc.abstractmethod
    async def get_contents(self) -> AsyncGenerator[str, None]:
        yield


class Vectorizer(Config):
    @abc.abstractmethod
    async def vectorize(self, *contents: str) -> List[List[float]]:
        pass


class DataDestination(Config):
    @abc.abstractmethod
    async def write_vectors(self, *vectors: List[float]) -> None:
        pass
