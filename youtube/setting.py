import urllib.request
# Settings File For Users


class Settings(object):

  
    # this the location of your internal storage. Don't Change it
    # if you change this, don't forget add a tailing slash at the end of the base_Path
    base_path = '/data/data/com.termux/files/home/storage/shared/'

    # Specify the Download Location for PCs.
    # if you change this, don't forget add a tailing slash at the end of the base_Path
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

def temp_thumbnail(stg):
    url = stg.thumbnail
    print(url)
    urllib.request.urlretrieve(url, stg.vid_id + '.jpg')
    print(stg.vid_id)
