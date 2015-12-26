# -*- coding: utf-8 -*-
'''
Created on 28 Jun 2015

@author: annakeren
'''
import unittest
import sqlite3
# from src.annakeren.ipa.persist import MongoPersistence

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def connectToSqlite(self):
        connection = sqlite3.connect("//Users//annakeren//Documents//workspace//IPAEngine//IPAEngine//ipa.sqlite")
        return connection

    def testConnectToSqlite3(self):
        connection = self.connectToSqlite()
        connection.close()
        print "Sqlite Database created and opened successfully"

    def testThatCanCreateDB(self):
        connection = self.connectToSqlite()
        cursor = connection.cursor()
        cursor.execute("drop table if exists words;")
        cursor.execute("CREATE TABLE words (language1 text, original1 text, ipa1 text, language2 text, original2 text, ipa2 text, resemblance real);")
        
        self.commitAndClose(connection)
    

    def commitAndClose(self, connection):
        connection.commit()
        connection.close()

    def testThatCanInsertToDB(self):
        connection = self.connectToSqlite()
        cursor = connection.cursor()
        
        cursor.execute("INSERT INTO words VALUES('Mandarin','鲍鱼','bàoyú', 'German', 'Abalone', 'Abalone', 20);")
        connection.commit()
        cursor.execute("SELECT * FROM words LIMIT 1;")
    
        data = cursor.fetchone()
        self.assert_(data[0] == 'Mandarin', "Failed to insert data to sqlite3")
        self.assert_(data[3] == 'German', "Failed to insert data to sqlite3")
        self.assert_(data[4] == 'Abalone', "Failed to insert data to sqlite3")
        self.assert_(data[5] == 'Abalone', "Failed to insert data to sqlite3")
        self.assert_(data[6] == 20.0, "Failed to insert data to sqlite3")
        self.commitAndClose(connection)
        
    
#     def testConnectToMongo(self):
#         params = ['localhost', 27017]
#         db = MongoPersistence.MongoPersistence.connect(params)
#         print db
#         pass
# 
#     def testInsert(self):
#         params = ['localhost', 27017]
#         db = MongoPersistence.MongoPersistence.connect(params)
#         db.ipa_engine.drop()
#         
#         basicWord = {'_id': 'id', 
#                      'word':'word', 
#                      'language':'language', 
#                      'consonantTranscript':'consonantTranscript', 
#                      'fullTranscript':'fullTranscript'}
#         db.ipa_engine.insert(basicWord)
#         print db.ipa_engine.find_one()
if __name__ == "__main__":
    unittest.main()