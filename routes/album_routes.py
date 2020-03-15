from flask import Blueprint, render_template, redirect

from services.album_service import AlbumService
from services.band_service import BandService
from web_forms.album_form import AlbumForm

album_urls = Blueprint("album", __name__)


@album_urls.route('/albums/<id_performer>/', methods=['GET'])
def albums(id_performer):
    band = BandService().find(id=id_performer)
    if len(band) == 1:
        band = band[0]
    else:
        return 'Oops'
    albums = AlbumService().find(id_performer=id_performer)
    return render_template('albums.html', albums=albums, id_performer=id_performer, name_performer=band['bandname'])


@album_urls.route('/album/<id_performer>/performer', methods=['GET', 'POST'])
def album(id_performer):
    band = BandService().find(id=id_performer)
    if len(band) == 1:
        band = band[0]
    else:
        return 'Oops'
    form = AlbumForm()
    if form.validate_on_submit():
        AlbumService().save(data=form, id_performer=id_performer)
        return redirect('/albums/{}'.format(id_performer))
    return render_template('album.html', form=form, id_performer=id_performer, name_performer=band['bandname'])


@album_urls.route('/album/<id_album>/performer/<id_performer>', methods=['GET', 'POST'])
def album_id(id_album, id_performer):
    album_for_html = AlbumService().find(id=id_album)
    if len(album_for_html) == 1:
        album_for_html = album_for_html[0]
    else:
        return 'Oops'
    form = AlbumForm()
    if form.validate_on_submit():
        AlbumService().save(data=form, id=id_album, id_performer=id_performer)
        return redirect('/albums/{}'.format(id_performer))
    form.albumname.data = album_for_html['albumname']
    form.genre.data = album_for_html['genre']
    form.year.data = album_for_html['year']
    return render_template('album.html', form=form, id=id_album, id_performer=id_performer,
                           name_performer=album_for_html['bandname'])


@album_urls.route('/album/<id>/delete/<id_performer>')
def album_delete(id, id_performer):
    AlbumService().delete(id)
    return redirect('/albums/{}'.format(id_performer))
