from elasticsearch import Elasticsearch
from flask import Flask, request, jsonify, send_from_directory, url_for, redirect, render_template
import gensim
import fnmatch
import pickle
from scipy import spatial
from bert_serving.client import BertClient
import numpy as np


bc = BertClient()
es = Elasticsearch("http://localhost:9200")
app = Flask(__name__)


@app.route('/')
def root():
    return send_from_directory('frontend', 'main.html')


@app.errorhandler(404)
def page_not_found(e):
    return send_from_directory("frontend", "error.html")


@app.route('/cases/<path:path>')
def casename(path):
    text = open("All_FT/"+path, 'r+')
    name = path[:-4]
    content = text.read()
    content = content.split('\n')
    index = content.index(fnmatch.filter(content, '1.*')[0])
    headings = content[:index]
    sections = content[index:]
    text.close()

    # return send_from_directory('All_FT', path)
    return render_template('cases.html', name=name, text=sections, headings=headings)


@app.route('/acts/<path:path>')
def actname(path):
    text = open("All_Acts/"+path, 'r+')
    name = path[:-4]
    content = text.read()
    text.close()
    content = content.split('\n')
    sections = []
    for x in content:
        sections.append(x.split('-->'))
    print(len(sections))
    return render_template('acts.html', name=name, text=sections)
    # return send_from_directory('All_Acts', path)


@app.route('/replacer.js')
def replacer():
    return send_from_directory("static", "replacer.js")


@app.route('/wallpaper1.png')
def wallpaper():
    return send_from_directory("static", "wallpaper1.png")


@app.route('/logo.png')
def logo():
    return send_from_directory("static", "logo.png")


@app.route('/query1', methods=['GET', 'POST'])
def query1():

    query = request.get_json()
    keywordsList = query[0]['query']
    fromDate = query[0]['time']['from']
    toDate = query[0]['time']['to']
    cat = query[0]['cat']
    act = query[0]['act']
    judge = query[0]['judge']

    if fromDate == "":
        fromDate = "18000101"
    if toDate == "":
        toDate = "20200101"
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
                            "must": {"multi_match": {"query": searchString, "fields": ["legal_key", "subject"]}},
                            "filter": [
                                {"range": {"date": {"gte": fromDate,
                                                    "lte": toDate, "format": "yyyyMMdd"}}},
                            ],
                            "should": [
                                {"match": {"judge": judge}},
                                {"match": {"case_cat": cat}},
                                {"match": {"act_used": act}},
                                {"match": {"subject": cat}},
                            ]
                        }

                    }})

    file_list = []
    for cases in res['hits']['hits']:
        temp = cases['_source']['filename']+'.txt'
        file_list.append(temp)

    acts = []
    for files in file_list:
        res1 = es.search(index="acts",
                         body={"query": {
                             "query_string": {
                                 "default_field": "File_Name",
                                 "query": files+" OR "+files+"\n",
                                 "default_operator": "AND"
                             }
                         }})
        temp = []
        for i in res1['hits']['hits']:
            temp.append(i['_source']['Act_Name'])

        acts.append(temp)

    qq = res['hits']['hits']+(acts)
    return jsonify(qq)


@app.route('/query2', methods=['GET', 'POST'])
def query2():

    query = request.get_json()
    actquery = query[0]['query']
    fromDate = query[0]['time']['from']
    toDate = query[0]['time']['to']
    cat = query[0]['cat']
    act = query[0]['act']
    judge = query[0]['judge']

    if fromDate == "":
        fromDate = "18000101"
    if toDate == "":
        toDate = "20200101"
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
                                         {"match": {"judge": judge}},
                                         {"match": {"case_cat": cat}},
                                         {"match": {"act_used": act}},
                                         {"match": {"subject": cat}},
                                     ]
                                 }
                             }}))

    resultReturn = []
    for result in res:
        try:
            resultReturn.append(result['hits']['hits'][0])
        except:
            pass

    acts = []
    for files in file_list:
        res1 = es.search(index="acts",
                         body={"query": {
                             "query_string": {
                                 "default_field": "File_Name",
                                 "query": files+" OR "+files+"\n",
                                 "default_operator": "AND"
                             }
                         }})
        temp = []
        for i in res1['hits']['hits']:
            temp.append(i['_source']['Act_Name'])

        acts.append(temp)

    qq = resultReturn+(acts)
    return jsonify(qq)


@app.route('/query3', methods=['GET', 'POST'])
def query3():

    query = request.get_json()

    searchString = query[0]['query']
    fromDate = query[0]['time']['from']
    toDate = query[0]['time']['to']
    cat = query[0]['cat']
    act = query[0]['act']
    judge = query[0]['judge']

    if fromDate == "":
        fromDate = "18000101"
    if toDate == "":
        toDate = "20200101"
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
                                {"match": {"judge": judge}},
                                {"match": {"case_cat": cat}},
                                {"match": {"act_used": act}},
                                {"match": {"subject": cat}},
                            ]
                        }

                    }})

    file_list = []
    for cases in res['hits']['hits']:
        temp = cases['_source']['filename']+'.txt'
        file_list.append(temp)

    acts = []
    for files in file_list:
        res1 = es.search(index="acts",
                         body={"query": {
                             "query_string": {
                                 "default_field": "File_Name",
                                 "query": files+" OR "+files+"\n",
                                 "default_operator": "AND"
                             }
                         }})
        temp = []
        for i in res1['hits']['hits']:
            temp.append(i['_source']['Act_Name'])

        acts.append(temp)

    qq = res['hits']['hits']+(acts)
    return jsonify(qq)


@app.route('/query4', methods=['GET', 'POST'])
def query4():

    query = request.get_json()

    searchString = query[0]['query']
    fromDate = query[0]['time']['from']
    toDate = query[0]['time']['to']
    cat = query[0]['cat']
    act = query[0]['act']
    judge = query[0]['judge']

    if fromDate == "":
        fromDate = "18000101"
    if toDate == "":
        toDate = "20200101"
    if judge == "":
        judge = "*"
    if act == "":
        act = "*"
    if cat == "":
        cat = "*"

    s = ""
    for x in searchString:
        s = s + x + " "
    a = bc.encode([s])

    arr = np.load("all_arr.npy")
    f = open("list.txt", 'rb')
    flist = pickle.load(f)
    similarity = np.zeros((arr.shape[0], 1), dtype=float)

    for x in range(arr.shape[0]):
        sim = 100-spatial.distance.cosine(arr[x], a)*100
        similarity[x] = sim

    sort_indices = np.argsort(similarity, axis=0)
    sort_indices = np.ravel(sort_indices[::-1][:10])
    sort_indices = sort_indices.tolist()
    file_list = [flist[x] for x in sort_indices]

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
                                         {"match": {"judge": judge}},
                                         {"match": {"case_cat": cat}},
                                         {"match": {"act_used": act}},
                                         {"match": {"subject": cat}},
                                     ],
                                 }
                             }}))

    resultReturn = []
    for result in res:
        try:
            resultReturn.append(result['hits']['hits'][0])
        except:
            pass

    acts = []
    for files in file_list:
        res1 = es.search(index="acts",
                         body={"query": {
                             "query_string": {
                                 "default_field": "File_Name",
                                 "query": files+" OR "+files+"\n",
                                 "default_operator": "AND"
                             }
                         }})
        temp = []
        for i in res1['hits']['hits']:
            temp.append(i['_source']['Act_Name'])

        acts.append(temp)

    qq = resultReturn+(acts)
    return jsonify(qq)


@app.route('/autocomplete', methods=['GET', 'POST'])
def autocomplete():
    query = request.get_json()

    searchString = query[0]['query']
    res = es.search(index="words",
                    body={"query": {
                        "bool": {
                            "must": {"match": {"data": searchString[0]}},
                        }

                    }})

    return jsonify(res['hits']['hits'][0]['_source']['data'])


if __name__ == '__main__':
    app.run(debug=True)
