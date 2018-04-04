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
    url_3=[]
    url_4=[]
    fr = open(fab, "r") #file read
    k=0
    for line in fr:
        k+=1
        if(k%4==1):
            url_1.append(line)
        elif(k%4==2):
            url_2.append(line)  
        elif(k%4==3):
            url_3.append(line)
        elif(k%4==0):
            url_4.append(line)
        else :
            print('Error found')
    _i1=len(url_1)
    _i2=len(url_2)
    _i3=len(url_3)
    _i4=len(url_4)
    _j1=0
    _j2=0
    _j3=0
    _j4=0
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        if(kworker==1):
            for item1 in url_1: 
                _j1+=1
                if _j1 <= _i1:
                    _str_1="downloading "+str(item1)
                    print(_str_1)
                    os.system('notify-send '+_str_1)
                    ydl.download([item1])
        elif(kworker==2):
            for item2 in url_2:
                _j2+=1
                if _j2<=_i2:
                    _str_2="downloading"+str(item2)
                    print(_str_2)
                    os.system('notify-send'+_str_2)
                    ydl.download([item2])
        elif(kworker==3):
            for item3 in url_3:
                _j3+=1
                if _j3<=_i3:
                    _str_3="downloading"+str(item3)
                    print(_str_3)
                    os.system('notify-send'+_str_3)
                    ydl.download([item3])
        elif(kworker==4):
            for item4 in url_4:
                _j4+=1
                if _j4<=_i4:
                    _str_4="downloading"+str(item4)
                    print(_str_4)
                    os.system('notify-send'+_str_4)
                    ydl.download([item4])
        else :
            print('Error')
pool = mp.Pool(processes=4)
results = [pool.apply_async(dwnl, args=(x,)) for x in range(1,5)]
output = [p.get() for p in results]
print(output)


