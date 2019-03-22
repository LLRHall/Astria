from elasticsearch import Elasticsearch
from flask import Flask
import requests

es = Elasticsearch("http://localhost:9200")
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "LLR Open Soft 2019"

@app.route('/query1',methods=['GET','POST'])
def query1():
   
   query = requests.get_json()
   
   keywordsList = query['query']
   
   searchString=""
   for q in keywordsList:
      searchString+=q+','

   searchString=searchString[:-1]
   res = es.search(index="cases",body={"query":{"match":{"legal-key":searchString}}})

   for cases in res['hits']['hits']:
      print(cases['_source']['title'])

   return res['hits']['hits']

if __name__ == '__main__':
   app.run(debug=True)
