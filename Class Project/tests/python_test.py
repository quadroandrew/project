from app.main import *

# region CSV READ
print("\nCSV reader")

filename = '../app/etymology.csv'
text = "I see them"
csvread(filename, text)

filename = '../app/etymology.csv'
text = "I see it"
csvread(filename, text)

filename = '../app/etymology.csv'
text = "It sees them"
csvread(filename, text)
# endregion

# region SQL READ
print("\nSQL reader")
sqlread()

print("\nSQL writer")
insert_into = ("INSERT INTO wordhistory (WordText, NLTKTag, Etymological)"
               "VALUES"
               "('and', 'CC', 'German')"
               ",('now', 'RB', 'German')"
               ",('for', 'IN', 'Frisian')"
               ",('something', 'NN', 'German')"
               ",('different', 'JJ', 'French')"
               )
sqlwrite(insert_into)

sqlcheck("and now for something completely different")
# endregion
