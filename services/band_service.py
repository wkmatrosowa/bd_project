from sql_tables.band_table import BandTable
from web_forms.band_form import BandForm


class BandService:

    __table = BandTable()

    def save(self, data: BandForm, id: int = None):
        if id:
            self.__table.update()
        else:
            self.__table.insert(bandname=data.bandname.data,
                                yearoffoundation=data.yearoffoundation.data)
