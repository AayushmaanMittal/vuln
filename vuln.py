import sqlite3
from flask import Flask, request

app = Flask(__name__)
db = sqlite3.connect('users.db', check_same_thread=False)

@app.route('/user')
def user():
    q = "SELECT * FROM users WHERE id=" + request.args['id']
    return db.execute(q).fetchall()
