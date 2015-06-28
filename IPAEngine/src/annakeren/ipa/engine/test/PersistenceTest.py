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
        MongoPersistence.MongoPersistence.connect("params")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testConnectToMongo']
    unittest.main()