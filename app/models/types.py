from app.models import db


class TypesModel(db.Model):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemons.id'), nullable=False)
    name = db.Column(db.String, 255, nullable=False)
    #pokemon = db.relationship('PokemonModel', backref=db.backref('pokemons', lazy=True))
    pokemon = db.relationship('PokemonModel')

    def __init__(self, pokemon, name):
        self.pokemon_id = pokemon
        self.name = name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
