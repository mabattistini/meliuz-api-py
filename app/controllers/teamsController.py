from app.models.pokemon import PokemonModel
from app.models.teams import TeamsModel, TeamsPokemonsModel


class TeamsController(object):

    def get_all(self):
        records = TeamsModel.get_all()
        return records

    def get_by_id(self, id):
        return TeamsModel.find_by_id(id)

    def create(self, name, coach):
        team = TeamsModel(name=name, coach=coach)
        team.save_to_db()
        return team

    def update(self, id, name, coach):
        team = TeamsModel.find_by_id(id)
        team.name = name
        team.coach = coach
        team.update()
        return team

    def delete(self, id):
        team = TeamsModel.find_by_id(id)
        team.delete_from_db()
        return None


class TeamsPokemonController(object):

    def get_all(self, team=None):

        if not team:
            records = TeamsPokemonsModel.get_all()
        else:
            records = TeamsPokemonsModel.get_by_team(team_id=team)
        return records

    def get_by_id(self, id):
        return TeamsPokemonsModel.find_by_id(id)

    def create(self, team_id, pokemon_id):

        team = TeamsModel.find_by_id(team_id)
        if not team:
            raise Exception('Não existe um time com este id')

        pokemon = PokemonModel.find_by_id(pokemon_id)
        if not pokemon:
            raise Exception('Não existe um pokemon com este id')

        count = TeamsPokemonsModel.count_pokemons(team_id=team_id)
        if count >= 6:
            raise Exception('Número de pokemons excedido, máximo é 6')

        team_pokemon = TeamsPokemonsModel(team=team_id, pokemon=pokemon_id)
        team_pokemon.save_to_db()
        return team_pokemon

    def update(self, id, pokemon_id):

        team_pokemon = TeamsPokemonsModel.find_by_id(id)
        if not team_pokemon:
            raise Exception('Não existe um registro com este id')

        team_pokemon.pokemon_id = pokemon_id
        team_pokemon.update()
        return team_pokemon

    def delete(self, id):

        team_pokemon = TeamsPokemonsModel.find_by_id(id)
        if not team_pokemon:
            raise Exception('Não existe um registro com este id')

        team_pokemon.delete_from_db()
        return None
