from dataclasses import dataclass
from abc import ABC


@dataclass
class routes(ABC):

    def read_from(self, data):
        pass

    def write_to(self):
        pass
