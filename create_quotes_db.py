import sqlite3


def create_quotes_db():
	con = sqlite3.connect('database.db')
	print("Opened database successfully")
	cur = con.cursor()

	cur.execute("DROP TABLE quotes")

	cur.execute("""
        CREATE TABLE quotes (
            id	INTEGER	PRIMARY KEY	NOT NULL,
            quote	TEXT	NOT NULL
        );
    """)

	print("Created table.")
	con.close()


def insert_quotes(quotes):
	con = sqlite3.connect('database.db')
	cur = con.cursor()

	for i in range(len(quotes)):
		cur.execute("INSERT INTO quotes (quote) VALUES (?)", [quotes[i]])
	con.commit()
	print("Text added")
	con.close


create_quotes_db()

quotes = []

with open("quotes.txt") as f:
	for line in f:
		quotes.append(line.strip())
f.close()

insert_quotes(quotes)