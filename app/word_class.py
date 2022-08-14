from dataclasses import dataclass
from app.obfuscation.obf_word_class import word_class


@dataclass
class WordInfo(word_class):

    word: str
    tag: str
    ety: str
