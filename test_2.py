from __future__ import unicode_literals 
import youtube_dl
ydl_opts = {}
_url_='https://www.youtube.com/watch?v=2YuLhvdg5xc' #provide the url 
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
  meta = ydl.extract_info( _url_, download=False) #download set to no i.e false
     print 'upload date : %s' %(meta['upload_date'])
     print 'uploader : %s' %(meta['uploader'])
     print 'views : %d' %(meta['view_count']) 
     print 'likes : %d' %(meta['like_count']) 
     print 'dislikes : %d' %(meta['dislike_count']) 
     print 'id : %s' %(meta['id'])
     print 'format : %s' %(meta['format'])
     print 'duration : %s' %(meta['duration'])
     print 'title : %s' %(meta['title'])
     print 'description : %s' %(meta['description']) 
 
