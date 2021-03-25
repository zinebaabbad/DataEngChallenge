from bs4 import BeautifulSoup
import requests
from readability import Document
from rake_nltk import Rake

class Scraping(object):
    def __init__(self,url):
        self.url = url
        self.html = self.loadURL(url)
        self.parsedHtml = self.scrapHtml(self.html)

    def loadURL(self,url:str):

        response=requests.get(url)
        response.raise_for_status()
        return response.text

    def scrapHtml(self,html:str):
        parsedHtml = BeautifulSoup(html, 'html.parser')
        cleanHtml = Document(parsedHtml).get_clean_html()
        return cleanHtml
    def parseHtmlTag(self,cleanHtml,htmlTag, htmlOption, htmlValue):
        ''' explore site news menu in order to scrape every article's category'''
        return cleanHtml.html.find(htmlTag,{ htmlOption:htmlValue})
    def parseListHtmlTag(self,cleanHtml,htmlTag, htmlOption, htmlValue):
        ''' explore site news menu in order to scrape every article's category'''
        return cleanHtml.html.find_all(htmlTag,{ htmlOption:htmlValue})
class ArticleScarping(Scraping):
    def __init__(self, url :str, authorHtmlTag: dict, dateHtmlTag:dict):
        Scraping.__init__(self,url)
        self.authorHtmlTag = authorHtmlTag
        self.dateHtmlTag = dateHtmlTag
        # init keywords extractor
        self.rake = Rake()

    def parseArticle(self):
        return self.parsedHtml.get_text()
    def parseAuthor(self):
        tag=self.authorHtmlTag["tag"]
        tagOption=self.authorHtmlTag["tagOption"]
        tagValue=self.authorHtmlTag["tagValue"]
        return self.parsedHtml(tag, {tagOption:tagValue}).get_text()
    def parseDate(self):
        tag=self.dateHtmlTag["tag"]
        tagOption=self.dateHtmlTag["tagOption"]
        tagValue=self.dateHtmlTag["tagValue"]
        return self.parsedHtml(tag, {tagOption:tagValue}).get_text()
    def parseText(self):
        return self.parsedHtml.get_text()
    def getKeyWords(self):
        self.rake.extract_keywords_from_text(self.parsedHtml)
    def parseTitle(self):
        title="nan"
        if (self.parsedHtml.title is not None):
            title = self.parsedHtml.title.string
        return title
    def getArticleJson(self):
        json={"title" :self.parseTitle(),
        "date":self.parseDate(),
        "author":self.parseAuthor(),
        "article":self.parseText(),
        "keywords":self.getKeyWords(),}
        return json
class newsSiteScraping(Scraping):
    def __init__(self, url :str, articleHtmlTag: dict):
        Scraping.__init__(self,url)
        self.articleHtmlTag = articleHtmlTag
    def scrapListArticles(self):
        listArticles=[elem.find("href").get_text() for elem in self.parseListHtmlTag(self.parsedHtml)]
        return listArticles

