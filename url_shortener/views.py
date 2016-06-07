from flask import abort, jsonify, make_response, request
from . import app, db_manager


@app.route('/users', methods=['POST'])
def add_user():
    """
    Endpoint to add user
    Json passed by POST: ex. { "id": "jibao" }
    :return: 201, object created
             409, object already exist
    """
    userid = request.json['id']
    obj_created = db_manager.add_user(userid)
    if not obj_created:
        abort(409)
    return make_response(jsonify(obj_created), 201)