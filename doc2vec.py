# Function to get the similarity from a given string
import gensim

def getRank(input_string):
    

    model = gensim.models.doc2vec.Doc2Vec.load("NEW_D2V.model")
    similar_doc = model.docvecs.most_similar(positive=[model.infer_vector(input_string.split())],topn=5)
    return similar_doc