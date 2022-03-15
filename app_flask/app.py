from numpy import NaN
from flask import Flask, request, render_template
from gensim.models import KeyedVectors
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim') # not sure it's useful there


app = Flask(__name__)

# Let's load the Word Embeddings model trained with the .bin composed of tons of french words.
# Can't really explain how it's working for the moment. 
model = KeyedVectors.load_word2vec_format("trained_model_french.bin", binary=True, unicode_errors="ignore")

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
    word1 = 'chien' # We'll have to fix word1 as a random french word
    word2 = request.values.get("mot")  # We get the users's word
    result = model.similarity(word1, word2) # The function which calculate similarities    
    return render_template('./similarity.html', resultat = result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
