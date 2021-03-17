from app.models.pokemon import PokemonModel


class PokemonController(object):

    def get_all(self):
        records = PokemonModel.get_all()
        #records = PokemonModel.find_by_id(1)
        return records
