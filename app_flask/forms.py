from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

class SimilarityForm(FlaskForm):
    text = TextAreaField("")
    submit = SubmitField("Send")