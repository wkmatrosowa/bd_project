from flask import Blueprint, render_template, redirect

from services.album_service import AlbumService
from web_forms.album_form import AlbumForm

album_urls = Blueprint("album", __name__)


@album_urls.route('/albums/<id_performer>/', methods=['GET'])
def albums(id_performer):
    albums = AlbumService().find(id_performer=id_performer)
    return render_template('albums.html', albums=albums, id_performer=id_performer)


@album_urls.route('/album/<id_performer>/performer', methods=['GET', 'POST'])
def album(id_performer):
    form = AlbumForm()
    if form.validate_on_submit():
        AlbumService().save(data=form, id_performer=id_performer)
        return redirect('/albums/{}'.format(id_performer))
    return render_template('album.html', form=form, id_performer=id_performer)
