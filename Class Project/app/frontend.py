import string
from app import word_class
from app.sql_scripting import sql_system
from app.obfuscation.obf_frontend import front_end
from dataclasses import dataclass
import contractions
import time

try:
    import nltk
except ModuleNotFoundError:
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    import nltk

from nltk import RegexpTokenizer


@dataclass
class frontend(front_end):

    def input_system(self, input_words, debug):

        start_time = time.time()
        input_words = contractions.fix(input_words)
        punctuation = ''
        if input_words[-1] in string.punctuation:
            punctuation = (input_words[-1], input_words[-1])
        print('Contractions removed:', input_words) if debug else ()
        tokenizer = RegexpTokenizer(r'\w+')
        text_tokenized = tokenizer.tokenize(input_words)
        text_tagged = nltk.pos_tag(text_tokenized)
        if len(punctuation) > 0:
            text_tagged.append(punctuation)
        word_class_list = []
        reader_reference = sql_system

        for ind_word in text_tagged:
            function_time = time.time()
            if ("NNP" in ind_word[1]) or ("NNPS" in ind_word[1]) \
                    or ("I" in ind_word[0]) \
                    or (ind_word[0] in string.punctuation):
                print("Skipped lowercasing") if debug else ()
            else:
                lower_case_list = list(ind_word)
                lower_case_list[0] = lower_case_list[0].lower()
                ind_word = tuple(lower_case_list)
                print("ind: ", ind_word) if debug else ()
            word_class_list.append(word_class.WordInfo(ind_word[0], ind_word[1],
                                                       reader_reference.read(reader_reference, ind_word[0], ind_word[1],
                                                                             debug)))
            print(ind_word, "took", time.time() - function_time, "to process") if debug else ()
        if debug:
            for word in word_class_list:
                print("frontend: ", word.word)
        print("Returning class list @:", time.time() - start_time) if debug else ()
        return frontend.prepare_for_HTML(self, word_class_list, debug)

    def prepare_for_HTML(self, input_block, debug):
        etymologies = ''
        word_append = ''
        return_block = "The sentence:<br/>"
        for word_plus in input_block:
            if word_plus == input_block[0]:
                word_append += word_plus.word.capitalize() + " "
            else:
                word_append += word_plus.word + " "
        return_block += word_append + "<br/><br/>"
        print(return_block) if debug else ()
        for ety_plus in input_block:
            etymologies += ety_plus.word + ":<br/>" + ety_plus.ety + "<br/><br/>"
        return_block += etymologies
        if debug:
            sql = "SELECT * FROM wordhistory"
            db = sql_system.print_db(sql_system, sql)
            for row in db:
                print(row)

        return return_block
