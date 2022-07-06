# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from VideoIndirici import app
from flask         import request, send_file
from requests      import get
from io            import BytesIO

@app.route('/indir')
def indir():
    _link = request.args.get('_link')
    _isim = request.args.get('_isim')

    istek = get(_link, allow_redirects=True)

    return send_file(BytesIO(istek.content), mimetype='video/mp4', as_attachment=True, download_name=f'{_isim}.mp4')