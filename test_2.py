#ydl3.py
from __future__ import unicode_literals 
import youtube_dl
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
  meta = ydl.extract_info( 'https://www.youtube.com/watch?v=9bZkp7q19f0', download=False) #download set to noi.e false
  print 'upload date : s' (meta['upload_date'])
  print 'uploader : s' (meta['uploader'])
  print 'views : d' (meta['view_count']) 
  print 'likes : d' (meta['like_count']) 
  print 'dislikes : d' (meta['dislike_count']) 
  print 'id : s' (meta['id'])
  print 'format : s' (meta['format'])
  print 'duration : s' (meta['duration'])
  print 'title : s' (meta['title'])
  print 'description : s' (meta['description']) 
