from sql_tables.album_table import AlbumTable
from web_forms.album_form import AlbumForm


class AlbumService:
    __table = AlbumTable()

    def save(self, data: AlbumForm, id: int = None):
        if id:
            self.__table.update(albumname=data.albumname.data,
                                year=data.year.data,
                                genre=data.genre.data,
                                id_performer=data.performer.data,
                                id=id)
        else:
            self.__table.insert(albumname=data.albumname.data,
                                year=data.year.data,
                                genre=data.genre.data,
                                id_performer=data.performer.data)



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
                    'albumname': res[1],
                    'year': res[2],
                    'genre': res[3],
                    'id_performer': res[4],
                }
            )
        return result

    def delete(self, id):
        self.__table.delete(id)
