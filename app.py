from flask import Flask, render_template
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host='uts-database.cdkiiq0mub2o.ap-southeast-2.rds.amazonaws.com',
    user='admin',
    password='00000009', 
    database='uts_db'
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT id, nama_produk, harga, gambar_url FROM daftar_produk")
    produk = cursor.fetchall()
    return render_template("index.html", produk=produk)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
