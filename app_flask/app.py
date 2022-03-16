from numpy import NaN
from flask import Flask, request, render_template
from gensim.models import KeyedVectors
import warnings
from forms import *
import os


warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim') # not sure it's useful there


app = Flask(__name__)

 # generate a secret key for the similarity form (html page test_similarity)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


# Let's load the Word Embeddings model trained with the .bin composed of tons of french words.
# Can't really explain how it's working for the moment. 
model = KeyedVectors.load_word2vec_format("../Data/model_leger.bin", binary=True, unicode_errors="ignore")
vocab_fr = load_vocab_fr() # We load the french dictionnary 
word_picked = pick_random_word(vocab_fr) # We generate the random french word
print(word_picked)
most_similar = model.most_similar(word_picked)[0][1]


##########################################################################################################
###################################### The model is heavy ################################################
################################## This is why the app makes #############################################
##################################### few seconds to start ###############################################
##########################################################################################################

# Generate global variables
id = 0
propositions = []


@app.route("/", methods=["GET", "POST"])
def similarity_score():
    form = SimilarityForm()

    # Initialize variables
    global propositions
    global id
    global word_picked
    global vocab_fr
    global most_similar
    # Populate the table
    table = Historique(propositions)

    if request.method == "POST":

        word1 = word_picked
        word2 = request.form["text"]
        print(word2)
        if word2 not in vocab_fr :
            return render_template('./error_word.html')
        elif word1 == word2 : 
            return render_template('./win.html')   
        else : 
            result = model.similarity(word1, word2)
            word_proposed = Proposition(id, word2, result)
            propositions.append(word_proposed)
            table = Historique(propositions)
            id+=1
        return render_template("/home.html", form=form, table=table, most = most_similar)
        
    else:
        return render_template("/home.html", form=form, table=table, most = most_similar)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
