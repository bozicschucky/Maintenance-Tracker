#!flask/bin/python
from flask import Flask, abort, request, url_for
from flask.json import jsonify

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True)