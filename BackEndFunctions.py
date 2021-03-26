import Scraping
import DataBaseUtilities
import json
class Functions():

    def __init__(self):
        self.newsSite="https://www.theguardian.com/international"
        # its just an example we can make it more generic by putting all news sites in a config file
        self.articleTag = {"tag":"a","tagOption":"data-link-name","tagValue":"article"}
        self.authorTag = {"tag": "a", "tagOption": "rel", "tagValue": "author"}
        self.dateTag={"tag": "label", "tagOption": "class", "tagValue": "css-hn0k3p"}
        self.articleTextTag={"tag": "div", "tagOption": "class", "tagValue": "article-body-commercial-selector css-79elbk article-body-viewer-selector"}
        self.db=DataBaseUtilities.MongoDataBase()



    def refreshDatabase(self):
            self.articlesList = Scraping.newsSiteScraping(self.newsSite,self.articleTag).scrapListArticles()
            resultJSON=list()
            for elem in self.articlesList:
                try:
                    articleJson=Scraping.ArticleScarping(elem ,self.authorTag, self.dateTag,self.articleTextTag).getArticleJson()
                    resultJSON.append(articleJson)
                    self.db.addEntry(articleJson)
                except:
                    resultJSON.append(elem+" could not be parsed")
                #
            return json.dumps(self.resultJSON)


    def getArticleByName(self,title):
        return json.dumps(self.db.findByTitle(title))

    def getArticleByAuth(self, author):
            return json.dumps(self.db.findByAuthor(author))

    def getArticleBykeyword(self, keyword):
            return json.dumps(self.db.findByKeyword(keyword))

