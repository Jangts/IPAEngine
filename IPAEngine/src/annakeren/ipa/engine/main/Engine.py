'''
Created on 31 May 2015

@author: annakeren
'''
    
class Engine(object):
    
    b=['0x62','0x0253', '0x0299', '0x03B2']
    c=['0x63','0x0254', '0x0255', '0x00E7']
    d=['0x64','0x0257', '0x0256', '0x00F0', '0x02A4']
    f=['0x66','0x025F', '0x0284']
    g=['0x67','0x0261', '0x0260', '0x0262', '0x029B', '0x11f']
    h=['0x68','0x78', '0x0266', '0x0267', '0x0127', '0x0265', '0x029C']
    j=['0x6a','0x029D', '0x026D', '0x026C', '0x026B', '0x026E', '0x17e', '0x292']
    k=['0x6b', '0x967', '0x78', '0x71'] #h
    l=['0x6c','0x029F', '0x26b']
    m=['0x6d','0x0271', '0x026F', '0x0270']
    n=['0x6e','0x014B', '0x0273', '0x0272', '0x0274', '0x14b']
    r=['0x72','0x281', '0x0279', '0x027A', '0x027E', '0x0280', '0x0281', '0x027D', '0x279']
    p=['0x70']
    s=['0x73', 
            '0x7a','0x5a','0x0282', 
            '0x0283', '0x161', '0x10d']
    t=['0x74','0x0288', '0x02A7']
    v=['0x76','0x028B', '0x2C71', '0x77']
    
    soundDictionary = [
                            b, 
                            c, 
                            d, 
                            f, 
                            g, h, j, k, 
                            l, 
                           m, n, 
                            r, 
                            p, 
                           s, 
                            t,
                             v
                            ]
        
    @staticmethod    
    def percentage(matchCount, firstWordLength, secondWordLength):    
        percent = 0
        if matchCount > 0:
            if firstWordLength == secondWordLength:
                if secondWordLength <> 0:
                    percent = (float(firstWordLength)/float(secondWordLength))*100.0
            
            
            if firstWordLength < secondWordLength:
                if secondWordLength <> 0:
                    percent = (float(firstWordLength)/float(secondWordLength))*100.0
            
            if firstWordLength > secondWordLength:
                if firstWordLength <> 0:
                    percent = (float(secondWordLength)/float(firstWordLength))*100.0
        return percent
      
    @staticmethod
    def findMatch(firstWord, secondWord):
        shiftGroupBPFV = [
                          '0x62','0x0253', '0x0299', '0x03B2', #b 
                          '0x66','0x025F', '0x0284',#f 
                          '0x70',#p 
                          '0x76','0x028B', '0x2C71', '0x77']#v 
        shiftGroupDTS = [
                        '0x64','0x0257', '0x0256', '0x00F0', '0x02A4',#d 
                        '0x74','0x0288', '0x02A7', #t
                         '0x73', 
                        '0x7a','0x5a','0x0282', 
                         '0x0283', '0x161', '0x10d', '0x17e']#s
        shiftGroupGJHK = ['0x67','0x0261', '0x0260', '0x0262', '0x029B', '0x11f',#g 
                        '0x6a','0x029D', '0x026D', '0x026C', '0x026B', '0x026E', '0x292',#j 
                        '0x68','0x78', '0x0266', '0x0267', '0x0127', '0x0265', '0x029C',#h 
                        '0x6b', '0x967', '0x71']#k
        shiftGroupLMNR = [
                        '0x6c','0x029F', '0x26b', #l 
                          '0x6d',
                        '0x0271', '0x026F', '0x0270',#m 
                        '0x6e',
                        '0x014B', '0x0273', '0x0272', '0x0274', '0x14b',#n 
                          '0x72','0x281', '0x0279', '0x027A', '0x027E', '0x0280', '0x0281', '0x027D', '0x279'
                          ]#r
        shiftDictionary = [
                            shiftGroupBPFV,
                           shiftGroupDTS,
                            shiftGroupGJHK,
                            shiftGroupLMNR
                           ] 
    
        foundCounter = 0
        soundIterator = 0
        for c in firstWord:
#             exact match
            soundIterator = soundIterator + 1
            found = secondWord.find(c)
            if found > -1:
                foundCounter = foundCounter + 1
            else:
                for soundDictionaryEntry in Engine.soundDictionary:
                    for sound in soundDictionaryEntry:
                        if unichr(int(sound, 16))== c:
                            found = secondWord.find(unichr(int(sound, 16)))
                            if found > -1:
                                foundCounter = foundCounter + 1
                if soundIterator > foundCounter & foundCounter< len(firstWord):
                    for shiftGroup in shiftDictionary:
                        hexC = hex(ord(c))
                        if hexC in shiftGroup:
                            for c2 in secondWord:
                                for shift in shiftGroup:
                                    if unichr(int(shift, 16))== c2:
                                        foundCounter = foundCounter + 1
        
        return foundCounter
