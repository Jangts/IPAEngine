'''
Created on 3 Jul 2015

@author: annakeren
'''

from src.annakeren.ipa.engine.main import Engine
from src.annakeren.ipa.persist import MongoPersistence

class ComparisonPersistence(object):
    '''
    classdocs
    '''
    @staticmethod 
    def connectToDB(params):
        dbConection = MongoPersistence.MongoPersistence.connect(params)
        return dbConection
    
    
#    firstWord, secondWord, 
#    languageFirst, languageSecond
#    transcriptFirst, tarnscriptSecond
#    consonantsFirst, consonantsSecon

        
    '''
    methodocs
    two words are compared and comparison
    result is saved to mongodb
    _id is params[0] + ' ' + params[1] + ' ' + param[4] + ' ' + param[5]
    '''
    @staticmethod 
    def compareAndPerist(params, dbConnection):
        firstWord = params[0]                   
        languageFirst = params[1]
        transcriptFirst = params[2]
        consonantsFirst = params[3]
        
        secondWord = params[4]
        languageSecond = params[5]
        transcriptSecond = params[6]
        consonantsSecond = params[7]


        matchCount = Engine.Engine.findMatch(consonantsFirst, consonantsSecond)
        
        firstWordLength = len(consonantsFirst)
        secondWordLength = len(consonantsSecond)
        matchPercentage = Engine.Engine.percentage(firstWordLength, secondWordLength)
        
        x = firstWord + " " + languageFirst + " "  +  secondWord + " " + transcriptSecond
        post = {
                    '_id':x,
                     'matchCount':matchCount,
                     'matchPercentage':matchPercentage,
                     'words':
                    [
                      {
                       'word':firstWord, 
                       'language':languageFirst, 
                       'consonantTranscript':consonantsFirst, 
                       'fullTranscript':transcriptFirst
                       },
                     {
                       'word':secondWord, 
                       'language':languageSecond, 
                       'consonantTranscript':consonantsSecond, 
                       'fullTranscript':transcriptSecond
                       }
                    ]
                }
        
        MongoPersistence.MongoPersistence.insert(dbConnection, post)