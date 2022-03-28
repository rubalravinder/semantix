from flask import Flask, request
from gensim.models import KeyedVectors
import os


app = Flask(__name__)

# generate a secret key for the similarity form (html page test_similarity)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


# Generate global variables
model = KeyedVectors.load_word2vec_format("./model_leger.bin", binary=True, unicode_errors="ignore")


# HTML page
@app.route("/", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        word1='table'
        word = request.form.get('word')
        result = round(model.similarity(word1, word), 3)
        return str(result)
    else:
        return '''
                <form method="POST">
                    <div><label>Word: <input type="text" name="word"></label></div>
                    <input type="submit" value="Submit">
                </form>'''

#Execute program
if __name__ == "__main__":
    app.run(debug=True)