from elasticsearch import Elasticsearch
from flask import Flask, request, jsonify, send_from_directory
import gensim

es = Elasticsearch("http://localhost:9200")
app = Flask(__name__)


def getRank(input_string):

    model = gensim.models.doc2vec.Doc2Vec.load("Model/NEW_D2V.model")
    similar_doc = model.docvecs.most_similar(
        positive=[model.infer_vector(input_string.split())], topn=10)
    return similar_doc


@app.route('/')
def root():
    return send_from_directory('frontend','main.html')


@app.route('/query1', methods=['GET', 'POST'])
def query1():

    query = request.get_json()
    # print(request.body)
    print(query)
    keywordsList = query[0]['query']
    fromDate = query[0]['time']['from']
    toDate = query[0]['time']['to']
    cat = query[0]['cat']
    act = query[0]['act']
    judge = query[0]['judge']

    if judge == "":
        judge = "*"
    if act == "":
        act = "*"
    if cat == "":
        cat = "*"

    searchString = ""
    for q in keywordsList:
        searchString += q+','

    searchString = searchString[:-1]
    res = es.search(index="cases",
                    body={"query": {

                        "bool": {
                            "must": {"multi_match": {"query": searchString, "fields": ["legal-key", "subject"]}},
                            "filter": [
                                {"range": {"date": {"gte": fromDate,
                                                    "lte": toDate, "format": "yyyyMMdd"}}},
                            ],
                            "should": [
                                {"wildcard": {"judge": {"value": judge}}},
                                {"wildcard": {"case-cat": {"value": cat}}},
                                {"wildcard": {"act-used": {"value": act}}},
                                {"wildcard": {"subject": {"value": cat}}},
                            ]
                        }

                    }})

    return jsonify(res['hits']['hits'])


@app.route('/query2', methods=['GET', 'POST'])
def query2():

    query = request.get_json()

    actquery = query[0]['query']
    fromDate = query[0]['time']['from']
    toDate = query[0]['time']['to']
    cat = query[0]['cat']
    act = query[0]['act']
    judge = query[0]['judge']

    if judge == "":
        judge = "*"
    if act == "":
        act = "*"
    if cat == "":
        cat = "*"

    res = es.search(index="acts",
                    body={"query": {
                        "bool": {
                            "must": {"match": {"Act_Name": actquery[0]}},
                        }
                    }})

    file_list = []
    for acts in res['hits']['hits']:
        temp = list(acts['_source']['File_Name'].replace(' ', '').split(','))
        for i in temp:
            if i != '\n':
                file_list.append(i)
    print(file_list)
    res = []
    for i in file_list:
        if i[-1] == '\n':
            temp = i[:-5]
        else:
            temp = i[:-4]

        res.append(es.search(index="cases",
                             body={"query": {
                                 "bool": {
                                     "must": {"match": {"filename": temp}},
                                     "filter": [
                                         {"range": {"date": {"gte": fromDate,
                                                             "lte": toDate, "format": "yyyyMMdd"}}},
                                     ],
                                     "should": [
                                         {"wildcard": {"judge": {"value": judge}}},
                                         {"wildcard": {"case-cat": {"value": cat}}},
                                         {"wildcard": {"act-used": {"value": act}}},
                                         {"wildcard": {"subject": {"value": cat}}},
                                     ]
                                 }
                             }}))

    resultReturn = []
    for result in res:
        resultReturn.append(result['hits']['hits'][0])

    return jsonify(resultReturn)


@app.route('/query3', methods=['GET', 'POST'])
def query3():

    query = request.get_json()

    searchString = query[0]['query']
    fromDate = query[0]['time']['from']
    toDate = query[0]['time']['to']
    cat = query[0]['cat']
    act = query[0]['act']
    judge = query[0]['judge']

    if judge == "":
        judge = "*"
    if act == "":
        act = "*"
    if cat == "":
        cat = "*"

    res = es.search(index="cases",
                    body={"query": {

                        "bool": {
                            "must": {"match": {"title": searchString[0]}},
                            "filter": [
                                {"range": {"date": {"gte": fromDate,
                                                    "lte": toDate, "format": "yyyyMMdd"}}},
                            ],
                            "should": [
                                {"wildcard": {"judge": {"value": judge}}},
                                {"wildcard": {"case-cat": {"value": cat}}},
                                {"wildcard": {"act-used": {"value": act}}},
                                {"wildcard": {"subject": {"value": cat}}},
                            ]
                        }

                    }})

    return jsonify(res['hits']['hits'])


@app.route('/query4', methods=['GET', 'POST'])
def query4():

    query = request.get_json()

    searchString = query[0]['query']
    fromDate = query[0]['time']['from']
    toDate = query[0]['time']['to']
    cat = query[0]['cat']
    act = query[0]['act']
    judge = query[0]['judge']

    tuple_list = getRank(searchString[0])
    file_list = [i[0] for i in tuple_list]

    res = []
    for i in file_list:
        if i[-1] == '\n':
            temp = i[:-5]
        else:
            temp = i[:-4]
        print(temp)
        res.append(es.search(index="cases",
                             body={"query": {
                                 "bool": {
                                     "must": {"match": {"filename": temp}},
                                     "filter": [
                                         {"range": {"date": {"gte": fromDate,
                                                             "lte": toDate, "format": "yyyyMMdd"}}},
                                     ],
                                     "should": [
                                         {"wildcard": {"judge": {"value": judge}}},
                                         {"wildcard": {"case-cat": {"value": cat}}},
                                         {"wildcard": {"act-used": {"value": act}}},
                                         {"wildcard": {"subject": {"value": cat}}},
                                     ]
                                 }
                             }}))

    resultReturn = []
    for result in res:
        resultReturn.append(result['hits']['hits'][0])

    return jsonify(resultReturn)


@app.route('/autocomplete', methods=['GET', 'POST'])
def autocomplete():
    query = request.get_json()

    searchString = query[0]['query']
    print(searchString)
    res = es.search(index="words",
                    body={"query": {
                        "bool": {
                            "must": {"match": {"data": searchString[0]}},
                        }

                    }})

    return jsonify(res['hits']['hits'])


if __name__ == '__main__':
    app.run(debug=True)
