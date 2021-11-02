# pip install --user -U nltk
import re
import string

import nltk
from nltk.corpus import stopwords, words

nltk.download('stopwords')



class Text():
    def __init__(self):
        pass

    def wordInText(self):
        frequency = {}
        document_text = open('the_stranger.txt', 'r')
        text_string = document_text.read().lower()
        match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

        for word in match_pattern:
            count = frequency.get(word, 0)
            frequency[word] = count + 1

        frequency_list = frequency.keys()

        for words in frequency_list:
            return words, frequency[words]


    def maxfrquency(self, frequency):
        res = self.wordInText()
        maxValue = res.max(frequency[words])
        return maxValue

    def uniqueWord(self, words=None):
        res = self.wordInText()
        if res.frequency[words] == 1:
            return res.words

class TextModification(Text):
    def withoutPunctuatuion(self):
        res = Text.wordInText()
        res.translate(str.maketrans('', '', string.punctuation))

    def stopWords(self):
        res = Text.wordInText()
        return stopwords.words(res)

    def withoutCharacter(self):
        res = Text.wordInText()
        new_string = ''.join(char for char in res if char.isalnum())
        return new_string


