# Import the database
import database.mysql_repository

from app import sql_scripting

# Instantiate a MysqlRepository object to use for the queries
repo = database.mysql_repository.MysqlRepository()

sql = ("SELECT * "
       "FROM wordhistory"
       )

print("Print the database")
result = sql_scripting.print_db(sql)

for line in result:
    print(line)

print("\nInserting line")
sql_insert = ("INSERT INTO wordhistory "
              "(WordText, NLTKTag, Etymological) "
              "VALUES "
              "('me', 'PRP', 'German') "
              "; "
              )

sql_scripting.sql_write(sql_insert, False)

print("\nRemoving line")
input_word = 'I'
input_tag = 'DET'
sql_remove = ("DELETE FROM wordhistory "
              "WHERE wordtext = '{0}' AND NLTKTag = '{1}'"
              .format(input_word, input_tag)
              )

result = sql_scripting.print_db(sql)

for line in result:
    print(line)