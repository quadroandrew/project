from app.obfuscation.obf_clean import cleaner
from dataclasses import dataclass
import re


@dataclass
class reg_cleaner(cleaner):

    def clean_request(self, input_words):
        return re.sub(r'\[[0-9\]]+]', '', input_words)
