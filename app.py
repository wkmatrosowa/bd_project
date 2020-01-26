from flask import Flask, render_template, redirect

from mysql_helper import mysql_helper
from web_forms.musician_form import MusicianForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/musicians')
def hello_world():
    return 'musicians'

@app.route('/musician', methods=['GET', 'POST'])
def musician():
    form = MusicianForm()
    if form.validate_on_submit():
        print(form.firstname.data)
        return redirect('/')
    return render_template('musician.html', form=form)


if __name__ == '__main__':
    app.run()
    print(mysql_helper)
