'''
Created on 26 Dec 2015

@author: annakeren
'''
import sqlite3

class SqlitePersistence(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    
    @staticmethod 
    def connect(fileName):
        connection = sqlite3.connect(fileName)
        return connection
    
    @staticmethod
    def createTableWords(connection):
        cursor = connection.cursor()
        cursor.execute("drop table if exists words;")
        cursor.execute("CREATE TABLE words (language1 text, original1 text, ipa1 text, language2 text, original2 text, ipa2 text, resemblance real, matches real);")
        
    @staticmethod
    def insert(db, post):
        posts = db.posts
        posts.insert_one(post)
        return posts
