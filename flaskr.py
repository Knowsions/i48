# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~
    Application written with Flask and sqlite3.
"""
import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
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
    if not session.get('logged_in'):
        return render_template('login.html')
    db = get_db()
    cur = db.execute('select id, descripcion from catalogo_estatus order by id desc')
    estatus = cur.fetchall()
    return render_template('show_estatus.html', estatus=estatus)
    
#agregar vista polizas renovadas sin cobrar
@app.route('/renovadas')
@app.route('/')
def show_renovadas():
    if not session.get('logged_in'):
        return render_template('login.html')
    db = get_db()
    #Solo polizas con estatus 1
    cur = db.execute('select id_poliza,  no_poliza,	case when fecha_vencimiento < date(date(\'now\'), \'+5 day\')\
                then 1\
                else 0 end as peligro, fecha_vencimiento,costo_renovacion,nombre_cliente,\
            telefono,correo,direccion,estatus from polizas where estatus = 1  order by fecha_vencimiento')
    renovadas = cur.fetchall()
    return render_template('show_renovadas.html', renovadas=renovadas)
    
#vista polizas notificadas
@app.route('/notificadas')
def show_notificadas():
    if not session.get('logged_in'):
        return render_template('login.html')
    #Cancelamos facturas ya vencidas
    #cancelarFacturas()
    db = get_db()
    #Solo polizas con estatus 2
    cur = db.execute('select id_poliza,  no_poliza,	case when fecha_vencimiento < date(date(\'now\'), \'+5 day\')\
                then 1\
                else 0 end as peligro, fecha_vencimiento,costo_renovacion,nombre_cliente,\
            telefono,correo,direccion,estatus from polizas where estatus = 2  order by fecha_vencimiento')
    notificadas = cur.fetchall()
    return render_template('show_notificadas.html', notificadas=notificadas)
    
#vista polizas pagadas
@app.route('/pagadas')
def show_pagadas():
    if not session.get('logged_in'):
        return render_template('login.html')
    db = get_db()
    #Solo polizas con estatus 3
    cur = db.execute('select id_poliza,  no_poliza,	case when fecha_vencimiento < date(date(\'now\'), \'+5 day\')\
                then 1\
                else 0 end as peligro, fecha_vencimiento,costo_renovacion,nombre_cliente,\
            telefono,correo,direccion,estatus from polizas where estatus = 3  order by fecha_vencimiento')
    pagadas = cur.fetchall()
    return render_template('show_pagadas.html', pagadas=pagadas)
    
#vista polizas canceladas
@app.route('/canceladas')
def show_canceladas():
    if not session.get('logged_in'):
        return render_template('login.html')
    db = get_db()
    #Solo polizas con estatus 3
    cur = db.execute('select id_poliza,  no_poliza,	case when fecha_vencimiento < date(date(\'now\'), \'+5 day\')\
                then 1\
                else 0 end as peligro, fecha_vencimiento,costo_renovacion,nombre_cliente,\
            telefono,correo,direccion,estatus from polizas where estatus = 4  order by fecha_vencimiento')
    canceladas = cur.fetchall()
    return render_template('show_canceladas.html', canceladas=canceladas)

#cancelamos las polizas que ya superan la fecha limite
def cancelarFacturas():
    db = get_db()
    #Cancelacion de facturas que superan su limite de vigencia
    cur = db.execute('update polizas set estatus = 4 where fecha_vencimiento < date(\'now\')')
    execute = cur.fetchall()
    

<<<<<<< HEAD
#update estatus poliza a estatus notificado
=======
@app.route('/historial')
def show_historial():
    if not session.get('logged_in'):
        return render_template('login.html')
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    fetched = db.execute('select detalle_siniestro, monto_pago, descuento, razon_descuento from historial  where id_poliza = 11111 order by fecha_hora')
    historial = fetched.fetchall()
    return render_template('show_historial.html', historial=historial)

#update poliza
>>>>>>> 0649003dea58f9abcbfba826fb79acc55d43f467
@app.route('/update', methods=['POST'])
def update():
    if not session.get('logged_in'):
        return render_template('login.html')
    db = get_db()
    db.execute('update polizas set estatus = 2 where id_poliza = ?',
               [request.form['id_poliza']])
    db.commit()
    flash('update')
    return redirect(url_for('show_renovadas'))
    
#update estatus poliza a estatus pagada
@app.route('/updatepagada', methods=['POST'])
def update_pagada():
    if not session.get('logged_in'):
        return render_template('login.html')
    db = get_db()
    db.execute('update polizas set estatus = 3 where id_poliza = ?',
               [request.form['id_poliza']])
    db.commit()
    flash('update')
    return redirect(url_for('show_notificadas'))



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