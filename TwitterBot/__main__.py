import sys
from .classifyPoS import ClassifyPoS
from .server import server
from .tweets import tweets
#from .unique import unique
from textblob import TextBlob
import time

#back a directory then path to template
file = "/../Sentence_Structures/Sentences.csv" 
preFormat = ""
postFormat = ""
sleepMin = 5

def main():
    '''
    Main driver for TwitterBot program
    Passes a username to pullTweets, which returns a string of words from twitter
    The string is then passed to unique which cleans the data
    The clean data is then passed into a TextBlob object
    The TextBlob is passed to classifyWords which returns a dictionary of lists
    Each list is a different part of speech
    This dictionary is then passed to madlib which returns a finished madlib string
    '''
    
    twitterInterface = tweets()#tweets.py class object
    #need requestTweets option that returns a list of 3-tuple usernames
    while(True):
        #see more info in twitter docs
        print("Processing...")
        usernames = twitterInterface.getRequests()#3tuple [sendingUser,chosenUser,tweetID]
        
        if(usernames is not None):
            for sendingUser, chosenUser, tweetID in usernames:
                print(sendingUser)
                generateTweet(sendingUser, chosenUser, tweetID, twitterInterface)
        print("sleeping...")
        time.sleep(sleepMin * 60)

def generateTweet(sendingUser, chosenUser, tweetID, twitterInterface):
    #pass username to getTweets, return a list of words
    tweets = twitterInterface.get_tweets(chosenUser)
    if(tweets is None):
        return #do nothing
    #unique takes TextBlob as param, return TextBlob
    ##CURRENTLY NOT USING UNIQUE
    '''uniqueParser = unique(tweets)
    uniqueStr = uniqueParser.cleanTweets()'''
    #pass refinedList to parser to get a dictionary
    tweetBlob = TextBlob(uniqueStr)
    classifier = classifyWords(tweetBlob)
    tweetDict = classifier.createWordDictionary()

    #pass the dictionary to create madlibs, return a string
    sentenceGenerator = formatter(tweetDict, file, preFormat, postFormat)
    sentenceStr = sentenceGenerator.createSenctence()
    # final tweet format: "@sendingUser 'sentence'"
    if(int(tweetID) != 0):
        twitterInterface.postTweet(sentenceStr, sendingUser, chosenUser, tweetID)
    #print string
    print(sentenceStr)
    
if __name__ == '__main__':
    main()

        

