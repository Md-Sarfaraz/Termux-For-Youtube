
import subprocess as sub
import threading
import time
from downloader import stg

#stg = setting.Settings()

def msg_on_progress(prog, eta, speed, size):
    cmd = [
        'termux-notification', 
        '-t', f'Progress \u2193{prog}  |  {speed}  |  {eta}',
        '--id', stg.vid_id,
        '-c', stg.title,
        '--sound', '--vibrate', '800',
        '--priority', 'high',
        '--alert-once',
       ]
    sub.run(cmd)


def msg_on_finish(path):
    sub.run(['termux-notification-remove',stg.vid_id])
    cmd = [
        'termux-notification', 
        '-t', 'Downloading Complete',
        '-c', stg.title,
        '--sound', '--vibrate', '800',
        '--priority', 'high',
        '--action','termux-open "'+ path+'"'
    ]
    sub.run(cmd)
    print(stg.title)
    print(path)


def run_on_progress(perc,eta,speed,size):
    p = threading.Thread(target=msg_on_progress, args=(perc,eta,speed,size))
    p.start()
    p.join()


def run_on_finish(path):
    fin = threading.Thread(target=msg_on_finish, args=(path,))
    fin.start()
    fin.join()