from numpy import NaN
from flask import Flask, request, render_template
from gensim.models import KeyedVectors
import warnings
from forms import *
import os
import operator
#import spacy


warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim') # not sure it's useful there


app = Flask(__name__)

# generate a secret key for the similarity form (html page test_similarity)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


# Let's load the Word Embeddings model trained with the .bin composed of tons of french words.

model = KeyedVectors.load_word2vec_format("./Data/model_pV1.bin", binary=True, unicode_errors="ignore")
vocab_fr = load_vocab_fr(model) # We load the french dictionnary
dico_fr = pd.read_csv('./Data/list_mots.txt', encoding = 'utf-8',sep ='\t',  header = None)
dico_fr = dico_fr.iloc[:,0].values.tolist()

# Generate global variables

def index():
    """returns the actual id"""
    for id in range(1000):
        yield id
        id += 1


# choix du mot à deviner
word_picked = pick_random_word(vocab_fr)
print(word_picked)
list_of_word_picked = [""]
list_of_word_picked.append(word_picked)
longueur_mot = len(word_picked)
most_similar = round(model.most_similar(word_picked)[0][1], 3)
print(most_similar)


###################################################################################################################################################################
################################################    APP      ######################################################################################################
###################################################################################################################################################################

@app.route("/", methods=["GET", "POST"])
def bouton():
    # global word_picked, most_similar, list_of_word_picked, longueur_mot, id, propositions_str, data

    # # au cas où abandon
    # data = list(data)
    # data.clear()
    # data = tuple(data)
    # propositions_str.clear()
    # id = 1
    return render_template('./home.html')


@app.route("/win", methods=["GET", "POST"])
def win():
    return render_template('./win.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template('./contact.html')

@app.route("/home", methods=["GET", "POST"])
def retour_home():
    return render_template('./home.html')


@app.route("/play", methods=["GET", "POST"])
def similarity_score():
    form = SimilarityForm()

    # Initialize variables

    propositions_str = []

    headings = ('id', 'mot', 'score')
    data = ()
    sorted_data = ()
    word_proposed = ()


    # def index():
    #     """returns the actual id"""
    #     for id in range(1000):
    #         yield id
    #         id += 1

    # increment_id = index()
    # id = next(increment_id)

    global word_picked, dico_fr, most_similar, list_of_word_picked, longueur_mot

    
    if request.method == "POST":

        word1 = word_picked
        word2 = request.form["text"]
           
        if word2 not in dico_fr :
            return render_template("/play.html", form=form, most = most_similar, previous_word = list_of_word_picked[-2], longueur_mot = longueur_mot, erreur='Mot inexistant, essayez-en un autre', headings=headings, data=sorted_data)
        elif word1 == word2 :
            data = list(data)
            data.clear()
            data = tuple(data)
            propositions_str.clear()
            return render_template('./win.html')  
        else : 
            result = round(model.similarity(word1, word2), 3)
            word_proposed = (id, word2, result)

            if word2 not in propositions_str:
                data = list(data)
                data.append(word_proposed)
                propositions_str.append(word2)
                sorted_data = tuple(sorted(data, key=operator.itemgetter(2), reverse=True))
                data = tuple(data)
                

        return render_template("/play.html", form=form, most = most_similar, previous_word = list_of_word_picked[-2], longueur_mot = longueur_mot, headings=headings, data=sorted_data, word_proposed=word_proposed, id = id)
    
    else:
        return render_template("/play.html", form=form, most = most_similar, previous_word = list_of_word_picked[-2], longueur_mot = longueur_mot, headings=headings, data=sorted_data, word_proposed=word_proposed, id = id)


#Execute program

# if __name__ == "__main__":
    # app.run()
    # app.run(host='0.0.0.0,  debug = True)
