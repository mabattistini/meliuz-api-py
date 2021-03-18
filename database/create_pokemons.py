import json
import sqlite3
import sys


class SqliteDB(object):
    def __init__(self, database, json_file):
        print("populando database")
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        self.__load_tables(json_file)

    def __load_tables(self, json_filename):
        with open(json_filename, 'r') as jf:
            json_data = jf.read()
            json_data = json.loads(json_data)
            pokemons = json_data['pokemon']
            for pokemon in pokemons:
                try:
                    self.cursor.execute('INSERT INTO pokemons '
                                        '(id, name, height, weight, xp, image, types1) '
                                        'VALUES(?, ?, ?, ?, ?, ?, ?);',
                                        (pokemon['id'], pokemon['name'], pokemon['height'],
                                         pokemon['weight'], pokemon['xp'], pokemon['image'],
                                         ','.join(pokemon['types'])))

                    for type_pokemon in pokemon['types']:
                        self.cursor.execute('INSERT INTO types (pokemon_id, name) '
                                            'VALUES(?, ?);', (pokemon['id'], type_pokemon))

                    self.conn.commit()
                except sqlite3.IntegrityError as error:
                    if str(error).find('UNIQUE constraint failed') == 0:
                        self.conn.rollback()
                    else:
                        raise Exception((str(error)))

            return None


if __name__ == '__main__':
    args = sys.argv
    path = args[1]
    db = SqliteDB(database=path + '/Pokemon.db', json_file=path + '/Pokemons.json')
