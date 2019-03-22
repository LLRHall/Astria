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
   
    "bool": {
        "must":     { "match":{"legal-key":searchString}},
        "filter": [
           { "match":{"judge":judge}}
        ]
    }

   }})
   print("result is")
   for cases in res['hits']['hits']:
      print(cases['_source']['judge'])

   return "Yo"

if __name__ == '__main__':
   app.run(debug=True)
