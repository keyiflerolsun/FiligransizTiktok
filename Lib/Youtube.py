# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pytube import YouTube
from time   import strftime, gmtime
from Kekik  import okunabilir_byte

def youtube_veri(_link:str):
    yt_data  = YouTube(_link)
    videolar = yt_data.streams.filter(progressive=True)

    return {
        "baslik"   : yt_data.title, 
        "yukleyen" : yt_data.author,
        "aciklama" : yt_data.description,
        "sure"     : strftime("%M:%S", gmtime(yt_data.length)),
        "izleyici" : yt_data.views,
        "tarih"    : yt_data.publish_date,
        "gorsel"   : yt_data.thumbnail_url,
        "videolar" : [
            {
                "video"  : video.url,
                "boyut"  : okunabilir_byte(video.filesize),
                "kalite" : video.resolution
            }
              for video in videolar
        ]
    }