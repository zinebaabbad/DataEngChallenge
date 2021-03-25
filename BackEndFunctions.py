import Scraping
import DataBaseUtilities



def exception_decorator(func):
    def new_func(*args, **kwargs):
        try:
            ret = func(*args, **kwargs)
            return ret
        except Exception as e:
            return str("500 A server error occurred please contact the administrator error : "+str(e))
    return new_func()
class Functions():

    def __init__(self):
        self.newsSite="https://www.theguardian.com/international"
        # its just an example we can make it more generic by putting all news sites in a config file
        self.articleTag = {"tag":"a","tagOption":"data-link-name","tagValue":"article"}
        self.authorTag = {"tag": "a", "tagOption": "rel", "tagValue": "author"}
        self.dateTag={"tag": "label", "tagOption": "for", "tagValue": "dateToggle"}
        self.db=DataBaseUtilities.MongoDataBase()

    @exception_decorator
    def refreshDatabase(self):

            self.articlesList = Scraping.newsSiteScraping(self.articleTag).scrapListArticles()
            for elem in self.articlesList:
                articleJson=Scraping.Article(elem ,self.authorTag, self.dateTag).getArticleJson()
                self.db.addEntry(articleJson)
            return self.articlesList

    @exception_decorator
    def getArticleByName(self,title):
        self.db.findByTitle(title)
f=Functions().refreshDatabase()
Functions().getArticleByName("")