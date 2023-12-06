# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = sorted(word.lower())

    def match(self, listy=[]):
        match = [x for x in listy if self.word == sorted(x.lower())]
        return match if match else []


