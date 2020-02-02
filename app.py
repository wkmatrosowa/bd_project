from flask import Flask, render_template, redirect

from mysql_helper import mysql_helper
from routes.musician_routes import musician_urls
from services.band_service import BandService
from web_forms.band_form import BandForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.register_blueprint(musician_urls)

@app.route('/')
def index():
    links = [
        {
            'href': '/musicians',
            'name': 'Музыканты',
        },
        {
            'href': '/bands',
            'name': 'Группы',
        }
    ]
    return render_template('index.html', links=links)


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
