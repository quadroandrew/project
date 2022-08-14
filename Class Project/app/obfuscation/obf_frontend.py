from dataclasses import dataclass
from abc import ABC


@dataclass
class front_end(ABC):

    def input_system(self, input_words, debug):
        pass

    def prepare_for_HTML(self, input_block, debug):
        pass
