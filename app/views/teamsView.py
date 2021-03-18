import sqlite3

from flask import Blueprint, jsonify, request, json

from app.controllers.teamsController import TeamsController
from app.serializer.teamsSerializer import TeamsSerializer

teams_view = Blueprint('teams_view', __name__)


@teams_view.route('', methods=['GET'])
@teams_view.route('/', methods=['GET'])
def all():
    rows = TeamsController().get_all()
    response = TeamsSerializer(rows, many=True)
    return jsonify({'teams': response})


@teams_view.route('', methods=['POST', 'PUT', 'DELETE'])
def createTeam():
    campos = json.loads(request.data)
    response = {}

    try:
        name = campos['name']
        coach = campos['coach']
    except KeyError:
        return jsonify({'error': {'message': 'dados não informados'}}), 400

    if len(name) < 1 or len(name) > 5:
        return jsonify({'error': {'message': 'nome do grupo não deve exceder a 5 caracteres'}}), 400

    if request.method == 'POST':
        try:
            team = TeamsController().create(name=name, coach=coach)
            response = TeamsSerializer(team)
        except Exception as e:
            if str(e).find('UNIQUE constraint failed') > -1:
                return jsonify({'error': {'message': 'Já existe um time cadastrado com este nome'}}), 400
            else:
                return jsonify({'error': {'message': str(e)}}), 400
    elif request.method == 'PUT':
        id = request.args.get('id')
        if not id:
            return jsonify({'error': {'message': 'Informar o id do time'}}), 400
        team = TeamsController().update(id=id, name=name, coach=coach)
        response = TeamsSerializer(team)
    elif request.method == 'DELETE':
        id = request.args.get('id')
        if not id:
            return jsonify({'error': {'message': 'Informar o id do time'}}), 400
        TeamsController().delete(id=id)
        response = {'message': 'Time excluido com sucesso'}

    return jsonify({'teams': response}), 200
