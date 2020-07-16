from __future__ import unicode_literals
import youtube_dl
from youtube_dl.utils import YoutubeDLError
import threading
import setting
from view import style as st


stg = setting.Settings()


def donwlaod_with_param(url="", param={}, download=False,is_info=False):
    meta = {}
    with youtube_dl.YoutubeDL(param) as ydl:
        try:
            meta = ydl.extract_info(url, download=download)
            if is_info:
                stg.title = meta['title']
                stg.vid_id = meta['id']
                stg.thumbnail = meta['thumbnail']
                setting.temp_thumbnail(stg)
        except KeyboardInterrupt:
            print(f"\n{st.red}Ctrl + C Detected\nQuiting...{st.reset}")
            exit(0)
        except YoutubeDLError:
            print(f"\n{st.red}YoutubeDLError : Check URL or Network Connection{st.reset}")
            exit(1)
    return meta


def fetch_info(url,ydl_opt):
    argu = {
        'url' : url,
        'param' : ydl_opt,
        'is_info' : True
    }
    fin = threading.Thread(target=donwlaod_with_param, kwargs=argu)
    fin.start()
    fin.join()