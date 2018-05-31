import sqlite3
from flask import Flask, request,render_template
import json
import hashlib

app = Flask(__name__)
SQLITE_FILE = 'user_DB.sqlite'    # name of the sqlite database file

def createDB():
    # Connecting to the database file
    conn = sqlite3.connect(SQLITE_FILE)
    c = conn.cursor()
    # Creating a users credentials in SQLite table 
    c.execute('CREATE TABLE IF NOT EXISTS users (\
        username    text NOT NULL PRIMARY KEY,\
        name        text NOT NULL,\
        password    text    NOT NULL \
    );')
    conn.commit()
    try:
        c.execute('''INSERT INTO users( username, name, password) VALUES(?,?,?)''', ('mani', 'Manikandan','dff712e518cbf62c6993d8f79d42240f507d873e9dbe9b0239a887fcd3f711c4'))
        # Committing changes and closing the connection to the database file
        conn.commit()
    except:
        pass
    conn.close()

@app.route('/', methods=['GET','POST'])
def render_login():
    if request.method == 'POST':
        global SQLITE_FILE
        # Connecting to the database file
        conn = sqlite3.connect(SQLITE_FILE)
        c = conn.cursor() 
        username = request.form["username"]
        password = request.form["password"]
        c.execute('''SELECT username, name, password FROM users WHERE username = ?''',(username,))
        rows = c.fetchall()
        conn.commit()
        conn.close()
        if len(rows) == 0:
            return render_template("index.html",data="Username not found - Click on forgot username link to recover it")
        else:
            hex_password = hashlib.sha256(str.encode(password)).hexdigest()
            print(hex_password)
            if rows[0][2] == hex_password:
                return 'Hello '+ rows[0][1],200
            else:
                return render_template("index.html",data="Incorrect Password - Click on forgot password link to recover it")
    else:
        return render_template("index.html")

@app.route('/forgot_password', methods=['GET','POST'])
def forgot_password():
    return render_template("forgot_password.html")

@app.route('/forgot_username', methods=['GET','POST'])
def forgot_username():
    return render_template("forgot_username.html")

if __name__ == "__main__":
    createDB()
    app.run(debug = True)
