from flask import Flask, render_template

from routes.album_routes import album_urls
from routes.band_routes import band_urls
from routes.musician_routes import musician_urls
from routes.song_routes import song_urls

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.register_blueprint(musician_urls)
app.register_blueprint(band_urls)
app.register_blueprint(album_urls)
app.register_blueprint(song_urls)


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
        },
        {
            'href': '/stats',
            'name': 'Статистика',
        }
    ]
    return render_template('index.html', links=links)

if __name__ == '__main__':
    app.run()
