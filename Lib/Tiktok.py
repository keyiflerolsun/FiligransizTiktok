# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from requests import get
from time     import strftime, gmtime
from Kekik    import okunabilir_byte

def tiktok_veri(_id):
    istek = get(f"https://api.tiktokv.com/aweme/v1/multi/aweme/detail/?aweme_ids=%5B{_id}%5D")
    veri  = istek.json()["aweme_details"][0]
    return {
        "yukleyen" : veri["author"]["unique_id"],
        "aciklama" : veri["desc"],
        "sure"     : strftime("%M:%S", gmtime(veri["video"]["duration"]/1000)),
        "kalite"   : veri["video"]["ratio"],
        "boyut"    : okunabilir_byte(veri["video"]["play_addr"]["data_size"]),
        "gorsel"   : veri["video"]["origin_cover"]["url_list"][0],
        "video"    : veri["video"]["play_addr"]["url_list"][0],
    }