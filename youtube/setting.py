import urllib.request
import subprocess as sub
import os
# Settings File For Users


class Settings(object):

    # this the location of your internal storage. Don't Change it
    # if you change this, don't forget add a tailing slash at the end of the base_Path
    base_path = '/data/data/com.termux/files/home/storage/shared/'

    # Specify the Download Location for PCs.
    # if you change this, don't forget add a tailing slash at the end of the base_Path,
    # and comment out the above 'base_path'
    #base_path = './../'

    # if you change this, don't forget add a tailing slash at the end of the save_Path
    save_Path = base_path+'Youtube/'


    # Don't change Below This
    # it will update while running of the programme.
    ###################################################

    is_Audio = False
    title = 'name'
    vid_id = 'video id'
    fullpath = 'for quick access'
    thumbnail = 'link'

def temp_thumbnail(stg,remove=False):
    tmp = '/data/data/com.termux/files/home/bin/.tmp/'

    if remove:
        test = os.listdir(tmp)
        for item in test:
            if item.endswith(".jpg"):
                os.remove(os.path.join(tmp, item))
        print('\nAll Clear')
    else:
        url = stg.thumbnail
        urllib.request.urlretrieve(url, tmp+stg.vid_id + '.jpg')

