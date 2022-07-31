# Get the time for tracking the amount of time passes between functions
import time

# Import nltk
import nltk
from nltk import word_tokenize

# Download any needed packages
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Use this import to process CSV files
# The SQL database should override the usage of the CSV file
import csv

# Import the database
import database.mysql_repository

# Instantiate a MysqlRepository object to use for the queries
repo = database.mysql_repository.MysqlRepository()


def csvread(filename, csvinput):
    ###
    # This is for debugging. Find ways to reduce time
    ###

    # Start timer
    start = time.time()
    prefunction = time.time()

    # Create the list of items
    # This should be revamped to use other things (dict?) over list
    try:
        wordList, tagList, etyList = OpenFile.readfile(OpenFile, filename)
    except IOError:
        print("Opening file error")

    text = word_tokenize(csvinput)
    tagged = nltk.pos_tag(text)

    print("text tagged: ", tagged)

    ###
    CallForTime.timeAtNow(prefunction)
    prefunction = time.time()
    ###

    # Find all the indexes that match the word
    for word in tagged:

        print(word[0])

        indexes = [i for i, j in enumerate(wordList) if j == word[0]]

        # print("indexes: ", indexes)
        if not indexes:
            etymology = "invalid"
        else:
            for index in indexes:

                if tagList[index] == word[1]:
                    etymology = etyList[index]
                    break

        print(etymology)


class OpenFile:

    def __init__(self):
        """
        Initializes the file reader
        Reads the Excel spreadsheet and returns the word, part of speech tag, and etymology
        """

    def readfile(self, filename):

        # Use these for processing the csv
        fields = []
        rows = []
        word = []
        postag = []
        ety = []

        # This script is a generic CSV reader from online

        # reading csv file
        with open(filename, 'r') as csvfile:

            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = next(csvreader)

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)

            # get total number of rows
            print("Total no. of rows: %d" % (csvreader.line_num))

        # printing the field names
        print('Field names are:' + ', '.join(field for field in fields))

        for row in rows:

            # parsing each column of a row
            for count, col in enumerate(row):

                # Break apart the csv into text, POS tag, and etymology
                if count == 0:
                    word.append(col)
                elif count == 1:
                    # Append the sentence
                    postag.append(col)
                elif count == 2:
                    # Get the label
                    ety.append(col)
                else:
                    print("Error in the count")

        return word, postag, ety


class CallForTime:

    def timeAtNow(thetime):
        now = time.time()
        print("completed function: ", round(now - thetime, 2), " seconds\n")


# Function to check input against database
def sqlcheck(inputwords):
    ###
    # This is for debugging. Find ways to reduce time
    ###

    # Start timer
    start = time.time()
    prefunction = time.time()

    text = word_tokenize(inputwords)
    tagged = nltk.pos_tag(text)

    print("text tagged: ", tagged)

    ###
    CallForTime.timeAtNow(prefunction)
    prefunction = time.time()
    ###

    for word in tagged:
        sql = ("SELECT * "
               "FROM wordhistory "
               "WHERE wordtext = '{0}' AND NLTKTag = '{1}'"
               .format(word[0], word[1])
               )

        result = query_db(sql)
        if len(result) != 0:
            print(result)
        else:
            print("invalid word")

    ###
    CallForTime.timeAtNow(prefunction)
    ###


###
# DEBUGGER: Function to read from database
###
def sqlread():
    sql = ("SELECT * "
           "FROM wordhistory"
           )
    result = query_db(sql)
    print("\nFirst word: ", result[0][0])


# Function to write to database
def sqlwrite(sqlinput):
    print("\nInserting data: ")

    insert_db(sqlinput)

    sql = ("SELECT * "
           "FROM wordhistory"
           )
    result = query_db(sql)
    print("\ndb: ")
    for line in result:
        print(line)


# Query database
def query_db(sql):
    repo.cursor.execute(sql)
    return list(repo.cursor)


# Write to database
def insert_db(sql):
    repo.cursor.execute(sql)
    print("\nInserted into database")
