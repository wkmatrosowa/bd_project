from flask import Blueprint, render_template, redirect

from services.band_service import BandService
from web_forms.band_form import BandForm

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
        return redirect('/')
    return render_template('band.html', form=form)