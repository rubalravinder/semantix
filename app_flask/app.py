from numpy import NaN
from flask import Flask, request, render_template
from gensim.models import KeyedVectors
import warnings
from forms import *
import os
import operator


warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim') # not sure it's useful there


app = Flask(__name__)

# generate a secret key for the similarity form (html page test_similarity)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


# Let's load the Word Embeddings model trained with the .bin composed of tons of french words.
# Can't really explain how it's working for the moment.

model = KeyedVectors.load_word2vec_format("../Data/model_leger.bin", binary=True, unicode_errors="ignore")
vocab_fr = load_vocab_fr(model) # We load the french dictionnary


# Generate global variables

word_picked = 'table' # We generate the random french word
print(word_picked)
list_of_word_picked = [word_picked]
longueur_mot = 0
most_similar = 0.65
id = 1
propositions = []


# HTML pages

@app.route("/", methods=["GET", "POST"])
def bouton():
    global word_picked
    global most_similar
    global list_of_word_picked
    global longueur_mot
    word_picked = pick_random_word(vocab_fr)
    list_of_word_picked.append(word_picked)
    longueur_mot = len(word_picked)
    most_similar = round(model.most_similar(word_picked)[0][1], 3)
    print(word_picked)
    print(most_similar)
    return render_template('./home.html')


@app.route("/win", methods=["GET", "POST"])
def win():
    return render_template('./win.html')


@app.route("/play", methods=["GET", "POST"])
def similarity_score():
    form = SimilarityForm()

    # Initialize variables
    global propositions
    global id
    global word_picked
    global vocab_fr
    global most_similar
    global list_of_word_picked
    global longueur_mot

    # Populate table
    table = Historique(propositions)

    if request.method == "POST":

        word1 = word_picked
        word2 = request.form["text"]
        if word2 not in vocab_fr :
            return render_template('./error_word.html')
        elif word1 == word2 :
            propositions.clear()
            id = 1
            return render_template('./win.html')   
        else : 
            result = round(model.similarity(word1, word2), 3)
            word_proposed = Proposition(id, word2, result)
            propositions.append(word_proposed)
            propositions_sorted =  sorted(propositions, key=operator.attrgetter('score'), reverse=True)
            table = Historique(propositions_sorted)
            id+=1
        return render_template("/play.html", form=form, table=table, most = most_similar, previous_word = list_of_word_picked[-2], longueur_mot = longueur_mot)
        
    else:
        return render_template("/play.html", form=form, table=table, most = most_similar, previous_word = list_of_word_picked[-2], longueur_mot = longueur_mot)




# Execute program

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
