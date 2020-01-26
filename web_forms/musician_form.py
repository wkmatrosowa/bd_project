from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class MusicianForm(FlaskForm):
    firstname = StringField('Имя')
    surname = StringField('Фамилия')
    specialization = StringField('Специализация')
    submit = SubmitField('Сохранить')
