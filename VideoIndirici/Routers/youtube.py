# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from VideoIndirici import app
from flask         import render_template, request, jsonify
from Lib.Youtube   import youtube_veri

@app.route("/youtube")
def youtube_index():
    return render_template("youtube.html", baslik="Youtube Video İndirici")

@app.route("/api/youtube_ver")
def youtube_ver():
    _link = request.args.get("_link")
    if not _link:
        return jsonify({"hata": "'_link' Verilmedi !"}), 403

    try:
        return youtube_veri(_link)
    except Exception as hata:
        return jsonify({"hata": f"{type(hata).__name__} | {hata}"}), 500