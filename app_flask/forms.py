import pandas as pd
import random
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

def load_vocab_fr():
    '''This function loads our french dictionnary and transforms it as a list'''
    words = pd.read_csv('../Data/liste_francais.txt', encoding = 'latin1', header = None)
    vocab = words.iloc[:,0].values.tolist()
    return vocab


def pick_random_word(mots_fr):
    '''This function picks randomly a word from our french dictionnary'''
    word_to_guess = random.choice(mots_fr)
    return word_to_guess


class SimilarityForm(FlaskForm):
    text = TextAreaField("")
    submit = SubmitField("Send")
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

class SimilarityForm(FlaskForm):
    text = TextAreaField("")
    submit = SubmitField("Send")
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

class SimilarityForm(FlaskForm):
    text = TextAreaField("")
    submit = SubmitField("Send")
