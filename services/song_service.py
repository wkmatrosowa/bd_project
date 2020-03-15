from sql_tables.song_table import SongTable
from web_forms.song_form import SongForm


class SongService:
    __table = SongTable()

    def save(self, data: SongForm, id: int = None, id_album=None):
        if id:
            self.__table.update(songname=data.songname.data,
                                id=id)
        else:
            self.__table.insert(songname=data.songname.data,
                                id_album=id_album)

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
                    'songname': res[1],
                    'id_album': res[2],
                }
            )
        return result

    def delete(self, id):
        self.__table.delete(id)
