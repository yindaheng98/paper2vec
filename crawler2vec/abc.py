import abc
from .config import Config


class Vectorizer(Config):
    @abc.abstractmethod
    async def vectorize(*args):
        pass
