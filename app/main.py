from flask import Flask, jsonify
from __version__ import __version__

app = Flask(__name__)


@app.route('/version')
def hello():
    return jsonify(version=__version__)


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)