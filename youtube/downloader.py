from __future__ import unicode_literals
import yt_dlp
from yt_dlp.utils import YoutubeDLError
import threading
import setting
from view import style as st


stg = setting.Settings()


def donwlaod_with_param(url="", param={}, download=False,is_info=False):
    meta = {}
     with yt_dlp.YoutubeDL(param) as ydl:
        try:
            meta = ydl.extract_info(url, download=download)
            if is_info:
                stg.title = meta['title']
                stg.vid_id = meta['id']
                stg.thumbnail = meta['thumbnail']
                setting.temp_thumbnail(stg)
        except KeyboardInterrupt:
            print(f"\n{st.red}Ctrl + C Detected\nQuiting...{st.reset}")
            setting.temp_thumbnail(stg)
            exit(0)
        except YoutubeDLError:
            print(f"\n{st.red}YoutubeDLError : Check URL or Network Connection{st.reset}")
            setting.temp_thumbnail(stg)
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
