from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Konfigurasi database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="dbname"
)
cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    cursor.execute("INSERT INTO items (name) VALUES (%s)", (name,))
    db.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("DELETE FROM items WHERE id = %s", (id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)