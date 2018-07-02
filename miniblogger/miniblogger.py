from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
import sqlite3
import atexit
import os
import json

app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/entries', methods=['GET'])
def show_entries():
    db = get_db()
    cur = db.execute('select * from entries order by id desc')
    entries = cur.fetchall()
    data = []
    for row in entries:
            data.append([x for x in row])
    return jsonify(data)


@app.route('/add', methods=['POST'])
def add_entry():
    # if not session.get('logged_in'):
    #     abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
                 [request.json['title'], request.json['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))



# 

# port = int(os.getenv('PORT', 8000))

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=port, debug=True)
