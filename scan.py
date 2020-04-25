from downloader import donwlaod_with_param, MyLogger,my_hook


link ='https://www.youtube.com/watch?v=eMIxokGhFHM'

ydl_opts = {
    'quite': True,
    'logger': MyLogger(),
    'outtmlp': '%(title)s.%(ext)s',
    'progress_hooks': [my_hook]
}


donwlaod_with_param(link,ydl_opts)