'''
Created on 6 Aug 2015

@author: annakeren
'''
import unittest
from src.annakeren.wikiIPA.wikiIPA import Utils
from src.annakeren.wikiIPA.wikiIPA import WiktionarySpider


class Test(unittest.TestCase):

    def setUp(self):
        print "setup"
      
    
    def readAllFilesFromFolder(self):
        files = Utils.Utils.readAllFilesFromFolder("/Users/annakeren/ipa")
        for file in files:
            with open(file, "r") as f:
                f.read()
    
      
    def testWriteToFile(self):
        Utils.Utils.createNewFileAndWrite("/Users/annakeren/ipa/test.html", "page")
     
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()