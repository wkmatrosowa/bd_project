from flask import Blueprint, render_template, redirect

from services.band_service import BandService
from web_forms.band_form import BandForm
from web_forms.participants_form import ParticipantsForm

band_urls = Blueprint("band", __name__)


@band_urls.route('/bands')
def bands():
    bands = BandService().find()
    return render_template('bands.html', bands=bands)


@band_urls.route('/band', methods=['GET', 'POST'])
def band():
    form = BandForm()
    if form.validate_on_submit():
        BandService().save(form)
        return redirect('/bands')
    return render_template('band.html', form=form)


@band_urls.route('/band/<id>', methods=['GET', 'POST'])
def band_id(id):
    band_for_html = BandService().find(id=id)
    if len(band_for_html) == 1:
        band_for_html = band_for_html[0]
    else:
        return 'Oops'
    form = BandForm()
    if form.validate_on_submit():
        BandService().save(form, id=id)
        return redirect('/bands')
    form.bandname.data = band_for_html['bandname']
    form.yearoffoundation.data = band_for_html['yearoffoundation']
    return render_template('band.html', form=form, id=id)


@band_urls.route('/band/<id>/participants', methods=['GET', 'POST'])
def participants(id):
    band_for_html = BandService().find(id=id)
    band_musicians = BandService().get_participants(id=id)
    if len(band_for_html) == 1:
        band_for_html = band_for_html[0]
    else:
        return 'Oops'
    form = ParticipantsForm()
    if form.data['submit']:
        redirect_url = '/band/{}/participants'.format(id)
        BandService().add_participant(id_band=id, id_musician=form.musicians.data)
        return redirect(redirect_url)

    band_candidates = BandService().get_candidates(id=id)
    form.musicians.choices = band_candidates
    return render_template('participants.html', name=band_for_html['bandname'], band_musicians=band_musicians,
                           form=form, id=id)


@band_urls.route('/band/<id_band>/participant/<id_musician>', methods=['GET'])
def participant_delete(id_band, id_musician):
    BandService().delete_participant(id_band, id_musician)
    return redirect('/band/{}/participants'.format(id_band))
