from view import style as st
import setting
from notify import run_on_progress, run_on_finish
import subprocess as sub

toMb = 1048576  # devide to get size in Mb from Bytes
set = setting.Settings()

class Config:

    def my_hook(self, d):
        
        if d['status'] == 'finished':
            if set.is_Audio:
                print(
                    f"\n{st.green}Download Complete\nNow Converting to mp3 ...", end='')
            run_on_finish(d['filename'])

        if d['status'] == 'downloading':
            dsize = (
                f"{(d['downloaded_bytes'] / toMb):.2f}/{d['_total_bytes_str']}")
            percent = d['_percent_str']
            eta = d['_eta_str']
            speed = d['_speed_str']
            
            print(f"\r{percent}  {eta}  {speed}  {dsize}", end='')
            run_on_progress(d['_percent_str'], eta, speed, dsize)

        if d['status'] == 'error':
            print(d)

    def options(self, quality='best', audio=False):
        set.is_Audio = audio
        ydl_opts = {
            'quite': True,
            'logger': MyLogger(),
            'format': quality,
            'outtmpl': set.save_Path + "Video/%(title)s.%(ext)s",
            'progress_hooks': [self.my_hook],
            # 'socket_timeout': 5,
            'youtube_include_dash_manifest': False
        }
        aud_opts = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': "mp3",
            'outtmpl': set.save_Path + "Audio/%(title)s.%(ext)s",
            'noplaylist': True,
            'prefer_ffmpeg': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }],
            'postprocessor_args': [
                '-ar', '16000',
                '-ab', '256k'
            ]
        }

        return dict(ydl_opts, **aud_opts) if audio else ydl_opts


class MyLogger(object):
    def debug(self, msg):
        if 'already been downloaded' in msg:
            print("Media Already Downloaded")
        elif '[download] Downloading playlist: ' in msg:
            print(msg.replace('[download] Downloading p', 'P'), end='')
        elif '[download] Downloading video' in msg:
            print('\n'+msg.replace('[download] ', ''))

    def info(self, msg):
        print("info:: ", msg)

    def warning(self, msg):
        print("warn:: ", msg)

    def error(self, msg):
        print("error:: ", msg)

