from gensim.models import KeyedVectors

def load_model():
    model = KeyedVectors.load_word2vec_format("./model_leger.bin", binary=True, unicode_errors="ignore")    
    return model

if __name__ == '__main__':
    load_model()