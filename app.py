from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'uts-database.cdkiiq0mub2o.ap-southeast-2.rds.amazonaws.com',
    'user': 'admin',
    'password': '00000009',
    'database': 'uts_db'
}

@app.route('/')
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM daftar_produk")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
