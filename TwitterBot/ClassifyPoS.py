from textblob import TextBlob
from .unique import unique

class classifyPoS:
    '''Classifies twitter words into parts of speech'''

    def __init__(self, words):
        '''
        Sets up ClassifyPoS class
        Initializes member variables of words
        :param words: TextBlob object
        '''
        
        #checks parameters
        if(words is None):
            print("List of words is empty")
            quit()

        self.words = words
        self.classified = words.tags
        self.partOfSpeechArgs = {
            'singularNoun' : ["NN", "NNP"],
            'pluralNoun' : ["NNS", "NNPS"],
            'regularAdj' : ["JJ"],
            'superlativeAdj' : ["JJS"],
            'comparativeAdj' : ["JJR"],
            'presentVerb' : ["VB", "VBP", "VBZ"],
            'gerundVerb' : ["VBG"],
            'comparativeAdv' : ["RBR"],
            'superlativeAdv' : ["RBS"]
            }

    def createDictionary(self):
        '''
        Creates a dictionary of dictionaries for each
        generalized part of partsOfSpeech
        :return: dictionary of dictionaries
        '''

        singularNoun =      self.getPOSList(self.partOfSpeechArgs['singularNoun'])
        pluralNoun =        self.getPOSList(self.partOfSpeechArgs['pluralNoun'])
        regularAdj =        self.getPOSList(self.partOfSpeechArgs['regularAdj'])
        superlativeAdj =    self.getPOSList(self.partOfSpeechArgs['superlativeAdj'])
        comparativeAdj =    self.getPOSList(self.partOfSpeechArgs['comparativeAdj'])
        presentVerb =       self.getPOSList(self.partOfSpeechArgs['presentVerb'])
        pastVerb =          self.getPOSList(self.partOfSpeechArgs['pastVerb'])
        gerundVerb =        self.getPOSList(self.partOfSpeechArgs['gerundVerb'])
        comparativeAdv =    self.getPOSList(self.partOfSpeechArgs['comparativeAdv'])
        superlativeAdv =    self.getPOSList(self.partOfSpeechArgs['superlativeAdv'])

        wordsDict = {
            'singularNoun'      : singularNoun,
            'pluralNoun'        : pluralNoun,
            'regularAdj'        : regularAdj,
            'superlativeAdj'    : superlativeAdj,
            'comparativeAdj'    : comparativeAdj,
            'presentVerb'       : presentVerb,
            'pastVerb'          : pastVerb,
            'gerundVerb'        : gerundVerb,
            'comparativeAdv'    : comparativeAdv,
            'superlativeAdv'    : superlativeAdv
        }

        return wordsDict

    def getPartOfSpeech(self, arguments):
        '''
        Takes arguments and returns a dict of those parts of speech.
        Ex: if it takes ['singularNoun', 'pluralNoun'], it'll return
        a dict with two entries: singularNoun and pluralNoun.
        Each entry is a list of every singular noun and plural noun 
        respectively.
        :param arguments: list of parts of speech
        :return: dictionary of lists with an entry for each argument
        '''
        dict = {}
        for arg in arguments:
            dict[arg] = self.getPOSList(self.partOfSpeechArgs[arg])
            
        return dict

    def getPOSList(self, arguments):
        '''
        Gets a list of a particular part of speech

        :param arguments: list of TextBlob parts of speech
        :return: list of words matching the arguments
        '''

        #validate input
        if(arguments is None ):
            print("Error in getPOSList: param arguments is None")
            quit()

        words = self.classifiedWords
        partsOfSpeech = []

        '''for each argument, add a new list of words 
        that matches the arguments POS type'''
        for arg in arguments:
            #get every instance of the POS
            argumentPOS = [word[0] for word in words if arg in word]
            #concatenate lists together
            partsOfSpeech = partsOfSpeech + argumentPOS
        if(partsOfSpeech is not None):
            for word in partsOfSpeech[:]:
                if(len(word) < 4):
                    partsOfSpeech.remove(word)

        return partsOfSpeech
        
