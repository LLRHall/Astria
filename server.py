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
   # print(toDate)
   searchString=""
   for q in keywordsList:
      searchString+=q+','

   searchString=searchString[:-1]
   res = es.search(index="cases",
   body={"query":{
   
    "bool": {
        "must": { "match":{"legal-key":searchString}},
        "filter": [
           { "match":{"judge":judge}},
           { "match":{"act-used":act}},
           { "match":{"case-cat":cat}},
           { "range": {"date" : {"gte":"1 January 1900","lte":"1 January 2500", "format":"d M y || d M y"}}}
        ]
    }

   }})
   print("result is")
   for cases in res['hits']['hits']:
      print(cases['_source']['judge'])

   return "Yo"

@app.route('/query2',methods=['GET','POST'])
def query2():
   
   query = request.get_json()
   # print(query)
   
   actquery=query[0]['query']
   fromDate=query[0]['time']['from']
   toDate=query[0]['time']['to']
   cat=query[0]['cat']
   act=query[0]['act']
   judge=query[0]['judge']
   
   # print(type(keywordsList))
   # print(toDate)
   
   print(actquery[0])
   res = es.search(index="acts",
   body={"query":{
    "bool": {
        "must": { "match":{"Act_Name":actquery[0]}},
    }
   }})

   file_list=[]
   x =[]
   for acts in res['hits']['hits']:
      
      x.append(acts['_source']['File_Name'].replace(' ','').split(','))

   print(x)
   print(file_list)
   return "Yo"

@app.route('/query3',methods=['GET','POST'])
def query3():
   
   query = request.get_json()
   # print(query)
   
   searchString=query[0]['query']
   fromDate=query[0]['time']['from']
   toDate=query[0]['time']['to']
   cat=query[0]['cat']
   act=query[0]['act']
   judge=query[0]['judge']
   
   # print(type(keywordsList))
   # print(toDate)
   #  = 

   # searchString=searchString[:-1]
   res = es.search(index="cases",
   body={"query":{
   
    "bool": {
        "must": { "match":{"title":searchString}},
        "filter": [
           { "match":{"judge":judge}},
           { "match":{"act-used":act}},
           { "match":{"case-cat":cat}},
           { "range": {"date" : {"gte":"1 January 1900","lte":"1 January 2500", "format":"d M y || d M y"}}}
        ]
    }

   }})
   print("result is")
   for cases in res['hits']['hits']:
      print(cases['_source']['judge'])

   return "Yo"

@app.route('/query4',methods=['GET','POST'])
def query4():
   
   query = request.get_json()
   # print(query)
   
   searchString=query[0]['query']
   fromDate=query[0]['time']['from']
   toDate=query[0]['time']['to']
   cat=query[0]['cat']
   act=query[0]['act']
   judge=query[0]['judge']
   
   # print(type(keywordsList))
   # print(toDate)
   #  = 

   # searchString=searchString[:-1]
   res = es.search(index="cases",
   body={"query":{
   
    "bool": {
        "must": { "match":{"title":searchString}},
        "filter": [
           { "match":{"judge":judge}},
           { "match":{"act-used":act}},
           { "match":{"case-cat":cat}},
           { "range": {"date" : {"gte":"1 January 1900","lte":"1 January 2500", "format":"d M y || d M y"}}}
        ]
    }

   }})
   print("result is")
   for cases in res['hits']['hits']:
      print(cases['_source']['judge'])

   return "Yo"

if __name__ == '__main__':
   app.run(debug=True)
