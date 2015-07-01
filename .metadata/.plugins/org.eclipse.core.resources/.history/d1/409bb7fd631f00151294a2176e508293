'''
Created on 28 Jun 2015

@author: annakeren
'''
import pymongo
from pymongo import MongoClient

class MongoPersistence(object):
    '''
    classdocs
    '''

    @staticmethod 
    def connect(params):
        '''
        Constructor
        '''
        client = MongoClient('localhost', 27017)
        db = client.ipa_engine
        post = {"test":"test1"}
        posts = db.posts
        posts.insert_one(post)
        collection = db.ipa_engine
        print collection