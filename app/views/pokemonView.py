from flask import Blueprint, jsonify, request

from app.controllers.pokemonController import PokemonController
from app.controllers.typesControllers import TypesController
from app.serializer.pokenonSerializer import pokemon_serializer

pokemon_view = Blueprint('pokemon_view', __name__)


@pokemon_view.route('/all', methods=['GET'])
def all():
    rows = PokemonController().get_all()
    response = pokemon_serializer(rows, many=True)
    return jsonify({'pokemons': response})


@pokemon_view.route('/filter', methods=['GET'])
def filter():
    filter_type = request.args.get('type')
    filter_name = request.args.get('name')

    if filter_type:
        filter_type = filter_type.split(',')

    if filter_name:
        filter_name = filter_name.split(',')

    if filter_name and not filter_type:
        rows = PokemonController().get_by_names(name=filter_name)
    else:
        rows = TypesController().get_by_name(
            name_list=filter_name,
            type_list=filter_type
        )

    response = pokemon_serializer(rows, many=True)

    return jsonify({'pokemons': response})
