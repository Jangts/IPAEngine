'''
Created on 28 Jun 2015

@author: annakeren
'''
import unittest
from src.annakeren.ipa.persist import MongoPersistence

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testConnectToMongo(self):
        params = ['localhost', 27017]
        db = MongoPersistence.MongoPersistence.connect(params)
        print db
        pass

    def testInsert(self):
        params = ['localhost', 27017]
        db = MongoPersistence.MongoPersistence.connect(params)
        db.ipa_engine.drop()
        
        basicWord = {'_id': 'id', 
                     'word':'word', 
                     'language':'language', 
                     'consonantTranscript':'consonantTranscript', 
                     'fullTranscript':'fullTranscript'}
        db.ipa_engine.insert(basicWord)
        print db.ipa_engine.find_one()
if __name__ == "__main__":
    unittest.main()