# Import the database
import database.mysql_repository

from app import sql_scripting

# Instantiate a MysqlRepository object to use for the queries
repo = database.mysql_repository.MysqlRepository()

sql_class = sql_scripting.sql_system

sql = ("SELECT * "
       "FROM wordhistory"
       )

print("Print the database")
result = sql_class.print_db(sql_class, sql)

for line in result:
    print(line)

print("\nInserting line")
sql_insert = ("INSERT INTO wordhistory "
              "(WordText, NLTKTag, Etymological) "
              "VALUES "
              "('me', 'PRP', 'German') "
              "; "
              )

print("\nRemoving line")
input_word = 'I'
input_tag = 'DET'
sql_remove = ("DELETE FROM wordhistory "
              "WHERE wordtext = '{0}' AND NLTKTag = '{1}'"
              .format(input_word, input_tag)
              )

sql_class.print_db(sql_class, sql_remove)

result = sql_class.print_db(sql_class, sql)

for line in result:
    print(line)
