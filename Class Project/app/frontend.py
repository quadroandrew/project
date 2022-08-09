# Get the word class
from app import word_class

# Get the sql read/write script
from app import sql_scripting

# Download any needed packages
try:
    import nltk
except ModuleNotFoundError:
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    import nltk

from nltk import word_tokenize

# Set a boolean to print out debug messages
debug = False


def input_system(input_words):
    # Tokenize the word list and tag them
    text_tokenized = word_tokenize(input_words)
    text_tagged = nltk.pos_tag(text_tokenized)

    # Empty list for the objects
    word_class_list = []

    for ind_word in text_tagged:

        # Lowercase all words except tags that are NNP, NNPS, or the word "I"
        if ("NNP" in ind_word[1]) or ("NNPS" in ind_word[1]) or ("I" in ind_word[0]):
            if debug:
                print("Skipped lowercasing")
        else:
            lower_case_list = list(ind_word)
            lower_case_list[0] = lower_case_list[0].lower()
            ind_word = tuple(lower_case_list)

            if debug:
                print("ind: ", ind_word)

        word_class_list.append(word_class.WordInfo(ind_word[0], ind_word[1],
                                                   sql_scripting.sql_read(ind_word[0], ind_word[1], debug)))

    if debug:
        for word in word_class_list:
            print("Class: ", word.word)

    for word_object in word_class_list:
        print(word_object.word, "is", word_object.ety)
