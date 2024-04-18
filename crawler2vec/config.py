import abc
from argparse import ArgumentParser


class Config(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def add_arguements(parser: ArgumentParser):
        pass
