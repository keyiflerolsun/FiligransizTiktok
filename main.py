# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI            import konsol
from CLI.HataYakala import cikis_yap, hata_yakala

from VideoIndirici  import app
from os             import environ

port = int(environ.get("PORT", 5000))
host = "0.0.0.0"

if __name__ == '__main__':
    try:
        # app.run(debug=True, host=host, port=port)

        konsol.print(f'\nFlaskTaban [bold red]{host}[yellow]:[/]{port}[/]\'de başlatılmıştır...\n', style="bold cyan", width=70, justify="center")

        from waitress import serve
        serve(app, host=host, port=port)
        # serve(app, host=host, port=port, url_scheme='https')
    except Exception as hata:
        hata_yakala(hata)