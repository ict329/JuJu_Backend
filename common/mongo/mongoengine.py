from mongoconf import *
from pymongo import MongoClient

class MGEngine:
    def __init__(self):
        self.client = MongoClient(MONGO_CONFIG['HOST'], MONGO_CONFIG['PORT'])
        dbname = MONGO_CONFIG['DB']
        self.db = self.client[dbname]
    

    """
    tablename string
    condition dictionary
    order dictionary
    returnfields range
    offset int
    limit int
    multiple boolean


    """

    def find(self,tablename,condition,order,returnfileds,offset,limit):
        return None

    def update(self,tablename,condition,update,multiple):
        return None

    def insert(self,tablename,condition):
        return None
    
    def delete(self,tablename,condition):
        return None
    
    def count(self,tablename,condition):
        return None


"""
find
insert
update
delete

"""

engine = MGEngine()
