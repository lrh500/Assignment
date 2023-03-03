import sqlite3
import csv

conn = sqlite3.connect('movie_data.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = conn.cursor()

conn.execute('DROP TABLE IF EXISTS movies')
conn.execute('DROP TABLE IF EXISTS ratings')

conn.execute('CREATE TABLE movies (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT, genre TEXT)')
conn.execute('CREATE TABLE ratings (id INTEGER PRIMARY KEY AUTOINCREMENT, userid INTEGER UNIQUE, movieid INTEGER REFERENCES movies(id), rating INTEGER, timestamp TEXT)')


with open('csv/movies.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        id=int(row[0])
        name=row[1]
        genre=row[2]

        cur.execute('INSERT INTO movies VALUES (NULL,?,?)', (name, genre))
        conn.commit()

with open('csv/ratings.csv', newline='') as d:
    reader=csv.reader(d,delimiter=",")
    next(reader)
    for row in reader:
        print (row)
        
        userid=int(row[0])
        movieid=int(row[1])
        rating=float(row[2])
        timestamp=row[3]

        try:
            cur.execute('INSERT INTO ratings VALUES(NULL,?,?,?,?)',(userid,movieid,rating,timestamp))
            conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Skipping duplicate rating for user {userid} and movie {movieid}")

        #cur.execute('INSERT INTO ratings VALUES(?,?,?,?)',(userid,movieid,rating,timestamp))
        #conn.commit()

print("data parsed successfully");

conn.close()
