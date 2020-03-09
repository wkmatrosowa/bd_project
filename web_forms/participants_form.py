from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


class ParticipantsForm(FlaskForm):
    musicians = SelectField('Музыканты', choices=[])
    submit = SubmitField('Добавить')