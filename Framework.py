import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

db_name = 'movie_data.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies')
def movies():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from customers
    cur.execute("select * from movies")
    rows = cur.fetchall()
    conn.close()
    return render_template('movies.html', rows=rows)


@app.route('/ratings')
def ratings():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from orders
    cur.execute("select * from ratings")
    rows = cur.fetchall()
    conn.close()
    return render_template('ratings.html', rows=rows)


@app.route('/ratings_details/<id>')
def ratings_details(id):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from ratings WHERE movieid=?", (id,))
    ratings = cur.fetchall()
    conn.close()

    if len(ratings) == 0:
        error_msg = f"This movie (id={id}) has not been rated by any user."
        return render_template('error.html', error=error_msg)

    return render_template('ratings_details.html', ratings=ratings)

