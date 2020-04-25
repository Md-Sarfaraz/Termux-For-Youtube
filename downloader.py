#!/usr/bin/env python
from __future__ import unicode_literals
import youtube_dl

#youlink = input("Enter URL : ")
testlink = "https://www.youtube.com/watch?v=daefaLgNkw0"
pivatal = 'https://www.youtube.com/watch?v=f-H1aJJpm0U'


class MyLogger(object):
    def debug(self, msg):
        pass
        # print(msg)

    def info(self, msg):
        print(msg)

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        #file_tuple = os.path.split(os.path.abspath(d['filename']))
        #print("Done downloading {}".format(file_tuple[1]))
        pass
    if d['status'] == 'downloading':
        print(d['_percent_str'], d['_eta_str'], d['_speed_str'], str(
            d['downloaded_bytes'])+'/'+str(d['_total_bytes_str']))
        # print(d)


ydl_opts = {
    'quite': True,
    'logger': MyLogger(),
    'outtmlp': '%(title)s.%(ext)s',
    'progress_hooks': [my_hook]
}


def get_info():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            meta = ydl.extract_info(testlink, download=False)
        except KeyboardInterrupt:
            print("\rCtrl + C Detected\nQuiting...")
            exit(1)
    i = 1
    for key in meta.get('formats'):
        if str(key['ext']) != "webm":
            print(str(i) + " : "+key['format_id']+"  "+key['format_note'] +
                  " \t "+key['ext']+"\tformat")
            i += 1
    # print(meta['formats'][1])


def donwlaod(vidoeUrl):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            meta = ydl.extract_info(videoUrl, download=True)
        except KeyboardInterrupt:
            print("\rCtrl + C Detected\nQuiting...")
            exit(1)
    i = 1
    # for key in meta.get('formats'):
    #   print(str(i)+ " : "+key['format_note']+ " \t "+key['ext']+"\tformat")
    #   i+=1


# donwlaod()
get_info()
