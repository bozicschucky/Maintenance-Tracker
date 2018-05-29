#!flask/bin/python
from flask import Flask, abort, request, url_for
from flask.json import jsonify

app = Flask(__name__)



@app.route('/api/v1/request/<int:id>', methods=['GET'])
def get_user_request_by_id(id):
    pass

@app.route('/api/v1/requests', methods=['GET'])
def get_user_requests():
    pass


@app.route('/api/v1/request/<int:id>', methods=['POST'])
def create_user_request():
    pass

@app.route('/api/v1/request/<int:id>', methods=['PUT'])
def update_user_request(id):
    pass



if __name__ == '__main__':
    app.run(debug=True)