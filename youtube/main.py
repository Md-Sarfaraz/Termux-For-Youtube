from downloader import donwlaod_with_param, fetch_info
from util import Config
from setting import Settings as setting
from view import style as st, user_view
import sys
import os
os.system('clear')

link = sys.argv[1]

def main():

    user_view()
    vid_option = select_option()
    ydl_opt = get_params(vid_option)
    print(f"{st.cyan}Download Starting ...{st.yellow}")
    
    fetch_info(link,ydl_opt)
    meta = donwlaod_with_param(link, ydl_opt, True)
    print('\n' + meta['title'])
    print(st.dcol, st.reset)


def get_params(val):
    return Config().options(val, True) if val == '140' else Config().options(val)


def select_option(view=False):

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

    if view:
        os.system('clear')
        user_view()

    uin = input(f"{st.yellow}Option : {st.green}")
    try:
        if uin == '':
            print('Selecting Best Quality by Default')
            return 'best'
        opt = int(uin)
        if not 0 <= opt < 9:
            return select_option(True)
        else:
            return select_dict.get(opt)
    except ValueError:
        return select_option(True)



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
