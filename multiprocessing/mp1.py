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
def dwnl(kworker):
    fab='LIST'
    url_1=[]
    url_2=[]
    fr = open(fab, "r") #file read
    k=0
    for line in fr:
        k+=1
        if(k%2==0):
            url_1.append(line)
        else:
            url_2.append(line)    
    _i=len(url_1)
    _j=len(url_2)
    k=0
    n=0
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        if(kworker==1):
            for item1 in url_1: 
                k+=1
                if k <= _i:
                    _str_1="downloading "+str(item1)
                    print(_str_1)
                    os.system('notify-send '+_str_1)
                    ydl.download([item1])
        elif(kworker==2):
            for item2 in url_2:
                n+=1
                if n<=_j:
                    _str_2="downloading"+str(item2)
                    print(_str_2)
                    os.system('notify-send'+_str_2)
                    ydl.download([item2])
pool = mp.Pool(processes=2)
results = [pool.apply_async(dwnl, args=(x,)) for x in range(1,3)]
output = [p.get() for p in results]
print(output)


