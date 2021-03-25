import flask
import BackEndFunctions
app = flask.Flask(__name__)
app.config["DEBUG"] = True
func=BackEndFunctions.Functions()

@app.route('/articles/<title>',methods=['GET'])
def getArticleByName(title):
   return func.getArticleByName(title)

@app.route('/refreshDatabase', methods=['GET'])
def refreshDatabase():
    return func.refreshDatabase()
app.run()