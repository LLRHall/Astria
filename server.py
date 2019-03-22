from elasticsearch import Elasticsearch
from flask import Flask,request

es = Elasticsearch("http://localhost:9200")
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "LLR Open Soft 2019"

@app.route('/query1',methods=['GET','POST'])
def query1():
   
   query = request.get_json()
   # print(query)
   
   keywordsList=query[0]['query']
   fromDate=query[0]['time']['from']
   toDate=query[0]['time']['to']
   cat=query[0]['cat']
   act=query[0]['act']
   judge=query[0]['judge']
   
   # print(type(keywordsList))
   searchString=""
   for q in keywordsList:
      searchString+=q+','

   searchString=searchString[:-1]
   res = es.search(index="cases",
   body={"query":{
   "match":{"legal-key":searchString},
   "range" : {"date" : {"gte":"2 Oct 1980","lte":"2 Oct 2000","format":"dd  M  yyyy||dd  M  yyyy"}}}})

   for cases in res['hits']['hits']:
      print(cases['_source']['title'])

   return "OK"

if __name__ == '__main__':
   app.run(debug=True)
