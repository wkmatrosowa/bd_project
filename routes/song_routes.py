from flask import Blueprint, render_template, redirect

from services.album_service import AlbumService
from services.band_service import BandService
from services.song_service import SongService
from web_forms.song_form import SongForm

song_urls = Blueprint("song", __name__)


@song_urls.route('/songs/<id_album>/', methods=['GET'])
def songs(id_album):
    album = AlbumService().find(id=id_album)
    if len(album) == 1:
        album = album[0]
    else:
        return 'Oops'

    band = BandService().find(id=album['id_performer'])
    if len(band) == 1:
        band = band[0]
    else:
        return 'Oops'
    songs = SongService().find(id_album=id_album)
    return render_template('songs.html',
                           songs=songs,
                           id_album=id_album,
                           name_album=album['albumname'],
                           id_performer=album['id_performer'],
                           name_performer=band['bandname']
                           )


@song_urls.route('/song/<id_album>/album', methods=['GET', 'POST'])
def song(id_album):
    album = AlbumService().find(id=id_album)
    if len(album) == 1:
        album = album[0]
    else:
        return 'Oops'
    form = SongForm()
    if form.validate_on_submit():
        SongService().save(data=form, id_album=id_album)
        return redirect('/songs/{}'.format(id_album))
    return render_template('song.html',
                           form=form,
                           id_album=id_album,
                           name_album=album['albumname']
                           )


@song_urls.route('/song/<id>/album/<id_album>', methods=['GET', 'POST'])
def song_id(id, id_album):
    song_for_html = SongService().find(id=id)
    if len(song_for_html) == 1:
        song_for_html = song_for_html[0]
    else:
        return 'Oops'
    form = SongForm()
    if form.validate_on_submit():
        SongService().save(data=form, id=id, id_album=id_album)
        return redirect('/songs/{}'.format(id_album))
    form.songname.data = song_for_html['songname']
    return render_template('song.html',
                           form=form,
                           id=id,
                           id_album=id_album,
                           name_album=song_for_html['albumname'])


@song_urls.route('/song/<id>/delete/<id_album>')
def song_delete(id, id_album):
    SongService().delete(id)
    return redirect('/songs/{}'.format(id_album))
