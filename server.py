import os
from flask import Flask, request, jsonify, send_from_directory
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


@app.route("/get-revenue", methods=['POST'])
def getRating():
    storyline = request.json['storyline']

    # sample calculation, ML processing goes here
    revenue = len(storyline.split())

    return jsonify({"revenue": revenue})
