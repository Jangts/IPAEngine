# -*- coding: utf-8 -*-
'''
Created on 28 Dec 2015

@author: annakeren
'''
from src.annakeren.wikiIPA.wikiIPA import Utils
from src.annakeren.ipa.persist import SqlitePersistence
from src.annakeren.ipa.engine.main import Engine
import string

if __name__ == '__main__':
    lines = Utils.Utils.readLinesToListFromFile("/Users/annakeren/Documents/workspace/IPAEngine/IPAEngine/words.txt")
    connection = SqlitePersistence.SqlitePersistence.connect("//Users//annakeren//Documents//workspace//IPAEngine//IPAEngine//ipa.sqlite")
    cursor = connection.cursor()
    for line in lines:
        permuations = Utils.Utils.getPermutations(line)
        for permutation in permuations:
            firstPair = permutation[0]
            secondPair = permutation[1]
            
#                 this is to take care of German pairs which do not have ipa, 
# in this case append the original word as ipa to the pair
            if len(secondPair) == 2:
                toCopy = secondPair[1]
                secondPair.append(toCopy)
            if len(firstPair) == 2:
                toCopy = firstPair[1]
                firstPair.append(toCopy)
            
#             this is an edge case for some Mandarin words without original script
            if not firstPair[2]:
                toCopy = firstPair[1]
                firstPair[2] = toCopy
            
            firstIpa = firstPair[2]
            secondIpa = secondPair[2]
            
            firstIpaConverted = Utils.Utils.convertDiphtongsToIpa(firstIpa)
            secondIpaConverted = Utils.Utils.convertDiphtongsToIpa(secondIpa)
            
            firstIpaWithoutVowels = Utils.Utils.getWordWithoutVowels(firstIpaConverted)
            secondIpaWithoutVowels = Utils.Utils.getWordWithoutVowels(secondIpaConverted)
#             Convert consonant array to string
            firstConsonants = ""
            for character in firstIpaWithoutVowels:
                firstConsonants = firstConsonants + character
                
            secondConsonants = ""
            for character in secondIpaWithoutVowels:
                secondConsonants = secondConsonants + character
#             ENGINE running
            matchCount = Engine.Engine.findMatch(firstConsonants, secondConsonants)
        
            firstWordLength = len(firstIpaWithoutVowels)
            secondWordLength = len(secondIpaWithoutVowels)
            matchPercentage = Engine.Engine.percentage(firstWordLength, secondWordLength)
#             ENGINE running
            
#             Persist pair comparison results
            match = str(matchPercentage)
            beginning = "INSERT INTO words VALUES('"
            ending = ");"
            insertString = beginning + firstPair[0] + "', '" + firstPair[1] + "', '" + firstPair[2] + "', '" + secondPair[0] + "', '" + secondPair[1] + "', '" + secondPair[2] + "', "  + match + ending 
          
            cursor.execute(insertString)
            connection.commit()
            print permuations
    connection.close()
    pass