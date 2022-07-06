# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from VideoIndirici import app
from flask         import render_template

@app.route("/")
def index():
    return render_template("index.html", baslik="Video İndirici")