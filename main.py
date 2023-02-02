from flask import Flask, jsonify
from flask_cors import CORS
from threading import Thread

app = Flask('')
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)


@app.route('/')
def home():
	return "Welcome to the random quote API."


def run():
	app.run(host='0.0.0.0', port=8080)


t = Thread(target=run)
t.start()
