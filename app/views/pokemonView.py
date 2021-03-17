import json

from flask import Blueprint, jsonify

from app.controllers.pokemonController import PokemonController
from app.models.pokemon import PokemonSchema

pokemon_view = Blueprint('pokemon_view', __name__)


@pokemon_view.route('/all')
def all():
    rows = PokemonController().get_all()
    print(rows[0].types)
    pokemon_schema = PokemonSchema(many=True)
    response = pokemon_schema.dump(rows)
    return jsonify({'pokemons': response})
