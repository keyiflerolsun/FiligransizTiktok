# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from VideoIndirici import app
from flask         import make_response, jsonify, send_from_directory
from os            import path

@app.route("/favicon.ico", methods=["GET"])
def favicon():
    return send_from_directory(directory=path.join(app.root_path, "static"), filename="favicon.ico", mimetype="image/x-icon")

@app.errorhandler(404)
def dort_yuz_dort(error):
    return make_response(jsonify(hata="Sayfa Bulunamadı.."), 404)

@app.errorhandler(403)
def dort_yuz_uc(error):
    return make_response(jsonify(hata="Bu Sayfaya Erişim İzniniz Yoktur..!"), 403)

@app.errorhandler(410)
def dort_yuz_on(error):
    return make_response(jsonify(hata="Sayfa Taşınmış Olabilir.."), 410)

@app.errorhandler(500)
def bes_yuz(error):
    return make_response(jsonify(hata="Düzgün Argüman Verilmedi.. » (Sunucu Hatası Oluştu!)"), 500)