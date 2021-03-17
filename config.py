import os

DEBUG = True
PORT = 5000
HOST = "0.0.0.0"
SECRET_KEY = "o8-jEsz5fMEMY0hwIjwzfiuF0pYdvP0a0ckToSZuMtk="

DATABASE = os.path.dirname(__file__) + os.path.sep + 'database/Pokemon.db'

SQLALCHEMY_DATABASE_URI = 'sqlite:////' + DATABASE

print(SQLALCHEMY_DATABASE_URI)

