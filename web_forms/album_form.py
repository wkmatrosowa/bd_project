from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


class AlbumForm(FlaskForm):
    albumname = StringField('Название альбома')
    year = StringField('Год')
    genre = SelectField('Жанр', choices=[
        ('Не выбрано', 'Не выбрано'),
        ('Рок', 'Рок'),
        ('Рэп', 'Рэп'),
        ('Хип-хоп', 'Хип-хоп'),
        ('Поп', 'Поп'),
        ('Электроника', 'Электроника')
    ])
    submit = SubmitField('Сохранить')