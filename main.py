from flask import Flask, jsonify
from flask_cors import CORS
from threading import Thread

from route_get_random_quote import get_random_quote

app = Flask('')
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)


@app.route('/')
def home():
	return "Welcome to the random quote API."


@app.route('/random-quote', methods=['GET'])
def api_get_random_quote():
	return jsonify(get_random_quote())


def run():
	app.run(host='0.0.0.0', port=8080)


t = Thread(target=run)
t.start()