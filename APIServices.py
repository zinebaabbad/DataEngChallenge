import flask
import BackEndFunctions
app = flask.Flask(__name__)
app.config["DEBUG"] = True
func=BackEndFunctions.Functions()


@app.route('/home',methods=['GET'])
def gethome():
   return "Welcome "
@app.route('/articles/<title>',methods=['GET'])
def getArticleByName(title):
   return func.getArticleByName(title)
@app.route('/articles/author/<author>',methods=['GET'])
def getArticleByAuth(author):
   return func.getArticleByAuth(author)
@app.route('/articles/keyword/<keyword>',methods=['GET'])
def getArticleBykeyword(keyword):
   return func.getArticleBykeyword(keyword)

@app.route('/refreshDatabase', methods=['GET'])
def refreshDatabase():
    return func.refreshDatabase()



############################################################################TEST#####################################################################
app.run()
