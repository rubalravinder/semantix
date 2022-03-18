import pandas as pd
import random
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators
from flask_table import Table, Col
# import unidecode

def load_vocab_fr(model_word):
    '''This function loads our french dictionnary and transforms it as a list'''
    words = pd.read_csv('../Data/liste_francais.txt', encoding = 'latin1', header = None)
    vocab = words.iloc[:,0].values.tolist()
    for word in vocab : 
        if model_word.has_index_for(word) == False :
            vocab.remove(word)
    return vocab


def pick_random_word(mots_fr):
    '''This function picks randomly a word from our french dictionnary''' 
    word_to_guess = random.choice(mots_fr)
    return word_to_guess



class SimilarityForm(FlaskForm):
    text = TextAreaField("Essayez un mot", [validators.InputRequired()])
    submit = SubmitField("Envoyer")

# Declare table
class Historique(Table):
    id = Col('id')
    mot = Col('mot')
    score = Col('score')

    # def sort_propositions(self, propositions):
    #     # sort all scores
    #     scores = [prop.get_score() for prop in propositions]
    #     scores_sorted = scores.sort()

    #     # classify propositions
    #     ###### A COMPLETER ######
    #     for score in scores_sorted:
    #         if score in 
        



# Get some objects
class Proposition(object):
    def __init__(self, id, mot, score):
        self.id = id
        self.mot = mot
        self.score = score

    # def get_score(self):
    #     return self.score

