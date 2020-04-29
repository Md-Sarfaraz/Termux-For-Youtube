from downloader import donwlaod_with_param
from util import Config
import subprocess as sub
from view import style as st, user_view


import os
os.system('')

link = sys.argv[1]


def main():
    global ydl_opt
    cf = Config()
    user_view()
    uin = input(f"{st.yellow}Option : {st.green}")
    print(f"{st.cyan}Download Starting ...{st.yellow}")
    opt = select_option(int(uin))
    if uin == '1':
        ydl_opt = cf.options(opt, True)
    elif uin == '2':
        ydl_opt = cf.options(opt)
    else:
        ydl_opt = cf.options(opt)
    info = donwlaod_with_param(link, ydl_opt, True)
    print('\n' + info['title'])
    print(st.dcol, st.reset)
    notify(info['title'])


def notify(name):
    cmd = [
        'termux-notification',
        '-t', 'Download Complete',
        '-c', name,
        '--sound', '--vibrate', '800',
        '--priority', 'high'
    ]
    sub.run(cmd)


def select_option(opt):
    select_dict = {
        1: '140',
        2: 'best',
        3: 'best[height<=240]',
        4: 'best[height<=360]',
        5: 'best[height<=480]',
        6: 'best[height<=720]',
        7: 'best[height<=1150]',
        8: 'best[height<=1440]',
        9: 'best[height<=2160]',
        0: 0,
    }
    return select_dict.get(opt, -1)


if __name__ == "__main__":
    try:
        if 'youtu.be' in link or 'youtube.com' in link:
            main()
        else:
            print(f'{st.red} Wrong Youtube URL')
            from time import sleep
            sleep(5)
            exit(0)
    except KeyboardInterrupt:
        print(f"{st.red}\tInterruted By User\n\tQuiting ...")
        print(st.reset)
        exit(0)
