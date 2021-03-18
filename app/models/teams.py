from app.models import db


class TeamsModel(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(5), unique=True)
    coach = db.Column(db.String(255), nullable=False)

    def __init__(self, name, coach):
        self.name = name
        self.coach = coach

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


class TeamsPokemonsModel(db.Model):
    __tablename__ = 'teams_pokemons'

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemons.id'))
    team = db.relationship('TeamsModel', backref='teams_pokemons')
    pokemon = db.relationship('PokemonModel', backref='teams_pokemons')

    def __init__(self, team, pokemon):
        self.team_id = team
        self.pokemon_id = pokemon

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def get_by_team(cls, team_id):
        return cls.query.filter_by(team_id=team_id).all()

    @classmethod
    def count_pokemons(cls, team_id):
        rows = cls.query.filter_by(team_id=team_id).all()
        return len(rows)
