# Function to get the similarity from a given string
import gensim

def getRank(input_string):
    
    PATH = '/home/ubuntu/'
    file_name_to_index = list()
    with open(PATH+'index_to_csv.csv','r') as file:
        for item in file.readlines():
            file_name_to_index.append({item[0]:item[1]})
    model = gensim.models.doc2vec.Doc2Vec.load(PATH+"d2222v.model")
    similar_doc = model.docvecs.most_similar(positive=[model.infer_vector(input_string.split())],topn=5)
    file_rank = list()
    for items in similar_doc:
        file_rank.append((file_name_to_index[item[0]], item[1]))
    return file_rank