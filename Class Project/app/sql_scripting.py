# Import the database
import database.mysql_repository

# Instantiate a MysqlRepository object to use for the queries
repo = database.mysql_repository.MysqlRepository()


# Function to check input against database
def sql_read(input_word, input_tag, debug_bool):

    sql = ("SELECT Etymological "
           "FROM wordhistory "
           "WHERE wordtext = '{0}' AND NLTKTag = '{1}'"
           .format(input_word, input_tag)
           )

    result = query_db(sql)

    if len(result) != 0:
        result = result[0]
        result = list(result[0])
        result = ''.join(result)

        if debug_bool:
            print(result)

        return result
    else:
        if debug_bool:
            print("invalid word")

        # Write to the SQL file
        # Get the data from online

        return "not in the dictionary"


# Function to write to database
def sql_write(sqlinput, debug_bool):
    if debug_bool:
        print("\nInserting data: ")

    insert_db(sqlinput, debug_bool)

    sql = ("SELECT * "
           "FROM wordhistory"
           )
    result = query_db(sql)

    if debug_bool:
        print("\nDatabase: ")
        for line in result:
            print(line)


# Query database
def query_db(sql):
    repo.cursor.execute(sql)
    return list(repo.cursor)


# Write to database
def insert_db(sql, debug_bool):
    repo.cursor.execute(sql)

    if debug_bool:
        print("\nInserted into database")
