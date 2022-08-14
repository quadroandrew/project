from dataclasses import dataclass
from abc import ABC


@dataclass
class cleaner(ABC):

    def clean_request(self, input_words):
        pass
