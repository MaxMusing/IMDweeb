import os
import random
from flask import Flask, request, jsonify, send_from_directory
from App import getGenre

app = Flask(__name__, static_folder='client/build')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("client/build/" + path):
        return send_from_directory('client/build', path)
    else:
        return send_from_directory('client/build', 'index.html')


if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)


@app.route("/get-genre", methods=['POST'])
def getGenreAPI():
    storyline = request.json['storyline']
    genre = getGenre(storyline)

    return jsonify({"genre": genre})
