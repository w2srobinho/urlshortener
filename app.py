#!env/bin/python

from url_shortener import app


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)