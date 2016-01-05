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
        
        consonantsFirst = params[3]
        
        consonantsSecond = params[7]


        matchCount = Engine.Engine.findMatch(consonantsFirst, consonantsSecond)
        
        firstWordLength = len(consonantsFirst)
        secondWordLength = len(consonantsSecond)
        Engine.Engine.percentage(matchCount, firstWordLength, secondWordLength)
        