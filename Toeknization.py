import os
import nltk
import re
class Tokenization():
    def token(self,text_to_toekn):
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        self.token_query= ""
        self.token_query = tokenizer.tokenize(text_to_toekn)
        print("------"+str(self.token_query))
        return self.token_query



