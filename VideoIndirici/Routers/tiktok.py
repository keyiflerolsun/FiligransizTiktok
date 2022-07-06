# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from VideoIndirici import app
from flask         import render_template, request, jsonify
from Lib.Tiktok    import tiktok_veri

@app.route("/tiktok")
def tiktok_index():
    return render_template("tiktok.html", baslik="TikTok Video İndirici")

@app.route("/api/tiktok_ver")
def tiktok_ver():
    _id = request.args.get("_id")
    if not _id:
        return jsonify({"hata": "'_id' Verilmedi !"}), 403

    try:
        return tiktok_veri(_id)
    except Exception as hata:
        return jsonify({"hata": f"{type(hata).__name__} | {hata}"}), 500