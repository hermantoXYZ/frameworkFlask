from flask import Flask, render_template

app = Flask(__name__)

app_name = "Aplikasi Python Flask Pertama saya sebagai mahasiswa BISDIG (Varibel Global)"
user = {
        "name": "Becce",
        "age": 20,
        "gender": "Laki-laki"
}
#1 App Route Hello Word!
@app.route("/")
def hello_world():
    return "<p>Hello, World! I am a Python Flask App, Apa Kabar..</p>"


#2 App Route Aplikasi ke halaman lebih spesifik
@app.route("/aplikasi/")
def aplikasi():
    return "<p>Aplikasi Python Flask Pertama saya sebagai mahasiswa BISDIG</p>"

#3 App Route ke halaman HTML yang kece
@app.route("/page/kece/")
def kece():
    return render_template("kece.html")


#4 App Route ke halaman HTML yang kece Part Full menghubungkan langsung ke static CSS
@app.route("/page/kece/full/")
def kece_name():
    return render_template("kece_part2.html")


#5 App Route Dinamis
@app.route("/page/kece/<string:nama>")
def get_name(nama):
    return f"nama anda adalah {user}".format(nama)


@app.route("/page/keces/")
def get_name2():
    return f"nama anda adalah {user}"


#6 App Route Variabel Global
@app.route("/global/")
def global_name():
    return f"Nama Aplikasi {app_name}"

#7 App Route Varibel Local
@app.route("/local/")
def local_name():
    user = {
        "name": "Becce",
        "age": 20,
        "gender": "Laki-laki"
    }
    return render_template("local.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)