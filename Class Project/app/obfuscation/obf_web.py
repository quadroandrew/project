from dataclasses import dataclass
from abc import ABC


@dataclass
class web_scrape(ABC):

    def return_web(self, input_words, debug):
        pass
