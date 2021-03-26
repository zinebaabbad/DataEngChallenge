import Scraping
import DataBaseUtilities




class Functions():

    def __init__(self):
        self.newsSite="https://www.theguardian.com/international"
        # its just an example we can make it more generic by putting all news sites in a config file
        self.articleTag = {"tag":"a","tagOption":"data-link-name","tagValue":"article"}
        self.authorTag = {"tag": "a", "tagOption": "rel", "tagValue": "author"}
        self.dateTag={"tag": "label", "tagOption": "for", "tagValue": "dateToggle"}

        self.articleTextTag={"tag": "div", "tagOption": "class", "tagValue": "article-body-commercial-selector css-79elbk article-body-viewer-selector"}

        self.db=DataBaseUtilities.MongoDataBase()



    def refreshDatabase(self):

            self.articlesList = Scraping.newsSiteScraping(self.newsSite,self.articleTag).scrapListArticles()
            for elem in self.articlesList:
                try:
                    articleJson=Scraping.ArticleScarping(elem ,self.authorTag, self.dateTag,self.articleTextTag).getArticleJson()
                    print(articleJson)
                    self.db.addEntry(articleJson)
                except:
                    print(elem+" could not be parsed")
                #
            return self.articlesList


    def getArticleByName(self,title):
        return self.db.findByTitle(title)

    def getArticleByAuth(self, title):
            self.db.findByAuthor(title)
        getArticleByAuth

Functions().getArticleByName("Martin Woollacott, former Guardian foreign editor, dies aged 81 | The Guardian | The Guardian")