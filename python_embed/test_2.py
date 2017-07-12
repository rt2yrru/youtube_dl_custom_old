from __future__ import unicode_literals 
import os,json,sys
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    import youtube_dl
ydl_opts = {}
_url_='https://www.youtube.com/watch?v=2YuLhvdg5xc' #provide the url 
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
  meta = ydl.extract_info( _url_, download=False) #download set to no i.e false
  _json=json.dumps(meta)
  print(_json)
    
 
