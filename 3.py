from __future__ import unicode_literals
import os,json,youtube_dl
_a_=0
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
        elif _float==90:
            os.system('notify-send '+_str)  
        elif _float==99:
            os.system('notify-send '+_str) 
        else :
             _msg="a"   
        	
        #os.system('notify-send '+_str)
        #os.system('pkill notify-osd')
#dictionary object
ydl_opts ={
    'format': '720p/best',
    'postprocessors': [],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
_url_=[]
_t_a_=raw_input(" Enter the text file  : ")
_fab=str(_t_a_)
fr = open(_fab, "r") #file read
for line in fr:
    _url_.append(line)
_i=len(_url_)

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for item in _url_: 
        _a_+=1
        if _a_ <= _i:
            _str_="downloading "+str(_a_)+" of "+str(len(_url_))
            os.system('notify-send '+_str_)
            ydl.download([item]) 
            
        else :
            _str_=" error occured as counter exceed the length of list"   
            print(_str_)
            os.system('notify-send '+_str_)  


fr.close()  #file read is closed          
   
    
 
