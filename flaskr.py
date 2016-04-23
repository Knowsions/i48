# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~
    A microblog example application written as Flask tutorial with
    Flask and sqlite3.
    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_user
from contextlib import closing

# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='admin'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

# def init_db():
#     """Initializes the database."""
#     db = get_db()
#     with app.open_resource('schema.sql', mode='r') as f:
#         db.cursor().executescript(f.read())
#     db.commit()
    
def init_db():
    with closing(connect_db()) as db:
        # """Initializes the database."""
        # db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
    
# @app.cli.command('initdb')
# def initdb_command():
#     """Creates the database tables."""
#     init_db()
#     print('Initialized the database.')

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

#agregar estatus

def show():
    return render_template('show.html')

#agregar estatus
@app.route('/estatus')
def show_estatus():
    if current_user.is_authenticated():
        db = get_db()
        cur = db.execute('select id, descripcion from catalogo_estatus order by id desc')
        estatus = cur.fetchall()
        return render_template('show_estatus.html', estatus=estatus)
    else:
        return render_template("login.html")
    
#agregar vista polizas renovadas sin cobrar
@app.route('/')
def show_renovadas():
    if current_user.is_authenticated():
        db = get_db()
        cur = db.execute('select no_poliza,	case when fecha_vencimiento < date(date(\'now\'), \'+5 day\')\
                    then 1\
                    else 0 end as peligro, fecha_vencimiento,costo_renovacion,nombre_cliente,\
      telefono,correo,direccion,estatus from polizas order by fecha_vencimiento')
        renovadas = cur.fetchall()
        return render_template('show_renovadas.html', renovadas=renovadas)
    else:
        return render_template("login.html")

#update poliza
@app.route('/update', methods=['POST'])
def update():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('update polizas set estatus = 2 where id_poliza = ?',
                [request.form['id_poliza']])
    db.commit()
    flash('update')
    return redirect(url_for('show_renovadas'))


#agregar entrada blog
@app.route('/addestatus', methods=['POST'])
def add_estatus():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into catalogo_estatus (id, descripcion) values (?, ?)',
               [request.form['id'], request.form['descripcion']])
    db.commit()
    flash('Nuevo estatus agregado correctamente')
    return redirect(url_for('show_estatus'))

#Delete status selected
@app.route('/deleteestatus', methods=['POST'])
def delete_estatus():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('delete from catalogo_estatus where id = ?',
                [request.form['id']])
    db.commit()
    flash('borrado')
    return redirect(url_for('show_estatus'))


#login del usuario
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            #return redirect(url_for('show_estatus'))
            return redirect(url_for('show_renovadas'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_estatus'))

if __name__ == '__main__':
    # app.run()
    app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))