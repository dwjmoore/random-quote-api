import sqlite3
import random


def get_quotes():
	con = sqlite3.connect('database.db')
	con.row_factory = sqlite3.Row
	cur = con.cursor()
	cur.execute("SELECT * FROM quotes")
	rows = cur.fetchall()

	quotes = []

	for i in rows:
		quote = {}
		quote['id'] = i['id']
		quote['quote'] = i['quote']
		quotes.append(quote)

	return quotes


def get_random_quote():
	quotes = get_quotes()
	random_quote = random.choice(quotes)
	return random_quote