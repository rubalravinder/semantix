from numpy import NaN
from flask import Flask, request, render_template
from gensim.models import KeyedVectors
import warnings
from forms import *
#from forms import SimilarityForm
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


#####################################################################################################
############################ The model is heavy ################################################
######################## This is why the app makes ###################################################
########################### few seconds to start ########################################################
######################################################################################################


@app.route("/", methods=['GET', 'POST'])
def welcome():
    return render_template('./home.html')

@app.route("/similarity", methods=["GET", "POST"])
def similarity_route():
    most_similar = model.most_similar(word_picked)[0][1]
    word1 = word_picked # We'll have to fix word1 as a random french word
    print(word1)
    word2 = request.values.get("mot")  # We get the users's word
    if word2 not in vocab_fr : 
        return render_template('./error_word.html')
    else : 
        result = model.similarity(word1, word2) # The function which calculate similarities 
        if word1 == word2 : 
            return render_template('./win.html')   
        else : 
            return render_template('./similarity.html', resultat = (result*100), most = (most_similar * 100))



@app.route("/test_similarity", methods=["GET", "POST"])
def similarity_score():
    form = SimilarityForm()

    if request.method == "POST":
        word2 = request.form["text"]
        word1 = 'chien'

        result = model.similarity(word1, word2)
        # return render_template('./similarity.html', resultat = result)

        return f"""<h2>Your Word</h2> <p> {word2} </p> <h2>Your similarity score with {word1}: </h2> <p>{result}</p>"""
    
    else:
        return render_template("/test_similarity.html", form=form)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
