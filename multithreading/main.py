from __future__ import unicode_literals
import os,json,sys,csv
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    import youtube_dl
import multiprocessing as mp
output = mp.Queue()
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
def my_hook(d):
    print(d)
ydl_opts ={
    'format': '720p_HD/720p/best',
    'postprocessors': [],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
def dwnl():
    fab='LIST'
    url_1=[]
    fr = open(fab, "r") #file read
    k=0
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for line in fr:
            k+=1
            _str_1="downloading "+str(line)
            print(_str_1)
            os.system('notify-send '+line)
            ydl.download([line])
pool = mp.Pool(processes=4)
results = [pool.apply_async(dwnl)]
output = [p.get() for p in results]
print(output)

