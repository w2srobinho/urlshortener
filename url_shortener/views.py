from flask import abort, jsonify, make_response, redirect, request
from . import app, db_manager


@app.route('/urls/<id>', methods=['GET'])
def get_url(id):
    """
    Endpoint to add url
    :param id: the url code
    :return: 301, redirect to url found or
             401, if url not found
    """
    url_found = db_manager.find_url(id)
    if not url_found:
        abort(404)
    return redirect(url_found, code=301)


@app.route('/users/<user_id>/urls', methods=['POST'])
def add_url(user_id):
    """
    Endpoint to add url
    Json passed by POST: ex. {"url": "http://www.google.com.br"}
    :param user_id: name from owner
    :return: 201, json with the object created
                  ex. {
                        "id": "23094",
                        "hits": 0,
                        "url": "http://www.google.com.br",
                        "shortUrl": "http://<host>[:<port>]/asdfeiba"
                      }
    """
    url = request.json['url']
    obj_created = db_manager.add_url(user_id, url, request.host)
    if not obj_created:
        abort(404)
    return make_response(jsonify(obj_created), 201)


@app.route('/stats', methods=['GET'])
def global_stats():
    """
    Endpoint to generate global statistics url
    :return: 200, json with the global stats
                 ex. {
                        "hits": 193841,     // Total of hits of all urls from the system
                        "urlCount": 2512,   // Total of registered urls on system
                        "topUrls": [ // Top 10 Urls most accessed
                            // Stat object by id, ordered by hits desc
                            {
                                "id": "23094",
                                "hits": 153,
                                "url": "http://www.google.com.br",
                                "shortUrl": "http://<host>[:<port>]/asdfeiba"
                            },
                            {
                                "id": "23090",
                                "hits": 89,
                                "url": "http://www.uol.com.br",
                                "shortUrl": "http://<host>[:<port>]/asdxiba"
                            },
                            // ...
                        ]
                    }
    """
    stats = db_manager.generate_global_statistics(request.host)
    return make_response(jsonify(stats), 200)


@app.route('/users/<user_id>/stats', methods=['GET'])
def user_stats(user_id):
    """
    Endpoint to generate user statistics url
    :param user_id: name from owner
    :return: 404, user not found  or
             200, json with the user stats
                 ex. {
                        "hits": 193841,     // Total of hits of all urls from the system
                        "urlCount": 2512,   // Total of registered urls on system
                        "topUrls": [ // Top 10 Urls most accessed
                            // Stat object by id, ordered by hits desc
                            {
                                "id": "23094",
                                "hits": 153,
                                "url": "http://www.google.com.br",
                                "shortUrl": "http://<host>[:<port>]/asdfeiba"
                            },
                            {
                                "id": "23090",
                                "hits": 89,
                                "url": "http://www.uol.com.br",
                                "shortUrl": "http://<host>[:<port>]/asdxiba"
                            },
                            // ...
                        ]
                    }
    """
    stats = db_manager.generate_user_statistics(user_id, request.host)
    if not stats:
        abort(404)
    return make_response(jsonify(stats), 200)


@app.route('/stats/<id>', methods=['GET'])
def url_stats(id):
    """
    Endpoint to generate url statistics
    :param user_id: encoded id from url
    :return: 404, user not found  or
             200, json with the user stats
                 ex. {
                        "id": "23094",
                        "hits": 0,
                        "url": "http://www.google.com.br",
                        "shortUrl": "http://<host>[:<port>]/asdfeiba"
                    }
    """
    stats = db_manager.generate_url_statistics(id, request.host)
    if not stats:
        abort(404)
    return make_response(jsonify(stats), 200)


@app.route('/urls/<id>', methods=['DELETE'])
def remove_url(id):
    """
    Endpoint to remove url
    :param id: encoded id from url
    """
    status = db_manager.remove_url(id)
    if not status:
        abort(404)
    return ''

@app.route('/users', methods=['POST'])
def add_user():
    """
    Endpoint to add user
    Json passed by POST: ex. { "id": "jibao" }
    :return: 201, object created or
             409, object already exist
    """
    user_id = request.json['id']
    obj_created = db_manager.add_user(user_id)
    if not obj_created:
        abort(409)
    return make_response(jsonify(obj_created), 201)
