from abc import ABC, abstractmethod


class DatabaseFactory(ABC):

    @abstractmethod
    def initilize(self):
        pass

    @abstractmethod
    def insert_one(self, collection: str, data: object):
        pass

    @abstractmethod
    def insert_many(self, collection: str, data: list):
        pass

    @abstractmethod
    def find(self, collection="", query={}, projection={}):
        pass

    @abstractmethod
    def update_one(self, collection: str, filter: dict, update: dict):
        pass

    @abstractmethod
    def update_many(self, collection: str, filter: dict, update: dict):
        pass

    @abstractmethod
    def delete_one(self, collection: str, filter: dict):
        pass

    @abstractmethod
    def delete_many(self, collection: str, filter: dict):
        pass
