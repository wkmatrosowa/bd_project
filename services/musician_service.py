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
            request[key] = params[key]
        return self.__table.find()