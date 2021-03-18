from app.models.pokemon import PokemonModel


class PokemonController(object):

    def get_all(self):
        records = PokemonModel.get_all()
        return records

    def get_by_id(self, id):
        return PokemonModel.find_by_id(id)

    def get_by_names(self, name):
        return PokemonModel.get_by_names(name_list=name)
