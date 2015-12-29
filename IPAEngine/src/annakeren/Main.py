'''
Created on 24 Aug 2015

@author: annakeren


'''

import time, re, urllib

from src.annakeren.wikiIPA.wikiIPA.WiktionarySpider import WiktionarySpider
from src.annakeren.wikiIPA.wikiIPA import Utils

def getTranslationsForAllWordsStartingWithLetter(wordsA, WiktionarySpider):
    ipaPattern = re.compile('<span class="IPA" lang="">(.*?)\</span>')
    translations = []
    for wordA in wordsA:
        try:
            ipaSpans = re.findall(ipaPattern, urllib.urlopen(wordA).read())
            time.sleep(10)
            if ipaSpans:
                socket = urllib.urlopen(wordA)
                page = socket.read()
#                 parsed_html = BeautifulSoup(page, "lxml")
                name = wordA.rsplit('/',1)[1]
                Utils.Utils.createNewFileAndWrite("/Users/annakeren/ipa/"+name+".html", page)
                socket.close()
#                 translation = WiktionarySpider.getTranslation(wordA)
#                 translations.append(translation)
        except:
            pass
    return translations

if __name__ == '__main__':
    
# extract 5 translations from every word
# save translations to csv file
    files = Utils.Utils.readAllFilesFromFolder("/Users/annakeren/ipa")
    translations = []
    translation = []
    for file in files:
        socket = urllib.urlopen(file)
        filePathSplit = re.split('/',file)
        filePathSplitLength = len(filePathSplit)
        fileName = filePathSplit[filePathSplitLength - 1]
        
        page = socket.read()
        
        translation = WiktionarySpider.getTranslation(page, fileName)
        translations.append(translation)
        socket.close          
    
    fileName = "/Users/annakeren/ipa/wictionary.csv"  
    counter = 0          
    for translation in translations:
        if(len(translation) > 2):
            counter = counter + 1
            Utils.Utils.writeToCsvFile(fileName, translation) 
    print counter

    pass