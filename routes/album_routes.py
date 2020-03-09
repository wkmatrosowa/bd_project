from flask import Blueprint, render_template

from services.album_service import AlbumService

album_urls = Blueprint("album", __name__)


@album_urls.route('/albums/<id_performer>/')
def albums(id_performer):
    albums = AlbumService().find(id_performer=id_performer)
    return render_template('albums.html', albums=albums)
