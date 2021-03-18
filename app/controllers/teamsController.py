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

    def get_all(self):
        records = TeamsPokemonsModel.get_all()
        return records

    def get_by_id(self, id):
        return TeamsPokemonsModel.find_by_id(id)
