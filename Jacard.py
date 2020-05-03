import nltk
import re
from hazm import *
import os

class JacardSimilarity():
    def jacardsimilarity(self,string_1,string_2):
            query = string_1.split()
            document = string_2.split()
            intersection = set(query).intersection(set(document))
            union = set(query).union(set(document))
            self.jacard=len(intersection) / len(union)
            print("--jaccard is ---"+str(self.jacard))
            return self.jacard