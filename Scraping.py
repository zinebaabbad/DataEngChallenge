from bs4 import BeautifulSoup
import requests

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

        return parsedHtml
    def parseHtmlTag(self,cleanHtml,htmlTagDict):

        tag=htmlTagDict["tag"]
        tagOption=htmlTagDict["tagOption"]
        tagValue=htmlTagDict["tagValue"]
        return cleanHtml.html.find(tag,{ tagOption:tagValue})
    def parseListHtmlTag(self,cleanHtml,htmlTagDict):
        ''' explore site news menu in order to scrape every article's category'''
        tag=htmlTagDict["tag"]
        tagOption=htmlTagDict["tagOption"]
        tagValue=htmlTagDict["tagValue"]
        return cleanHtml.html.find_all(tag,{ tagOption:tagValue})
class ArticleScarping(Scraping):
    def __init__(self, url :str, authorHtmlTag: dict, dateHtmlTag:dict,articleHtmlTag:dict):
        Scraping.__init__(self,url)
        self.authorHtmlTag = authorHtmlTag
        self.dateHtmlTag = dateHtmlTag
        self.articleHtmlTag=articleHtmlTag
        # init keywords extractor


    def parseArticle(self):

        return self.parseHtmlTag(self.parsedHtml,self.articleHtmlTag).get_text()
    def parseAuthor(self):
        return self.parseHtmlTag(self.parsedHtml,self.authorHtmlTag).get_text()
    def parseDate(self):
        try:
            return str( self.parsedHtml.time['datetime'])
        except:
            return self.parseHtmlTag(self.parsedHtml,self.dateHtmlTag).get_text()


    def parseText(self):
        return self.parseHtmlTag(self.parsedHtml,self.articleHtmlTag).get_text()
    def getKeyWords(self):
        '''
        20 a word
        :return:
        '''
        self.rake = Rake(max_length=30)
        self.rake.extract_keywords_from_text(self.parseText())
        result = self.rake.get_ranked_phrases_with_scores()
        return[ elem [1] for elem in result[:10]]

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
        "keywords":self.getKeyWords(),
        "url":self.url}
        return json
class newsSiteScraping(Scraping):
    def __init__(self, url :str, articleHtmlTag: dict):
        Scraping.__init__(self,url)
        self.articleHtmlTag = articleHtmlTag
    def scrapListArticles(self):
        listArticlesHtml=self.parseListHtmlTag(self.parsedHtml,  self.articleHtmlTag )
        listArticles=list(set([elem.get('href') for elem in listArticlesHtml]))
        return listArticles

