from dataclasses import dataclass
from abc import ABC


@dataclass
class word_class(ABC):
    word: str
    tag: str
    ety: str
