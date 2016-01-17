# -*- coding: utf-8 -*-
'''
Created on 23 Aug 2015

@author: annakeren
'''
import os
import string
import itertools

from src.annakeren.ipa.engine.main.Engine import Engine

class Utils(object):
    '''
    classdocs
    '''
    @staticmethod
    def readAllFilesFromFolder(path):
        pathsToFiles = []
        for root, dirs, files in os.walk(path):
            for file in files:
                pathsToFiles.append(root +  '/' + file)
        return pathsToFiles
    
    @staticmethod
    def createNewFileAndWrite(csvFileToWrite, page):
        with open(csvFileToWrite, "w") as f:
            if page:
                f.write(page)
            f.close()
    
    @staticmethod
    def writeToCsvFile(csvFileToWrite, triple):
        with open("/Users/annakeren/ipa/wictionary.csv", "a") as f:
            if triple:
                tripleLen = len(triple)
                for tripleEntry in triple:
                    if '.html' in tripleEntry:
                        f.write(tripleEntry)
                        f.write(', ')
                        ipa = triple[tripleLen - 1]
                        f.write(ipa.encode('utf-8'))
                        break
                    for tripleEntries in tripleEntry:
                        try:
                            f.write(tripleEntries.strip()) 
                        except:
                            pass
                            f.write(tripleEntries.encode('utf-8').strip()) 
                        
                        f.write(', ')
                f.write("\n")
        f.close()
            
    @staticmethod
    def readLinesToListFromFile(fname):
        with open(fname) as f:
            content = f.readlines()
        f.close()
        return content
    
    @staticmethod
    def appendToSpecificLanguageList(languagesList, specificList, currentWord):
        currentWordTrimmed = currentWord.translate(None, string.punctuation)
        if not currentWordTrimmed in languagesList:
            specificList.append(currentWordTrimmed)
    
    @staticmethod
    def getPermutations(line):
        splitLine = line.split() 
        splitLineLength = len(splitLine) 
        mandarin = "Mandarin"
        german = "German"
        hebrew = "Hebrew"
        persian = "Persian"
        russian = "Russian"
        english = "English"
        languagesList = []
        languagesList.append(mandarin)
        languagesList.append(german)
        languagesList.append(hebrew)
        languagesList.append(persian)
        languagesList.append(russian)
        mandarinList = []
        germanList = []
        hebrewList = []
        persianList = []
        russianList = []
        englishList = []
        if(splitLineLength > 2):
            englishList.append(splitLine[splitLineLength - 2])
            englishList.append(splitLine[splitLineLength - 1])
        index = 0
        
        for splitWord in splitLine:
            splitWord = splitWord.translate(None, string.punctuation)
            if splitWord.startswith(mandarin):
                currentWord = splitLine[index + 1]
                Utils.appendToSpecificLanguageList(languagesList, mandarinList, currentWord)
                currentWord = splitLine[index + 2]
                Utils.appendToSpecificLanguageList(languagesList, mandarinList, currentWord)
            if splitWord.startswith(german):
                currentWord = splitLine[index + 1]
                Utils.appendToSpecificLanguageList(languagesList, germanList, currentWord)
                currentWord = splitLine[index + 2]
                Utils.appendToSpecificLanguageList(languagesList, germanList, currentWord)
            if splitWord.startswith(hebrew):
                currentWord = splitLine[index + 1]
                Utils.appendToSpecificLanguageList(languagesList, hebrewList, currentWord)
                currentWord = splitLine[index + 2]
                Utils.appendToSpecificLanguageList(languagesList, hebrewList, currentWord)
            if splitWord.startswith(persian):
                currentWord = splitLine[index + 1]
                Utils.appendToSpecificLanguageList(languagesList, persianList, currentWord)
                currentWord = splitLine[index + 2]
                Utils.appendToSpecificLanguageList(languagesList, persianList, currentWord)
            if splitWord.startswith(russian):
                currentWord = splitLine[index + 1]
                Utils.appendToSpecificLanguageList(languagesList, russianList, currentWord)
                currentWord = splitLine[index + 2]
                Utils.appendToSpecificLanguageList(languagesList, russianList, currentWord)
            index = index + 1
        
        allList = []
        if mandarinList:
            mandarinList.insert(0, mandarin)
            allList.append(mandarinList)
        if germanList:
            germanList.insert(0, german)
            allList.append(germanList)
        if hebrewList:
            hebrewList.insert(0, hebrew)
            allList.append(hebrewList)
        if persianList:
            persianList.insert(0, persian)
            allList.append(persianList)
        if russianList:
            russianList.insert(0, russian)
            allList.append(russianList)
        if englishList:
            englishList.insert(0, english)
            allList.append(englishList)
        
        permutations = list(itertools.product(allList, repeat=3))
        permutationsSet = Utils.getSetOfPermutations(permutations)
        return permutationsSet
     
    @staticmethod
    def getSetOfPermutations(permutations):
        permutationsSet = []
        for permutation in permutations:
            first = permutation[0]
            second = permutation[1]
            if (first != second) & ((first, second) not in permutationsSet) & ((second, first) not in permutationsSet):
                permutationsSet.append((first, second))
        return permutationsSet

    @staticmethod
    def getAllPermutations(listToPermute):
        permutations = list(itertools.product(listToPermute, repeat=2))
        permutationsSet = Utils.getSetOfPermutations(permutations)
        return permutationsSet
    @staticmethod
    def convertDiphtongsToIpa(wordWithDiphtongs):
        wordTemp = string.replace(wordWithDiphtongs, 'dj', 'j')
        wordTemp = string.replace(wordTemp, 'ch', 'č')
        wordTemp = string.replace(wordTemp, 'Sch', 's')
        wordTemp = string.replace(wordTemp, 'sch', 's')
        wordTemp = string.replace(wordTemp, 'sz', 's')
        wordTemp = string.replace(wordTemp, 'y', 'j')
        wordTemp = string.replace(wordTemp, 'd͡ʒ', 'z')
        wordTemp = string.replace(wordTemp, 'sh', 's')
        wordTemp = string.replace(wordTemp, 'zh', 'z')
        wordTemp = string.replace(wordTemp, 'sh', 's')
        wordTemp = string.replace(wordTemp, 'kh', 'k')
        wordTemp = string.replace(wordTemp, 'tz', 't')
        wordTemp = string.replace(wordTemp, 'nn', 'n')
        wordTemp = string.replace(wordTemp, 'mm', 'm')
        wordTemp = string.replace(wordTemp, 'pp', 'p')
        wordTemp = string.replace(wordTemp, 'kk', 'k')
        wordTemp = string.replace(wordTemp, 'zz', 'z')
        wordTemp = string.replace(wordTemp, 'ss', 's')
        wordTemp = string.replace(wordTemp, 'tt', 't')
        wordTemp = string.replace(wordTemp, 'jj', 'j')
        wordTemp = string.replace(wordTemp, 'x', 'ks')
        return wordTemp
        
    @staticmethod
    def getWordWithoutVowels(wordWithVowels):
        wordWithoutVowels = []
        u = unicode(wordWithVowels, "utf-8")
#         wordWithVowelsList = list(wordWithVowels)
        for character in u:
            hexCharacter = hex(ord(character))
            if hexCharacter in Engine.b:
                wordWithoutVowels.append(character)
            if hexCharacter in Engine.c:
                wordWithoutVowels.append(character)
            if hexCharacter in Engine.d:
                wordWithoutVowels.append(character)
            if hexCharacter in Engine.f:
                wordWithoutVowels.append(character)
            if hexCharacter in Engine.h:
                wordWithoutVowels.append(character)
            if hexCharacter in Engine.g:
                wordWithoutVowels.append(character)
            if hexCharacter in Engine.j:
                wordWithoutVowels.append(character)
            if hexCharacter in Engine.k:
                wordWithoutVowels.append(character)
            if hexCharacter in Engine.l:
                wordWithoutVowels.append(character)
            if hexCharacter in Engine.m:
                wordWithoutVowels.append(character)
            if hexCharacter in Engine.n:
                wordWithoutVowels.append(character)
            if hexCharacter in Engine.r:
                wordWithoutVowels.append(character)
            if hexCharacter in Engine.p:
                wordWithoutVowels.append(character)
            if hexCharacter in Engine.s or hexCharacter == '0x282':
                wordWithoutVowels.append(character)
            if hexCharacter in Engine.t:
                wordWithoutVowels.append(character)
            if hexCharacter in Engine.v:
                wordWithoutVowels.append(character)
        
        return wordWithoutVowels
#             
