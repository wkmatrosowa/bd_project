from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


class MusicianForm(FlaskForm):
    firstname = StringField('Имя')
    surname = StringField('Фамилия')
    specialization = SelectField('Специализация', choices=[
        ('Не выбрано', 'Не выбрано'),
        ('Вокалист', 'Вокалист'),
        ('Басист', 'Басист'),
        ('Солист-гитарист', 'Солист-гитарист'),
        ('Ударник', 'Ударник'),
        ('Барабанщик', 'Барабанщик'),
        ('Пианист', 'Пианист'),
    ])
    submit = SubmitField('Сохранить')
