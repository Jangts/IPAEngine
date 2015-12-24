# -*- coding: utf-8 -*-
'''
Created on 20 Dec 2015

@author: annakeren
'''
import unittest
from src.annakeren.wikiIPA.wikiIPA import Utils

class Test(unittest.TestCase):


    def testThatICanReturnLinesFromFile(self):
        lines = Utils.Utils.readLinesToListFromFile("/Users/annakeren/words.txt")
        if len(lines) < 1961:
            self.fail("Failed to read the file")
        else: 
            pass

    def testThatCanProduceListOfPermutations(self):
        line = 'Mandarin:, ‎(jiāomá), ,,German: Abaka, Russian: абака́ , ‎/abaká/, abaca, /ˌæb.əˈkɑ/'
        permuations = Utils.Utils.getPermutations(line)
        if len(permuations) <> 6:
            self.fail("Failed to get permutations from a line")
        else:
            pass
        
    def testThatCanPermutate(self):
        allList = []
        allList.append(['Mandarin', 'm', 'm2'])
        allList.append(['German', 'g', 'g2'])
        allList.append(['Hebrew', 'h', 'h2'])
        allList.append(['English', 'e', 'e2'])
        permutations = Utils.Utils.getAllPermutations(allList)
        if len(permutations) <> 6:
            self.fail("msg")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testThatICanReturnLinesFromFile']
    unittest.main()