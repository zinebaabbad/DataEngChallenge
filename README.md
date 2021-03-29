# DataEngChallenge
The aim of this project is to scrap articles from the guardian home page, parse the title, author, name ,date and the full article.The data is stored in a mongodb database.


# Classes description : 
 * Scraping : 
    * newsSiteScraping : getting list of article urls from news site 
    * ArticleScarping : parse the article's author , title , date ,article body and construct a dictionary (json).As for keywords generation we used rake its not a very optimal algorithm but it helps us demonstrate the principle
                        
 * DataBaseUtilities : tackles mongo database connection. NB : usually the conection string should be hided and encrypted but in order for you to test the code I made a default connection string.
 * Api services : rest api routes done with Flask
 * Back end function : In order to seperate back end functionalities from url creation and routing,I created this class with all the functions deployed in the api services
 * Demo :a demonstration of the api services : it calls a local host therefore flask app should be running on the same machine 
