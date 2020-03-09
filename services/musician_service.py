from sql_tables.musician_table import MusicianTable
from sql_tables.performer_table import PerformerTable
from web_forms.musician_form import MusicianForm


class MusicianService:
    __table = MusicianTable()
    __performer_table = PerformerTable()

    def save(self, data: MusicianForm, id: int = None):
        if id:
            self.__table.update(firstname=data.firstname.data,
                                surname=data.surname.data,
                                specialization=data.specialization.data,
                                id=id)
        else:
            self.__table.insert(firstname=data.firstname.data,
                                surname=data.surname.data,
                                specialization=data.specialization.data)
            id = self.__table.inserted_id()
            self.__performer_table.insert(id_musician=id)

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

    def delete(self, id):
        self.__table.delete(id)
