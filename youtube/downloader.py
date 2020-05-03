from __future__ import unicode_literals
import youtube_dl
from youtube_dl.utils import YoutubeDLError


def donwlaod_with_param(url, param, download=False):
    meta = {}
    with youtube_dl.YoutubeDL(param) as ydl:
        try:
            meta = ydl.extract_info(url, download=download)
        except KeyboardInterrupt:
            print("\nCtrl + C Detected\nQuiting...")
            exit(0)
        except YoutubeDLError:
            print("\nYoutubeDLError : Check URL or Network Connection")
            exit(1)
    return meta

if __name__ == "__main__":
    pass
