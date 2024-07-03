from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from config import *

# Instancias 
app = Flask(__name__)
mysql = MySQL(app)

app.config.from_object('config') # importa todas las variables de configuración definidas en config.py a la aplicación Flask

@app.route('/')
def index():
    # Conexión con MySQL
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tareas')
    tareas = cur.fetchall()
    cur.close()
    return render_template('tareas/index.html', tareas=tareas)

# Nueva tarea
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        fecha_limite = request.form['fecha_limite']

        # Conexión con MySQL
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tareas (titulo, descripcion, fecha_limite) VALUES (%s, %s, %s)", (titulo, descripcion, fecha_limite))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))
    return render_template('tareas/create.html')


# Editar
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tareas WHERE id = %s", (id,))
    tarea = cur.fetchone()

    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        fecha_limite = request.form['fecha_limite']

        cur.execute("UPDATE tareas SET titulo=%s, descripcion=%s, fecha_limite=%s WHERE id=%s", (titulo, descripcion, fecha_limite, id))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))

    cur.close()
    return render_template('tareas/edit.html', tarea=tarea)


# Eliminar
@app.route('/delete/<int:id>')
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tareas WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True)


