from pymongo import MongoClient

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password, host, port, db, collection):
        # Initialize the MongoClient
        self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}/?directConnection=true')
        self.database = self.client[db]
        self.collection = self.database[collection]

    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)  # data should be dictionary            
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

    def read(self, query):
        if query is not None:
            cursor = self.collection.find(query)
            result = [document for document in cursor]
            return result
        else:
            raise Exception("Query is empty")
            return []

    def update(self, query, update_data):
        if query is not None and update_data is not None:
            result = self.collection.update_many(query, {'$set': update_data})
            return result.modified_count
        else:
            raise Exception("Query or update_data is empty")
            return 0

    def delete(self, query):
        if query is not None:
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            raise Exception("Query is empty")
            return 0

