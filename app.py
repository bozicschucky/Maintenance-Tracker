from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'Code'
api = Api(app)
