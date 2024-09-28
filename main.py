from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Konfigurasi database
db_config = {
    'host': 'localhost',
    'user': 'root',  # Ganti dengan username MySQL kamu
    'password': '',  # Ganti dengan password MySQL kamu
    'database': 'data'  # Nama database
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Koneksi ke database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Cek user dengan interpolasi string (rentan SQL Injection)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        return jsonify(status='success')
    else:
        return jsonify(status='error', message='Username atau password salah! Silakan isi kembali.')

@app.route('/welcome')
def welcome():
    # Redirect ke template welcome.html
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)
