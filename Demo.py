
import requests

endpoint="http://127.0.0.1:5000/"

print(requests.get(endpoint+'/home').text)
print(requests.get(endpoint+"/articles/Martin Woollacott, former Guardian foreign editor, dies aged 81 | The Guardian | The Guardian").text)
print(requests.get(endpoint+"/articles/author/Kari Paul").text)
print(requests.get(endpoint+"/articles/keyword/manner journalists").text)
