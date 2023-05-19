#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /: display "Hello HBNB!"
"""

from flask import Flask
app = Flask('web_flask')


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    """Return a simple HBNH message
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
