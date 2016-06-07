from flask import abort, jsonify, make_response, redirect, request
from . import app, db_manager


@app.route('/urls/<id>', methods=['GET'])
def get_url(id):
    """
    Endpoint to add url
    :param id: the url code
    :return: 301, redirect to url found
             401, if url not found
    """
    url_found = db_manager.find_url(id)
    if not url_found:
        abort(404)
    return redirect(url_found, code=301)


@app.route('/users/<userid>/urls', methods=['POST'])
def add_url(userid):
    """
    Endpoint to add url
    Json passed by POST: ex. {"url": "http://www.google.com.br"}
    :param userid: name from owner
    :return: 201, json with the object created
                  ex. {
                        "id": "23094",
                        "hits": 0,
                        "url": "http://www.google.com.br",
                        "shortUrl": "http://<host>[:<port>]/asdfeiba"
                      }
    """
    url = request.json['url']
    obj_created = db_manager.add_url(userid, url, request.host)
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
