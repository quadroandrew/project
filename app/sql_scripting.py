import string
from dataclasses import dataclass
from app.obfuscation.obf_db_reader import db_reader
import database.mysql_repository
from app.web_scraper import web_scraper
from app.clean_regex import reg_cleaner
import urllib.parse

repo = database.mysql_repository.MysqlRepository()

clean = reg_cleaner
scrape = web_scraper


@dataclass
class sql_system(db_reader):
    # region Read
    def read(self, input_word, input_tag, debug):
        sql = ("SELECT Etymological "
               "FROM wordhistory "
               "WHERE wordtext = '{0}' AND NLTKTag = '{1}'"
               .format(input_word, input_tag)
               )
        result = sql_system.query_db(self, sql)
        if len(result) != 0:
            result = result[0]
            result = list(result[0])
            result = ''.join(result)
            print(result) if debug else ()
            return result
        else:
            print("invalid word") if debug else ()
            if input_word in string.punctuation:
                print("punctuation found:", urllib.parse.quote(input_word.encode('utf8')), ":", input_word) \
                    if debug else ()
                new_ety = clean.clean_request(clean, scrape.return_web(scrape,
                                                                       urllib.parse.quote(input_word.encode('utf8')),
                                                                       debug))
            else:
                new_ety = clean.clean_request(clean, scrape.return_web(scrape, input_word, debug))
            record = (input_word, input_tag, new_ety)
            sql_system.write(sql_system, record, debug)
            return new_ety

    # endregion

    # region Write
    def write(self, order_input, debug):
        print("\nInserting data: ") if debug else ()
        insert_query = ("INSERT INTO wordhistory "
                        "(WordText, NLTKTag, Etymological) "
                        "VALUES "
                        "(%s, %s, %s) "
                        )
        sql_system.insert_db(sql_system, insert_query, order_input, debug)

    # endregion

    # region Query
    def query_db(self, sql):
        repo.cursor.execute(sql)
        return list(repo.cursor)
    # endregion

    def insert_db(self, sql, insertion, debug):
        print(insertion)
        repo.cursor.execute(sql, insertion)
        repo.commit_changes()
        print("\nInserted into database") if debug else ()
    # endregion

    # region Print
    def print_db(self, sql):
        repo.cursor.execute(sql)
        return repo.cursor.fetchall()
    # endregion

    # region Delete Database
    def delete_table(self):
        repo.cursor.execute("DELETE FROM wordhistory")
        repo.commit_changes()
    # endregion