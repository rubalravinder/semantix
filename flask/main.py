from unittest import result
from numpy import NaN
from flask import Flask, request, render_template
import requests
from gensim.models import KeyedVectors
import warnings
from forms import *
import os
import operator
import spacy

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim') # not sure it's useful there

app = Flask(__name__)

# generate a secret key for the similarity form (html page test_similarity)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY



# Generate global variables

# model = KeyedVectors.load_word2vec_format("./Data/model_leger.bin", binary=True, unicode_errors="ignore")
# vocab_fr = load_vocab_fr(model) # We load the french dictionnary

word_picked = 'table' # We generate the random french word
print(word_picked)
list_of_word_picked = [word_picked]
longueur_mot = 0
most_similar = 0.65
id = 1
propositions_str = []
nlp = spacy.load("./fr_core_news_md-3.2.0/fr_core_news_md/fr_core_news_md-3.2.0")

headings = ('id', 'mot', 'score')
data = ()
sorted_data = ()
word_proposed = ()


# HTML pages

@app.route("/", methods=["GET", "POST"])
def bouton():
    global word_picked, most_similar, list_of_word_picked, longueur_mot, nlp, id, propositions_str, data

    # au cas où abandon
    data = list(data)
    data.clear()
    data = tuple(data)
    propositions_str.clear()
    id = 1

    # choix du mot à deviner
    # word_picked = pick_random_word(vocab_fr, nlp)
    print(word_picked)
    # word_picked = check_compatibility(word_picked, model, vocab_fr, nlp)
    print(word_picked)
    list_of_word_picked.append(word_picked)
    longueur_mot = len(word_picked)
    # most_similar = round(model.most_similar(word_picked)[0][1], 3)
    print(most_similar)
    return render_template('./home.html')


@app.route("/win", methods=["GET", "POST"])
def win():
    global id 
    return render_template('./win.html', id = id )

@app.route("/contact", methods=["GET", "POST"])
def contact():
    global id 
    return render_template('./mail.php', id = id )


@app.route("/play", methods=["GET", "POST"])
def similarity_score():
    form = SimilarityForm()

    # Initialize variables
    global id, word_picked, vocab_fr, most_similar, list_of_word_picked, longueur_mot, propositions_str, headings, data, sorted_data, word_proposed

    
    if request.method == "POST":

        word1 = word_picked
        word2 = request.form["text"]
           
        if word2 not in vocab_fr :
            return render_template("/play.html", form=form, most = most_similar, previous_word = list_of_word_picked[-2], longueur_mot = longueur_mot, erreur='Mot inexistant, essayez-en un autre', headings=headings, data=sorted_data)
        elif word1 == word2 :
            data = list(data)
            data.clear()
            data = tuple(data)
            propositions_str.clear()
            id = 1
            return render_template('./win.html')  
        else : 
            result = round(model.similarity(word1, word2), 3)
            word_proposed = (id, word2, result)

            if word2 not in propositions_str:
                data = list(data)
                data.append(word_proposed)
                propositions_str.append(word2)
                # propositions_sorted =  sorted(propositions, key=operator.attrgetter('score'), reverse=True)
                sorted_data = tuple(sorted(data, key=operator.itemgetter(2), reverse=True))
                data = tuple(data)
                id+=1
                

        return render_template("/play.html", form=form, most = most_similar, previous_word = list_of_word_picked[-2], longueur_mot = longueur_mot, headings=headings, data=sorted_data, word_proposed=word_proposed, id = id)
    
    else:
        return render_template("/play.html", form=form, most = most_similar, previous_word = list_of_word_picked[-2], longueur_mot = longueur_mot, headings=headings, data=sorted_data, word_proposed=word_proposed, id = id)


@app.route("/test", methods=["GET", "POST"])
def sim():
    form = SimilarityForm()

    # Initialize variables
    global id, word_picked, most_similar, list_of_word_picked, longueur_mot, propositions_str, headings, data, sorted_data, word_proposed#, vocab_fr

    
    if request.method == "POST":

        word1 = word_picked
        word2 = request.form["text"]
           
        # if word2 not in vocab_fr :
        #     return render_template("/play.html", form=form, most = most_similar, previous_word = list_of_word_picked[-2], longueur_mot = longueur_mot, erreur='Mot inexistant, essayez-en un autre', headings=headings, data=sorted_data)
        if word1 == word2 :
            data = list(data)
            data.clear()
            data = tuple(data)
            propositions_str.clear()
            id = 1
            return render_template('./win.html')  
        else : 
            requete = {"word":word2}
            url = 'http://127.0.0.1:5000/'
            res = requests.post(url, data=requete)
            result = res.text
            word_proposed = (id, word2, result)

            if word2 not in propositions_str:
                data = list(data)
                data.append(word_proposed)
                propositions_str.append(word2)
                # propositions_sorted =  sorted(propositions, key=operator.attrgetter('score'), reverse=True)
                sorted_data = tuple(sorted(data, key=operator.itemgetter(2), reverse=True))
                data = tuple(data)
                id+=1
                
        return render_template("/play.html", form=form, most = most_similar, previous_word = list_of_word_picked[-2], longueur_mot = longueur_mot, headings=headings, data=sorted_data, word_proposed=word_proposed, id = id)
    
    else:
        return render_template("/play.html", form=form, most = most_similar, previous_word = list_of_word_picked[-2], longueur_mot = longueur_mot, headings=headings, data=sorted_data, word_proposed=word_proposed, id = id)


#Execute program

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
