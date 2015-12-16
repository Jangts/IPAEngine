'''
Created on 23 Aug 2015

@author: annakeren
'''
import os

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
            
        