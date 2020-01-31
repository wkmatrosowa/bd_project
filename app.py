from flask import Flask, render_template, redirect

from mysql_helper import mysql_helper
from services.band_service import BandService
from services.musician_service import MusicianService
from web_forms.band_form import BandForm
from web_forms.musician_form import MusicianForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/musicians')
def musicians():
    return 'musicians'

@app.route('/musician', methods=['GET', 'POST'])
def musician():
    form = MusicianForm()
    if form.validate_on_submit():
        MusicianService().save(form)
        return redirect('/')
    return render_template('musician.html', form=form)

@app.route('/bands')
def bands():
    return 'bands'

@app.route('/band', methods=['GET', 'POST'])
def band():
    form = BandForm()
    if form.validate_on_submit():
        BandService().save(form)
        return redirect('/')
    return render_template('band.html', form=form)


if __name__ == '__main__':
    app.run()
    print(mysql_helper)
