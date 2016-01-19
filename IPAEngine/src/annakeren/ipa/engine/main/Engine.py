'''
Created on 31 May 2015

@author: annakeren
'''
    
class Engine(object):
    
    b=['0x62','0x0253', '0x0299', '0x03B2']
    c=['0x63','0x0254', '0x0255', '0x00E7']
    d=['0x64','0x0257', '0x0256', '0x00F0', '0x02A4']
    f=['0x66','0x025F', '0x0284']
    g=['0x67','0x0261', '0x261', '0x0260', '0x0262', '0x029B', '0x11f']
    h=['0x68','0x78', '0x0266', '0x0267', '0x0127', '0x0265', '0x029C']
    j=['0x6a','0x029D', '0x026D', '0x026C', '0x026B', '0x026E', '0x17e', '0x292']
    k=['0x6b', '0x967', '0x78', '0x71', '0x127'] #h
    l=['0x6c','0x029F', '0x26b']
    m=['0x6d','0x0271', '0x026F', '0x0270']
    n=['0x6e','0x014B', '0x0273', '0x0272', '0x0274', '0x14b']
    r=['0x72','0x281', '0x0279', '0x027A', '0x027E', '0x0280', '0x0281', '0x027D', '0x279']
    p=['0x70']
    s=['0x10d', '0x73', '0x282',
            '0x7a','0x5a','0x0282', 
            '0x0283', '0x161', '0xdf']
    t=['0x74','0x0288', '0x02A7']
    v=['0x76','0x028B', '0x2C71', '0x77']
    
    soundDictionary = [
#                        s,
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
        if firstWordLength == 0 or secondWordLength ==  0:
            return 0
        persentOfWord1 = (float(matchCount) / float(firstWordLength)) * 100.0
        persentOfWord2 = (float(matchCount) / float(secondWordLength)) * 100.0
        
        percent = (persentOfWord1 + persentOfWord2) / 2.0
        return percent
      
    @staticmethod
    def findMatch(firstWord, secondWord):
        shiftGroupBPFV = [
                          '0x62','0x0253', '0x0299', '0x03B2', #b 
                          '0x66','0x025F', '0x0284',#f 
                          '0x70',#p 
                          '0x76','0x028B', '0x2C71', '0x77']#v 
        shiftGroupDTS = [
                         '0x10d', '0x0283', '0x161', '0x17e', '0x282', '0xdf',#s
                        '0x64','0x0257', '0x0256', '0x00F0', '0x02A4',#d 
                        '0x74','0x0288', '0x02A7', #t
                         '0x73', 
                        '0x7a','0x5a','0x0282', '0x283']
        shiftGroupGJHK = [
                        '0x67','0x0261', '0x261', '0x0260', '0x0262', '0x029B', '0x11f',#g 
                        '0x6a','0x029D', '0x026D', '0x026C', '0x026B', '0x026E', '0x292',#j 
                        '0x68','0x78', '0x0266', '0x0267', '0x0127', '0x0265', '0x029C',#h 
                        '0x6b', '0x967', '0x71', '0x127']#k
        shiftGroupLMNR = [
                        '0x6c','0x029F', '0x26b', #l 
                          '0x6d',
                        '0x0271', '0x026F', '0x0270',#m 
                        '0x6e',
                        '0x014B', '0x0273', '0x0272', '0x0274', '0x14b',#n 
                        '0x72','0x281', '0x0279', '0x027A', '0x027E', '0x0280', '0x0281', '0x027D', '0x279'
                          ]#r
    
        foundCounter = 0
        for c1 in firstWord:
            hexC1 = hex(ord(c1))  
            if hexC1 in shiftGroupBPFV:
                for c2 in secondWord:
                    hexC2 = hex(ord(c2)) 
                    if hexC2 in shiftGroupBPFV:
                        foundCounter = foundCounter + 1
                        firstWord = firstWord.replace(c1, "", 1)
                        secondWord = secondWord.replace(c2, "", 1)
                        break
            if hexC1 in shiftGroupGJHK:
                for c2 in secondWord:
                    hexC2 = hex(ord(c2)) 
                    if hexC2 in shiftGroupGJHK:
                        foundCounter = foundCounter + 1
                        firstWord = firstWord.replace(c1, "", 1)
                        secondWord = secondWord.replace(c2, "", 1)
                        break
            if hexC1 in shiftGroupDTS:
                for c2 in secondWord:
                    hexC2 = hex(ord(c2)) 
                    if hexC2 in shiftGroupDTS:
                        foundCounter = foundCounter + 1
                        firstWord = firstWord.replace(c1, "", 1)
                        secondWord = secondWord.replace(c2, "", 1)
                        break
            if hexC1 in shiftGroupLMNR:
                for c2 in secondWord:
                    hexC2 = hex(ord(c2)) 
                    if hexC2 in shiftGroupLMNR:
                        foundCounter = foundCounter + 1
                        firstWord = firstWord.replace(c1, "", 1)
                        secondWord = secondWord.replace(c2, "", 1)
                        break
        return foundCounter
