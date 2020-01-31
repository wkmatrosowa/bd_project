from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class BandForm(FlaskForm):
    bandname = StringField('Название группы')
    yearoffoundation = StringField('Год основания')
    submit = SubmitField('Сохранить')
