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

    def find(self, **params):
        request = {}
        for key in self.__table.allowable_keys:
            if params.get(key):
                request[key] = params[key]
        sql_result = self.__table.find(request)
        result = []
        for res in sql_result:
            result.append(
                {
                    'id': res[0],
                    'bandname': res[1],
                    'yearoffoundation': res[2],
                }
            )
        return result