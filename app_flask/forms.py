import pandas as pd
import random
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators
from flask_table import Table, Col
import spacy
import fr_core_news_md
# import unidecode

def load_vocab_fr(model_word):
    '''This function loads our french dictionnary and transforms it as a list'''
    words = pd.read_csv('../Data/liste_francais.txt', encoding = 'latin1', header = None)
    vocab = words.iloc[:,0].values.tolist()
    for word in vocab : 
        if model_word.has_index_for(word) == False :
            vocab.remove(word)
    return vocab


def pick_random_word(mots_fr, model_nlp):
    '''This function picks randomly a word from our french dictionnary''' 
    
    word_to_guess = random.choice(mots_fr)
    word_to_guess = model_nlp(word_to_guess)
    word_picked = word_to_guess[0].lemma_ 
    return word_picked

def check_compatibility(word_picked_bla, model, mots_fr, model_nlp): 
    while model.has_index_for(word_picked_bla) == False :
        word_picked_bla = pick_random_word(mots_fr, model_nlp)
    else : 
        word_picked = word_picked_bla
        return word_picked


class SimilarityForm(FlaskForm):
    text = StringField("Essayez un mot", [validators.InputRequired()])
    submit = SubmitField("Envoyer")

# Declare table
class Historique(Table):
    id = Col('id')
    mot = Col('mot')
    score = Col('score')

# Get some objects
class Proposition(object):
    def __init__(self, id, mot, score):
        self.id = id
        self.mot = mot
        self.score = score


