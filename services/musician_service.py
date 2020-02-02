from sql_tables.musician_table import MusicianTable
from web_forms.musician_form import MusicianForm


class MusicianService:
    __table = MusicianTable()

    def save(self, data: MusicianForm, id: int = None):
        if id:
            self.__table.update()
        else:
            self.__table.insert(firstname=data.firstname.data,
                                surname=data.surname.data,
                                specialization=data.specialization.data)

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
                    'firstname': res[1],
                    'surname': res[2],
                    'specialization': res[3],
                }
            )
        return result
