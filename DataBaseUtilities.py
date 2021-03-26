from pymongo import MongoClient
class MongoDataBase() :
    def __init__(self,connectionString="mongodb+srv://zineb:zineb@cluster0.itycp.mongodb.net/Blog?retryWrites=true&w=majority",database=None,collection=None):
        self._initConnString_(connectionString)
        self.client = MongoClient(connectionString)
        self._initDatabase_(database)
        self._initCollection_(collection)


    def _initConnString_(self,connectionString):
            self.connectionString=connectionString


    def _initDatabase_(self, database):
        if database is None:
            # default database
            self.database = self.client["Blog"]
        else:
            self.database = self.client[database]

    def _initCollection_(self, collection):
        if collection is None:
            # default database
            self.collection = self.database["articles"]
        else:
            self.collection = self.database[collection]

    def addEntry(self,articleJson):
        return self.collection.insert_one(articleJson)
    def findEntry(self,field,fieldValue):
        return self.collection.find_one( {field: fieldValue})
    def findByKeyword(self, keyWord):
        return self.findEntry("keywords", keyWord)
    def findByTitle(self, title):
        return self.findEntry("title", title)
    def findByAuthor(self, author):
        return self.findEntry("author", author)
