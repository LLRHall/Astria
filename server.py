from elasticsearch import Elasticsearch
from flask import Flask

es = Elasticsearch("http://localhost:9200")
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"
@app.route('/query1')
def query1():
   res = es.search(index="cases",body={"query":{"match":{"legal-key":"Rubber, Credit Note"}}})
   
   for cases in res['hits']['hits']:
      print(cases['_source']['title'])

   return 'OK'

if __name__ == '__main__':
   app.run(debug=True)
