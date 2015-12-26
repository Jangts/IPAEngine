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
        line1 = 'German:  abschwören,  Russian:,  отрека́ться,  ‎(otrekátʹsja),  abjure,  /æbˈdʒʊɹ/'
        permuations = Utils.Utils.getPermutations(line1)
        if len(permuations) <> 3:
            self.fail("Failed to get permutations from a line")
        else:
            pass
        
        line2 = 'Mandarin: 腹部 ,  ‎(fùbù),  German:,  Bauch,  Persian:,  شکم,  ‎(šekam),  Russian:,  живо́т,  ‎(živót),  abdomen,  /ˈæb.də.mən/'
        permuations = Utils.Utils.getPermutations(line2)
        if len(permuations) <> 10:
            self.fail("Failed to get permutations from a line")
        else:
            pass
        
        line3 ='Mandarin:,  ‎(jiāomá),  , , German: Abaka,  Russian: абака́ ,  ‎/abaká/,  abaca,  /ˌæb.əˈkɑ/'
        permuations = Utils.Utils.getPermutations(line3)
        if len(permuations) <> 6:
            self.fail("Failed to get permutations from a line")
        else:
            pass
        
    def testThatCanPermutate(self):
        allList = []
        allList.append(['Mandarin', 'm2'])
        allList.append(['German', 'g2'])
        allList.append(['Russian', 'r', 'r2'])
        allList.append(['English', 'e', 'e2'])
        permutations = Utils.Utils.getAllPermutations(allList)
        if len(permutations) <> 6:
            self.fail("msg")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testThatICanReturnLinesFromFile']
    unittest.main()