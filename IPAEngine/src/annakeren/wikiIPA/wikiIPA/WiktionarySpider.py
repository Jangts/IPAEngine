'''
Created on 6 Aug 2015

@author: annakeren
'''
import re, urllib, time
from bs4 import BeautifulSoup  


class WiktionarySpider(object):
    '''
    classdocs
    '''

    @staticmethod
    def getTranslation(page, fileName):
#   
        translation = []
        try:
            parsed_html = BeautifulSoup(page, "lxml")
            translationsTable = parsed_html.body.find('table', attrs={'class':'translations'})
            ipa = parsed_html.find('span', attrs={'class':'IPA'})
            ipas = ipa.text.split()
            
            
            lists = translationsTable.find_all('li')
            
            for list in lists:
                splitEntry = list.text.split()
                language = splitEntry[0]
                if(language=="Chinese:"):
                    language = splitEntry[1]
                    originalWord = splitEntry[4]
                    ipaContainig = splitEntry[6]
                    mandarinTranslation = []
                    mandarinTranslation.append(language)
                    mandarinTranslation.append(originalWord)
                    mandarinTranslation.append(ipaContainig)
                    translation.append(mandarinTranslation)
                     
                if(language=="German:"):
                    originalWord = splitEntry[1]
                    ipaContainig = splitEntry[4]
                    germanTranslation = []
                    germanTranslation.append(language)
                    germanTranslation.append(originalWord)
                    germanTranslation.append(ipaContainig)
                    translation.append(germanTranslation)
                 
                if(language=="Hebrew:"):
                    originalWord = splitEntry[1]
                    ipaContainig = splitEntry[4]
                    hebrewTranslation = []
                    hebrewTranslation.append(language)
                    hebrewTranslation.append(originalWord)
                    hebrewTranslation.append(ipaContainig)
                    translation.append(hebrewTranslation)
                 
                if(language=="Persian:"):
                    originalWord = splitEntry[1]
                    ipaContainig = splitEntry[3]
                    persianTranslation = []
                    persianTranslation.append(language)
                    persianTranslation.append(originalWord)
                    persianTranslation.append(ipaContainig)
                    translation.append(persianTranslation)
    #             if(language=="Romanian:"):
    #                 originalWord = splitEntry[1]
    #                 ipaContainig = splitEntry[4]
    #                 translation.append(language)
    #                 translation.append(originalWord)
    #                 translation.append(ipaContainig)
                     
                if(language=="Russian:"):
                    originalWord = splitEntry[1]
                    ipaContainig = splitEntry[4]
                    russianTranslation = []
                    russianTranslation.append(language)
                    russianTranslation.append(originalWord)
                    russianTranslation.append(ipaContainig)
                    translation.append(russianTranslation)
        except:
            pass
        if(len(translation) > 0):
            translation.append(fileName)
            translation.append(ipas[0])
        return translation    
        
    @staticmethod 
    def getWords(urlToEnglishLetter):
        print urlToEnglishLetter
        pattern = re.compile('^\/wiki/[a-z]{3,}')
        matches = []
        
        enIpas = []
        
        urllib.URLopener.version = 'annakeren/1.1 (https://uk.linkedin.com/in/annakeren; anna.keren.me@gmail.com) BasedOnSuperLib/1.4'
        try:            
            for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(urlToEnglishLetter).read(), re.I):
                link = i
                match = re.match(pattern, link)
                if match:
                    matches.append(match)

            ipaPattern = re.compile('<span class="IPA" lang="">(.*?)\</span>')
        
            
            
            for match in matches:
                ipaSpans = re.findall(ipaPattern, urllib.urlopen("https://en.wiktionary.org"+match.group()).read())
                if ipaSpans: 
                    enIpas.append("https://en.wiktionary.org"+match.group()) 
                    print "https://en.wiktionary.org"+match.group()
                time.sleep(15)
        except:
            pass
        
        return enIpas
        '''
        Constructor
        '''
        