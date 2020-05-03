import nltk
import re
from hazm import *
import os
import hazm
class Lemmiz():
    def lemmiz(self,string1, string2):
            # hazm test
            self.lem_string_1=""
            self.lem_string_2 = ""
            hazm_lemmatizer = Lemmatizer()
            #words = re.findall(r'\w+', string1)
            for word in string1:
                    self.lem_string_1+=(hazm_lemmatizer.lemmatize(word))+" "
            #words = re.findall(r'\w+', string2)
            for word in string2:
                words = re.findall(r'\w+', word)
                self.lem_string_2+=(hazm_lemmatizer.lemmatize(word))+" "
            print("lemmitzaton string_1---" + str(self.lem_string_2))
            print("lemmitzaton string_2---" + str(self.lem_string_2))

            return self.lem_string_2,self.lem_string_2


