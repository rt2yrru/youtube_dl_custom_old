from __future__ import unicode_literals
import os,json,youtube_dl

_faa='a'+'.json'
fo = open(_faa, "w")
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    _json=json.dumps(d)
    _faa='a'+'.json'
    fo = open(_faa, "w")
    fo.write(_json)
    fo.close() 

    if d['status'] == 'finished':
    	_msg='File downloaded '
        print(_msg)
        os.system('notify-send '+_msg) 
        #os.system('clear')
    else:
        #fo.write(d)
        os.system('clear')
        #_a_file=[]
        #_a_file[0].append(d['downloaded_bytes'])
        #_a_file[1].append(d['speed'])
        #_a__=str(d['downloaded_bytes']
        #_nm=d['eta']
        #print(d)
        print(_json)

        _str=str(d['_percent_str'])
        _strr=_str.replace("%", "")
        _float=float(_strr)
        if _float==80:
        	os.system('notify-send '+_str)
        	
        #os.system('notify-send '+_str)
        #os.system('pkill notify-osd')
#dictionary object
ydl_opts = {
    'format': 'best',
    'postprocessors': [],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

_url_='https://spankbang.com/1cqol/video/gdp+666'
#_url_=input("\n Enter the video url :")
#_i=len(_url_)
#list

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([_url_]) 
   
    
 
