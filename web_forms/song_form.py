from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SongForm(FlaskForm):
    songname = StringField('Название песни')
    submit = SubmitField('Сохранить')