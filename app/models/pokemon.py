from app.models import db
from app.models import ma


class PokemonModel(db.Model):
    __tablename__ = 'pokemons'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    xp = db.Column(db.Integer)
    image = db.Column(db.Text)
    types = db.Column(db.Text)

    def __init__(self, id, name, height, weight, xp, image):
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight
        self.xp = xp
        self.image = image

    def save_to_db(self):
        db.session.add(self)
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


class PokemonSchema(ma.Schema):
    class Meta:
        model = PokemonModel

        # Fields to expose
        fields = ("id", "name", "height", "weight", "xp", "image", "types")


class TypesModel(db.Model):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemons.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    pokemon = db.relationship('PokemonModel', backref='types')

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


class TypesShema(ma.Schema):
    class Meta:
        model = TypesModel
