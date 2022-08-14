from dataclasses import dataclass
from abc import ABC


@dataclass
class db_reader(ABC):

    def read(self, input_word, input_tag, debug_bool):
        pass

    def write(self, order_input, debug_bool):
        pass

    def query_db(self, orders):
        pass

    def insert_db(self, orders, records, debug_bool):
        pass

    def print_db(self, sql):
        pass

    def delete_table(self):
        pass
