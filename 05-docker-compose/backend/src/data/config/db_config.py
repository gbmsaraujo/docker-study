from pymongo import MongoClient


class DatabaseConfig(object):

    def __set_config(self):
        try:
            client = MongoClient(
                "mongodb://mongodb:27017/goals_db"
            )
            print("Conectado ao Mongo")
            return client["goals_db"]
        except Exception as e:
            print(e)
            client.close()

    def initilize(self):
        self.__set_config()

    def insert_one(self, collection: str, data: object):
        db = self.__set_config()
        return db[collection].insert_one(data)

    def insert_many(self, collection: str, data: list):
        db = self.__set_config()
        return db[collection].insert_many(data)

    def find(self, collection="", query={}, projection={}):
        db = self.__set_config()

        return db[collection].find(query, projection)

    def update_one(self, collection: str, filter: dict, update: dict):
        db = self.__set_config()
        return db[collection].update_one(filter, update)

    def update_many(self, collection: str, filter: dict, update: dict):
        db = self.__set_config()

        return db[collection].update_many(filter, update)

    def delete_one(self, collection: str, filter: dict):
        db = self.__set_config()
        return db[collection].delete_one(filter)

    def delete_many(self, collection: str, filter: dict):
        db = self.__set_config()
        return db[collection].delete_many(filter)
