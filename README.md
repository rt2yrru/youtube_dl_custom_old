# Purpose

    Want to embed youtube-dl,this is some of the ways I do it 
    
#1.py

     - It starts to download the video mentioned in _url_,with ydl_opts as the parameter.
     -  It will create a json file a.json which gets re written every time,you can use it to create a custom logger and display it as realtime progress
    -  The json is also printed in the terminal and cleared every time,so that you can see the realtime progress</td>
    -  It will send a custom notification at 80 percent progress so that you can prepare the code, at 100 % or finished,a notification of 'file download ' will appear to notify you that the file has been downloaded </td>


#2.py

    - It provides with meta data of a video/audio 

		

#Next

      - Add a script which will start a new download as soon as the status reaches 95 %
      - This way the time taken to convert the video,start a new download can be avoided
      
      example
      
      _url_=['a','b','c']
      _process=0
      _len=len(_url_)
      
      It starts with _url_[0],_process=1,so as soon it reaches 95 %, _url_[1] is started,_process=2  as _url_[0] will soon finish,
      As soon as _url[0] completes that thread will end
      
      As soon as _url_[1] reaches 95 % the same things occurs and a process is again started which starts _url_[2],_process=3
      As soon as _url_[1] completes and this thread is stopped,
      
      As soon as _url_[2] reaches 95 %,the invoker will stop as _process+=1 will make it 4 and _len=3,so the entire process will      terminate as _url_[2] completes
      
      
      This is a form of looping,while loop to be exact,but has to handled


#BUILD

<table width="100%"   align="center"  class="table_border_both">
<tr class="heading_table_top">
<td>  rg3:youtube-dl </td>
<td> Build Status</td>
<td><img src="https://travis-ci.org/rg3/youtube-dl.svg?branch=master" alt="youtube-dl build status"></td>
</tr>
<tr>
<td> siddht1:youtube-dl (fork) </td>
<td> Build Status</td>
<td><img src="https://travis-ci.org/siddht1/youtube-dl.svg?branch=master" alt="youtube-dl build status"></td>
</tr>
</table> 


#Usage    

      -Make sure you have the source of youtube-dl,source:https://github.com/rg3/youtube-dl
      -Alternatively if you don`t have the source,but have a excutable copy as mentioned in https://github.com/rg3/youtube-dl/#installation   then simply copy the exectuable to your current folder,this will work for linux versions only,windows user will have to get the source.
      Example: 
                - sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
               -  sudo chmod a+rx /usr/local/bin/youtube-dl 
	       
	       These commands were the one you already did,then once run "sudo youtube-dl -U" to update to the latest
	       then get your current path,
	       perform these steps
	       
	       - cp /usr/local/bin/youtube-dl   /[your_current_path]
	       rename youtube-dl to youtube-dl.zip
	       -unzip youtube-dl.zip
	       
	       As soon as you unzip,naviagate to the folder which has youtube-dl,
	       
	       the directory will look like 
	       
	       ----list--of---youtube-dl----------
	       
	       youtube_dl [folder]
	       __main__.py  [main youtube-dl loader file]


               ---end--of---youtube-dl----
	       
	       In this folder copy 1.py and 2.py,as these will directly invoke  __main__.py 
	       then added any url inside _url_=[''] residing in 1.py or 2.py
	       
	       run "'python 1.py'"    or  "'python 2.py'"
	       If you run 1.py
	       
	       -you must have got a json file "a.json",these stores your current progress realtime.Usage: https://github.com/siddht3/table_json_creator
	       -you must have got a notification,when the download reached 80%,90%,99% and when completed
	       
	      - you can now modify the code however you want
	       
                	       
	       
      
