
import subprocess as sub
import threading
import time
import setting
from downloader import stg

tmp = '/data/data/com.termux/files/home/bin/.tmp/'

def msg_on_progress(prog, eta, speed, size):
    
    cmd = [
        'termux-notification', 
        '-t', f'\u2193{prog}  |  {speed}  |  {eta}',
        '--id', stg.vid_id,
        '-c', stg.title,
        '--sound', '--vibrate', '800',
        '--priority', 'high',
        '--alert-once',
        '--image-path', tmp+stg.vid_id+'.jpg',
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
        '--image-path', tmp+stg.vid_id+'.jpg',
        '--action','termux-open "'+ path+'"'
    ]
    sub.run(cmd)
    setting.temp_thumbnail(stg,True)
   


def run_on_progress(perc,eta,speed,size):
    p = threading.Thread(target=msg_on_progress, args=(perc,eta,speed,size))
    p.start()
    p.join()


def run_on_finish(path):
    fin = threading.Thread(target=msg_on_finish, args=(path,))
    fin.start()
    fin.join()
