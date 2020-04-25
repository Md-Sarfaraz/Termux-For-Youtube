

ydl_opts = {
    'quite': True,
    'logger': MyLogger(),
    'outtmlp': '%(title)s.%(ext)s',
    'progress_hooks': [my_hook]
}


def my_hook(d):
    if d['status'] == 'finished':
        #file_tuple = os.path.split(os.path.abspath(d['filename']))
        #print("Done downloading {}".format(file_tuple[1]))
        pass
    if d['status'] == 'downloading':
        print(d['_percent_str'], d['_eta_str'], d['_speed_str'], str(d['downloaded_bytes'])+'/'+str(d['_total_bytes_str']))
        # print(d)


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

