from sql_tables.band_table import BandTable
from web_forms.band_form import BandForm


class BandService:
    __table = BandTable()

    def save(self, data: BandForm, id: int = None):
        if id:
            self.__table.update(bandname=data.bandname.data,
                                yearoffoundation=data.yearoffoundation.data,
                                id=id)
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

    def get_participants(self, id):
        sql_result = self.__table.get_participants(id)
        result = []
        for res in sql_result:
            result.append(
                {
                    'id_musician': res[0],
                    'surname': res[1],
                    'firstname': res[2],
                    'specialization': res[3],
                }
            )
        return result

    def get_candidates(self, id):
        sql_result = self.__table.get_candidates(id)
        result = [(0, 'Не выбрано')]
        for res in sql_result:
            result.append((res[0], res[1] + ' ' + res[2] + ' ' + res[3]))
        return result

    def add_candidate(self, id_band: int = 0, id_musician: int = 0):
        if id_band == 0 or id_musician == 0:
            return
        self.__table.add_candidate(id_band, id_musician)

    def delete(self, id):
        self.__table.delete(id)
