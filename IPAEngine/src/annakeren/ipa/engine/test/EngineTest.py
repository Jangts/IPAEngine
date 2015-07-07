import unittest

from src.annakeren.ipa.engine.main import Engine
from src.annakeren.ipa.engine.main import ComparisonPersistence

class EngineTest(unittest.TestCase):    
    
    def testComparePersistSpongeSfog(self):
        print 'English and Hebrew'
        sponge = unichr(0x73)+unichr(0x70)+unichr(0x6e)+unichr(0x02A4)
        sfog = unichr(0x73)+unichr(0x66)+unichr(0x67)
        print '(sponge)' + sponge + ' vs ' + sfog + '(sfog)'
        
        words  = [
                  'sponge', 'English', 'sponge', sponge,
                  'sfog', 'Hebrew', 'sfog', sfog
                  ]
        connectionParams = ['localhost', 27017]
        dbConnection = ComparisonPersistence.ComparisonPersistence.connectToDB(connectionParams)
        dbConnection.posts.drop()
        ComparisonPersistence.ComparisonPersistence.compareAndPerist(words, dbConnection)
        print dbConnection.posts.find()
    
    def testComparePersistSugarSaharSukar(self):
        print 'English and Russian'
        sugar = unichr(0x0283)+unichr(0x67)
        sahar = unichr(0x73)+unichr(0x78)+unichr(0x72)
        sukar = unichr(0x73)+unichr(0x6b)+unichr(0x281)
        print '(sugar)' + sugar + ' vs ' + sahar + '(sahar)'
        
        wordsSugarSahar  = [
                  'suggr', 'English', 'sugar', sugar,
                  'sahar', 'Russian', 'sahar', sahar
                  ]
        connectionParams = ['localhost', 27017]
        dbConnection = ComparisonPersistence.ComparisonPersistence.connectToDB(connectionParams)
        dbConnection.posts.drop()
        ComparisonPersistence.ComparisonPersistence.compareAndPerist(wordsSugarSahar, dbConnection)
        
        wordsSugarSukar = [
                  'sugar', 'English', 'sugar', sugar,
                  'sukar', 'Hebrew', 'sukar', sukar
                  ]
        print 'English and Hebrew'
        print '(sugar)' + sugar + ' vs ' + sukar + '(sukar)'
        ComparisonPersistence.ComparisonPersistence.compareAndPerist(wordsSugarSukar, dbConnection)
        
        wordsSaharSukar = [
                  'sahar', 'Russian', 'sahar', sahar,
                  'sukar', 'Hebrew', 'sukar', sukar
                  ]
        print 'Russian and Hebrew'
        print '(sahar)' + sahar + ' vs ' + sukar + '(sukar)'
        ComparisonPersistence.ComparisonPersistence.compareAndPerist(wordsSaharSukar, dbConnection)
        
        print dbConnection.posts.find()
        
#     def testComparePersistGoldZoloto(self):
#         print 'English and Russian'
#         gold = unichr(0x67)+unichr(0x6c)+unichr(0x64)
#         zoloto = unichr(0x7a)+unichr(0x6c)+unichr(0x74)
#         print '(gold)' + gold + ' vs ' + zoloto + '(zoloto)'
#         
#         words  = [
#                   'gold', 'English', 'gould', gold,
#                   'stand', 'Russian', 'zoloto', zoloto
#                   ]
#         connectionParams = ['localhost', 27017]
#         dbConnection = ComparisonPersistence.ComparisonPersistence.connectToDB(connectionParams)
# #         dbConnection.posts.drop()
#         ComparisonPersistence.ComparisonPersistence.compareAndPerist(words, dbConnection)
#         print dbConnection.posts.find()
#     
#     def testComparePersistStandStand(self):
#         print 'English consonant shift in connected speech:'
#         stand = unichr(0x73)+unichr(0x74)+unichr(0x6e)+unichr(0x64)
#         stamb = unichr(0x73)+unichr(0x74)+unichr(0x6d)+unichr(0x62)
#         print '(stand)' + stand + ' vs ' + stamb + '(like in stand back)'
#         
#         words  = [
#                   'stand', 'English', 'stand', stand,
#                   'stand', 'English', 'stamb', stamb
#                   ]
#         connectionParams = ['localhost', 27017]
#         dbConnection = ComparisonPersistence.ComparisonPersistence.connectToDB(connectionParams)
#         dbConnection.posts.drop()
#         ComparisonPersistence.ComparisonPersistence.compareAndPerist(words, dbConnection)
#         print dbConnection.posts.find()
#     
#     def testStandStamb(self):
#         print 'English consonant shift in connected speech:'
#         stand = unichr(0x73)+unichr(0x74)+unichr(0x6e)+unichr(0x64)
#         stamb = unichr(0x73)+unichr(0x74)+unichr(0x6d)+unichr(0x62)
#         print '(stand)' + stand + ' vs ' + stamb + '(like in stand back)'
#         actual = Engine.Engine.findMatch(stamb, stand)
#         self.assertEqual(4, actual, "msg")
#             
#     def testNaiceNaish(self):
#         print "English consonant shift in connected speech:"
#         naice = unichr(0x6e) + unichr(0x73)
#         naish = unichr(0x6e) + unichr(0x0283)
#         print '(nice)' +naice + ' vs ' + naish + '(like in nice shoes)'
#         actual = Engine.Engine.findMatch(naice, naish)
#         self.assertEqual(2, actual, "msg")
#             
#     def testZaeSea(self):
#         print 'English consonant shift in connected speech:'
#         sea = unichr(0x73)
#         zea = unichr(0x7a)
#         print '(sea)' + sea + ' vs ' + zea + '(like in swansea)'
#         actual = Engine.Engine.findMatch(zea, sea)
#         self.assertEqual(1, actual, "msg")
#             
#     def testSnegSnowSheleg(self):
#         print 'Russian and English'
#         sneg = unichr(0x73) + unichr(0x6e) + unichr(0x67)
#         snow = unichr(0x73) + unichr(0x6e)
#         sheleg = unichr(0x0283) + unichr(0x6c) + unichr(0x67)
#         print '(sneg)' + sneg + ' vs ' + snow + '(snow)'
#     
#         actualSnegSnow = Engine.Engine.findMatch(sneg, snow)
#         self.assertEqual(3, actualSnegSnow, "msg")
#             
#         print 'English and Hebrew'
#         print '(snow)' + snow + ' vs ' + sheleg + '(sheleg)'
#         actualSnowSheleg = Engine.Engine.findMatch(snow, sheleg)
#         self.assertEqual(2, actualSnowSheleg, "msg")
#             
#         print 'Russian and Hebrew'
#         print '(sheleg)' + sheleg + ' vs ' + sneg + '(sneg)'
#         actualSnegSheleg = Engine.Engine.findMatch(sneg, sheleg)
#         self.assertEqual(3, actualSnegSheleg, "msg")
#        
#     def testShemeshSolnzeSun(self):
#         print 'Russian and English'
#         sun = unichr(0x73) + unichr(0x6e)
#         solnze = unichr(0x73) + unichr(0x6c) + unichr(0x6e) + unichr(0x74) + unichr(0x73)
#         shemesh = unichr(0x0283) + unichr(0x6d) + unichr(0x0283)
#         print '(solnze)' + solnze + ' vs ' + sun + '(sun)'
#    
#         actualSolnzeSun = Engine.Engine.findMatch(solnze, sun)
#         self.assertEqual(5, actualSolnzeSun, "msg")
#            
#         print 'English and Hebrew'
#         print  '(sun)' + sun + ' vs ' + shemesh + '(shemesh)'  
#         actualSunShemesh = Engine.Engine.findMatch(sun, shemesh)
#         self.assertEqual(2, actualSunShemesh, "msg")
#            
#         print 'Russian and Hebrew'
#         print '(solnze)' + solnze + ' vs ' + shemesh + '(shemesh)'
#         actualSolnzeShemesh = Engine.Engine.findMatch(solnze, shemesh)
#         self.assertEqual(5, actualSolnzeShemesh, "msg")
#            
#     def testStarZvezda(self):  
#         print 'English and Russian'
#         star = unichr(0x73) + unichr(0x74)
#         zvezda = unichr(0x7a) + unichr(0x76) + unichr(0x7a) + unichr(0x64)
#         print '(star)' + star + ' vs ' + zvezda + '(zvezda)'
#         actualStarZvezda = Engine.Engine.findMatch(star, zvezda)
#         self.assertEqual(2, actualStarZvezda, "msg")
#            
#     def testWindVeter(self):  
#         print 'English and Russian'
#         wind = unichr(0x77) + unichr(0x6e) + unichr(0x64)
#         veter = unichr(0x76) + unichr(0x74) + unichr(0x72) + unichr(0x64)
#         print '(wind)' + wind + ' vs ' + veter + '(veter)'
#         actualWindVeter = Engine.Engine.findMatch(wind, veter)
#         self.assertEqual(3, actualWindVeter, "actual counter")
#            
#     def testSilkSholkMeshiSi(self):
#         print "English and Russian"
#         silk = unichr(0x73) + unichr(0x6c) + unichr(0x6b)
#         sholk = unichr(0x0283) + unichr(0x6c) + unichr(0x6b)
#         meshi = unichr(0x6d) + unichr(0x283)
#         si = unichr(0x73)
#           
#         print '(silk)' + silk + ' vs ' + sholk + '(sholk)'
#         actualSilkSholk =Engine.Engine.findMatch(silk, sholk)
#         self.assertEqual(3, actualSilkSholk, 'msg')
#           
#         print 'Mandarine and English'
#         print  si + '(si)' + ' vs ' +  '(silk)' + silk
#         actualSilkSi =Engine.Engine.findMatch(si, silk)
#         self.assertEqual(1, actualSilkSi, 'msg')
#           
#         print 'Mandarine and Hebrew'
#         print  si + '(si)' + ' vs ' +  '(meshi)' + meshi
#         actualSiMeshi =Engine.Engine.findMatch(si, meshi)
#         self.assertEqual(1, actualSiMeshi, 'msg')
#      
#     def testNasichKnyazi(self):
#         print 'Hebrew and Russian'
#         nasich = unichr(0x64) + unichr(0x73) + unichr(0x967)
#         knyazi = unichr(0x6b) + unichr(0x6e) + unichr(0x7a)
#         actualNasichKnyazi =Engine.Engine.findMatch(nasich, knyazi)
#         self.assertEqual(3, actualNasichKnyazi, 'msg')