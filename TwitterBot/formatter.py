import csv
import random
import os

class formatter:
    '''
    Handles getting random snetence structure and uses text  replacement
    to place parts of speech into madlib
    '''
    def __init__(self, partsOfSpeech, file, preFormat, postFormat):
        '''
        Initializes formatter class
        :param partsOfSpeech: a dictionary containing lists of parts of speech
        :param madlibFile: the relative file location of the madlibs csv
        :param preFormat: the HTML formatting before the inserted word
        :param postFormat: the HTML formatting after the inserted word
        '''
        self.wordsDict = partsOfSpeech
        self.file = os.path.abspath(os.path.dirname(__file__)) + file
        self.preFormat = preFormat
        self.postFormat = postFormat

    def getSentence(self):
        '''
        Returns random sentence structure from Sentences.csv
        :return: random sentence structure as a string
        '''
        #gets list of sentences
        sentences = self.readCSV()
        #gets random entry from list
        randomSentence = random.choice(sentences)
        #returns random entry
        return randomSentence

    def createSentence(self):
        '''
        Does text replacement on a sentence with the appropiate part of speech
        :return: an HTML formatted string representing the entire sentence
        '''
        #loop through each word
        sentence = self.getSentence()
        wordList = sentence.split(" ")
        for i, word in enumerate(wordList):
            #if string indicates need for PoS
            if(len(word) > 0 and word[0] == "#"): #removes hashtags from word(PoS)
                word = word[1:]#words after index 0 should start at index 1(due to " ")
                oldWord = word
                tempChar = ""
                #get list of that PoS
                if(word[-1] in __import__('string').punctuation):
                    tempChar = word[-1]
                    word = word[:-1]
                partOfSpeechList = self.wordsDict[word]

                #get random word
                word = random.choice(partOfSpeechList)
                #remove used word from the list
                partOfSpeechList.remove(word)
                word = word + tempChar
                word = self.preFormat + word + self.postFormat
                wordList[i] = word
                
        sentence = " ".join(wordList)
        return sentence

    def readCSV(self):
        '''
        Read each sentence structure from CSV file
        :return: list of sentence structures
        '''
        sentences = []

        #opens file
        with open(self.file, 'r') as file:
            reader = csv.reader(file)
            for row in reader: #sentences delineated by newline character(new row)
                sentences = sentences + row
        sentences = [list for list in sentences if list is not ''] #???
        return sentences
    
