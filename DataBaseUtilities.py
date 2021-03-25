from pymongo import MongoClient
class MongoDataBase() :
    def __init__(self,connString=None,database=None,collection=None):
        self.__initConnString__( connString)
        self.client = MongoClient(connString)
        self.__initDatabase__(database)
        self.__initCollection__(collection)

    def __initConnString__(self,connString):
        if connString is None :
            #default CONNSTRING
            self.connectionString="mongodb+srv://userGemography:6IXYIGz8tiMnuCs2@cluster0.1kqjy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        else:
            self.connectionString=connString


    def __initDatabase__(self, database):
        if database is None:
            # default database
            self.database = self.client['datacampdb']
        else:
            self.database = self.client[database]

    def __initCollection__(self, collection):
        if collection is None:
            # default database
            self.collection = self.database['datacampdb']
        else:
            self.collection = self.database[collection]

    def addEntry(self,articleJson):
        return self.collection.insert(articleJson)
    def findEntry(self,field,fieldValue):
        return self.collection.find( {field: fieldValue})
    def findByKeyword(self, keyWord):
        return self.findEntry("keyword", keyWord)
    def findByTitle(self, title):
        return self.findEntry("title", title)
    def textSearch(self,textSearch):
        self.collection.createIndex( { "name": "text", "description": "text" } )
        return self.collection.find( { "$text": { "$search": textSearch } } )