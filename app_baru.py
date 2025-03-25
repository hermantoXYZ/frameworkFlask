# App Baru
from flask import Flask, render_template

app = Flask(__name__)

app_name = "Aplikasi Python Flask Pertama saya sebagai mahasiswa BISDIG (Varibel Global)"
user = {
    "name": "Becce",
    "age": 20,
    "gender": "Laki-laki"
}


@app.route("/")
def hello_world():
    return "<p>Hello, World! I am a Python Flask App, Apa Kabar..</p>"