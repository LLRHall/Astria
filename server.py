from elasticsearch import Elasticsearch
from flask import Flask

es = Elasticsearch()
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"
@app.route('/query1')
def query1(keywords):
   return "wait"

if __name__ == '__main__':
   app.run(debug=True)
