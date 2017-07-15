#Purpose

 
<table width="100%"   align="center"  class="table_border_both">
<tr class="heading_table_top">
<td> Want to embed youtube-dl,this is some of the ways I do it.</td>
</tr>
<td>  Extend youtube-dl basic functions in python to be more flexible </td>
</tr>
<tr>
<td> Call youtube-dl or youtube_dl_embed via java </td>
</tr>
<tr>
<td> Call youtube-dl or youtube_dl_embed via c,c++ </td>
</tr>
<tr>
<td>  Call youtube-dl or youtube_dl_embed via PHP </td>
</tr>
</table>   
    
#MEMBERS

<table width="100%"   align="center"  class="table_border_both">
<tr class="heading_table_top">
<td> siddht 4/1/3 </td>
<td> project maintainer,developer </td>
<td> FULL ACCESS</td>
</tr>
<tr>
<td> yan12125 </td>
<td> youtube-dl -> project collaborator </td>
<td> FULL ACCESS </td>
</tr>
<tr>

</tr>
</table> 


#BUILD

<table width="100%"   align="center"  class="table_border_both">
<tr class="heading_table_top">
<td>  rg3:youtube-dl </td>
<td> TRAVIS CI </td>
<td> Build Status</td>
<td><img src="https://travis-ci.org/rg3/youtube-dl.svg?branch=master" alt="youtube-dl build status"></td>
</tr>
<tr>
<td> siddht1:youtube-dl (fork) </td>
<td> TRAVIS CI </td>
<td> Build Status</td>
<td><img src="https://travis-ci.org/siddht1/youtube-dl.svg?branch=master" alt="youtube-dl build status"></td>
</tr>
<tr>
<td> youtube-dl-embed project </td>
<td> TRAVIS CI </td>
<td> Build Status</td>
<td><img src="https://travis-ci.org/siddht4/youtube_dl_embed.svg?branch=master" alt="youtube-dl-embedd build status"></td>
</tr>
<td> youtube-dl-embed project </td>
<td> Coverity Scan  </td>
<td> Coverity Scan Status</td>
<td><a href="https://scan.coverity.com/projects/siddht4-youtube_dl_embed">
  <img alt="Coverity Scan Build Status"
       src="https://scan.coverity.com/projects/13144/badge.svg"/>
</a>
</td>
</tr>
<tr>
<td> youtube-dl-embed project </td>
<td>  dependencies</td>
<td> Dependencies Status</td>
<td><img src="https://img.shields.io/david/expressjs/express.svg" alt="youtube-dl-embed dependencies"></td>

</tr>
<tr>
<td> youtube-dl-embed project </td>
<td>  License</td>
<td> UNLICENSE</td>
<td><img src="https://img.shields.io/badge/license-UNLICENSE-green.svg" alt="youtube-dl-embed UNLICENSE LICENSE"></td>

</tr>


</table> 


#Thanks


<table width="100%"   align="center"  class="table_border_both">
<tr class="heading_table_top">
<td>  @yan12125 </td>
<td> Thanks  aka Yen Chi Hsuan (youtube-dl contributor/maintainer) for your help to extend this utility </td>

</tr>
<td> @iriberri </td>
<td> Thanks  aka Carla Iriberri (Travis Builder) for helping me fixing the builds for TRAVIS CI </td>

</tr>
<tr>

</tr>
</table>      

 #VERSION

 <table width="100%"   align="center"  class="table_border_both">
<tr class="heading_table_top">
<td> youtube-dl </td>
<td> 2017.07.15</td>

</tr>
<td> in youttube-dl [folder] </td>
<td> in __main__.py  [python file] </td>

</tr>
<tr>

</tr>
</table>        

#TRAVIS CI

 <table width="100%"   align="center"  class="table_border_both">
<tr class="heading_table_top">
<td> Built against</td>


</tr>
<td> python</td>


</tr>
<tr>
<td>  </td>
</tr>
</table>   
    
# 1.py (https://github.com/siddht4/youtube_dl_embed/blob/master/python_embed/1.py)


     - It starts to download the video mentioned in _url_,with ydl_opts as the parameter.
     -  It will create a json file a.json which gets re written every time,you can use it
     to create a custom logger and display it as realtime progress
    -  The json is also printed in the terminal and cleared every time,so that you can see 
    the realtime progress
    -  It will send a custom notification at 80 percent progress so that you can prepare the 
    code,at 100 % or finished,a notification of 'file download ' will appear to notify you 
    that the file has been downloaded 
    
    
    How it works :-
     First run this file via terminal by typing "python 1.py"
     Based on _url_ (python type list) it will start download
     Code part :
     
     _url_=['']  # undeclared list ,you can add your own url
     #_url_.append('')  # append to list _url_ ,you can add more url to the existing list,remove #
      _len=len(_url_)
      
      For _url=[] ,this is a python type list , 

 (https://github.com/siddht4/youtube_dl_embed/blob/master/python_embed/1.py#L60)
 
      Here you can declare all your url 
      
      example : _url=['url1','url2']   and so one 
      
      
       #_url_.append('') is commented,so to also run it uncomment it. 
       Whatever you provide here will be appended to _url
       
       example : _url=['url1','url2']  
       _url.append('url3')
       
       will make _url=['url1','url2','url3']  
      

 
     At 80 %   code part :

 (https://github.com/siddht4/youtube_dl_embed/blob/master/python_embed/1.py#L39-L49)
     
       _str=str(d['_percent_str'])
        _strr=_str.replace("%", "")
        _float=float(_strr)
        if _float==80:
      os.system('notify-send '+_str)
      
      You will see the notification 80% 
      
      This will also appear for 90%,99% and 100 % or completed
     


# 2.py (https://github.com/siddht4/youtube_dl_embed/blob/master/python_embed/2.py)


    - It provides with meta data of a video/audio 
    
    
# 3.py  (https://github.com/siddht4/youtube_dl_embed/blob/master/python_embed/3.py)


      This is a mere upgradation of 1.py so that one can simply enter a text file which has 
      all the url.
      
      How this works :-
      
     First run this file via terminal by typing "python 3.py"
     
     : A message will appear  " Enter the text file  :  "
     : Enter the file name,be sure to also provide the file format.example: 1.txt 
     : From here everything is similar to what you see in 1.py
     
     
       This is quite similar to "youtube-dl -a  [text_file]"

		

#Next 1  aka 5.py

      - Add a script which will start a new download as soon as the status reaches 95 %
      - This way the time taken to convert the video,start a new download can be avoided
      
      example
      
      _url_=['a','b','c']
      _process=0
      _len=len(_url_)
      
      It starts with _url_[0],_process=1,so as soon it reaches 95 %, _url_[1] is started,
      _process=2  as _url_[0] will soon finish,
      As soon as _url[0] completes that thread will end
      
      As soon as _url_[1] reaches 95 % the same things occurs and a process is again started 
      which starts _url_[2],_process=3
      
      As soon as _url_[1] completes and this thread is stopped,
      
      As soon as _url_[2] reaches 95 %,the invoker will stop as _process+=1 will make it 4 and
      _len=3,so the entire process will      terminate as _url_[2] completes
      
      
      This is a form of looping,while loop to be exact,but has to handled
      
      
#NEXt 3 aka 4.py
       
       - Parallel downloading from two url.
       - Evenly divides url list into two lists
       
       Sample code :
       
     sample.py


#Usage    

      -Make sure you have the source of youtube-dl,source: 
  (https://github.com/rg3/youtube-dl)    
  
      -Alternatively if you don`t have the source,but have a excutable copy as mentioned in 
  (https://github.com/rg3/youtube-dl/#installation) 
    
           then simply copy the exectuable to your
        current folder,this will work for linux versions only,windows user will have to get the source.
        Example: 
                - sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
               -  sudo chmod a+rx /usr/local/bin/youtube-dl 
	       
	       These commands were the one you already did,then once run "sudo youtube-dl -U" to update to 
	       the latest then get your current path, perform these steps
	       
	       - cp /usr/local/bin/youtube-dl   /[your_current_path]
	       rename youtube-dl to youtube-dl.zip
	       -unzip youtube-dl.zip -d /[the_folder_you_want]
	       
	       As soon as you unzip,naviagate to the folder which has youtube-dl,



         or  with the new structure in place simply clone this repository 

         terminal command "git clone https://github.com/siddht4/youtube_dl_embed"
	       
	       the directory will look like 
	       
	       ----list--of---youtube-dl----------
	       
	       youtube_dl [folder]
	       __main__.py  [main youtube-dl loader file]
           youtube_dl_embed [folder]

               ---end--of---youtube-dl----
	       

	       
	        ,as these will directly invoke  __main__.py 
	        then added any url inside _url_=[''] residing in 1.py or 2.py
          to run 3.py just provide a file as you did for "youtube-dl -a [file_name]"
	       
	        then naviagte to youtube_dl_embed folder

          and in terminal type "python 1.py"
	       
	        -you must have got a json file "a.json",these stores your current progress realtime.
	         Usage: 
(https://github.com/siddht3/table_json_creator)
		 
	         -you must have got a notification,when the download reached 80%,90%,99% and when completed
	       
	          - you can now modify the code however you want


#USAGE - JAVA

       If you would instead try the java one,then you would be using
 (https://github.com/siddht4/youtube_dl_embed/blob/master/java/main.java)

         as a base.

         Requirments :- 

         - python to run youtube-dl,youtube_dl_embed

         - java to run main.java


         How to do :-

         - Make sure you have java installed 

         - copy /java/main.java  to where would you like

         - make necessary changes to (https://github.com/siddht4/youtube_dl_embed/blob/master/java/main.java#L11)

         - run in terminal "javac main.java", this would create main.class,which is a class file,your main.java is compiled

         - Now run "java main" to get the ouput from the compiled class file


         Structure  :-

         JAVA --> exec  ---> python ----> youtube-dl 

         youtube-dl -> python -> exec --> JAVA


#USAGE - C

          If you would instead try the C  one,then you would be using
 (https://github.com/siddht4/youtube_dl_embed/blob/master/c/1.c)

         as a base.

         Requirments :- 

         - python to run youtube-dl,youtube_dl_embed

         - c,I have used gcc,to test and built it


         How to do :-

         - Make sure you have c installed,if you are using linux make sure gcc is installed

         - copy /c/1.c  to where would you like

         - make necessary changes to (https://github.com/siddht4/youtube_dl_embed/blob/master/c/1.c)

         - open terminal type the command as follows "gcc 1.c",this will compile 1.cc and create a.out file

         - now in terminal type "./a.out [any_command]",for this once instead,try "./a.out youtube-dl -v"


          Structure :- 

          C  --> std [in]  ---> python ----> youtube-dl

          youtube-dl --> python --> std [out] -- > C



#USAGE - C++

          If you would instead try the C++  one,then you would be using
 (https://github.com/siddht4/youtube_dl_embed/blob/master/c++/link.cpp)

         as a base.

         Requirments :- 

         - python to run youtube-dl,youtube_dl_embed

         - c++,I have used g++,to test and built it


         How to do :-

         - Make sure you have c++ installed,if you are using linux make sure g++ is installed

         - copy /c++/link.cpp  to where would you like

         - copy (https://github.com/siddht4/youtube_dl_embed/blob/master/c%2B%2B/pstream.h),this the psteam.h
          file/header to execute stdin and stdout for C++,this file opens streams to outside packages

         - make necessary changes to (https://github.com/siddht4/youtube_dl_embed/blob/master/c%2B%2B/link.cpp)
           especially (https://github.com/siddht4/youtube_dl_embed/blob/master/c%2B%2B/link.cpp#L8)
           changes needed to be made in 'proc("ls", redi::pstreams::pstdout | redi::pstreams::pstderr)'
           to something like proc '("youtube-dl -v ", redi::pstreams::pstdout | redi::pstreams::pstderr)''
           so make necessary changes after 'proc("'' line only 

         - then open terminal type the command as follows "g++ link.cpp",this will compile link.cpp and create a.out file

         - now in terminal type "./a.out ", to see your ouput based on  '("youtube-dl -v ", redi::pstreams::pstdout | redi::pstreams::pstderr)''


          Structure :- 

          C++  --> pstream  ---> python ----> youtube-dl

          youtube-dl --> python --> pstream -- > C++



#USAGE - PHP

          If you would instead try the PHP  one,then you would be using
 (https://github.com/siddht4/youtube_dl_embed/blob/master/php/test.php)

         as a base.

         NOTE :-

         - I am currently final testing PHP one so that a 

         - form with video url is given which is posted using POST method,lets name it form.php

         - a php which will sanitize data received via POST i.e URL,this will call exec function 
           which will then execute youtube-dl,so meanwhile a table will be created which uses json
           sample at (https://github.com/siddht3/table_json_creator)
           which will show realtime log to user.

         - As soon as it reaches 100 % or completed user will be redirtected to the downloaded link   


         Requirments :- 

         - python to run youtube-dl,youtube_dl_embed
         
         - php 7.0 

         - nginx (PHP CGI) or Apache server .


         How to do :-

         - Make sure you have nginx,php installed and nginx configured to run PHP via FASTCGI

         - copy /php/test.php  to where would you like

         - For testing purpose I am calling (https://github.com/siddht4/youtube_dl_embed/blob/master/python_embed/2.py)
            as it provides me with the metadata
            You can repurpose it in anyway you would,especially $cmd 

            '<?php
             $cmd="python ../python_embed/test_2.py";
             $out=shell_exec($cmd);
             var_dump($out);
             ?> '



      


          Structure :- 

         PHP --> FAST CGI --> NGINX  --> PYTHON --> youtube-dl 

         youtube-dl --> PYTHON --> NGINX --> FAST CGI  --> PHP


	       
	       
	      
#Other-Works 


<table width="100%"   align="center"  class="table_border_both">
<tr class="heading_table_top">
<td> Project Name   </td>
<td> Purpose </td>
<td> Info </td>
</tr>
<tr>
<td>  youtube_dl_java (https://github.com/siddht1/youtube_dl_java_old)</td>
<td> using youtube-dl via java i.e youtube-dl-java -> jvm -> python -> youtube-dl </td>
<td>  This project has been merged and is  under sub directory java (https://github.com/siddht4/youtube_dl_embed/tree/master/java)	 </td>
<td> </td>
</tr>
<tr>
<td> () </td>
<td>   using youtube-dl via c and c++ </td>
<td> - currently testing their behaviour  </td>
<td> This project has been merged and is  under sub directory C and C++ likewise (https://github.com/siddht4/youtube_dl_embed/tree/master/c)	
(https://github.com/siddht4/youtube_dl_embed/tree/master/c++)</td>

</tr>

</table>  

	       
#UNLICENSE

(https://github.com/rg3/youtube-dl/blob/master/LICENSE)	 
          	  
<table width="100%"   align="center"  class="table_border_both">
<tr class="heading_table_top">
<td> As youtube-dl is under unlicense, So these mere utilily as an extension is also provided as same as it also directly follows
	  youtube-dl as base</td>
</tr>
<tr>
</tr>

</table>  	  



#CHANGES
      

 
<table width="100%"   align="center"  class="table_border_both">
<tr class="heading_table_top">
<td> To accompany futher works like integration of the script with php,java,c,c++ the required folder 
      structure is done</td>
</tr>
<tr>
</tr>

</table>        


#TODO

       -Clean this readme file 

       -Push the php code,it will be under php_dashboard

       -Push 4.py i.e double downloading i.e parallel 2 process of youtube-dl

       -Push 5.py i.e serial downlading from two url 
          At 95% of the first process (process #1),process #2 will begin the next 
          download of the URL found in  '_url_ ' list. 
          As soon as the first process reaches 100 %,this process will exit and only
          process #2 will be present.
          As process #2 reaches 95 %,process #3 (rebirth of process #1) will start the next download of the URL
          in the link

          and the chain follows.
          So to say even process is always #2,odd process is always process #1 in ideal situation


          Some cases :-

         Case 1:

            Synopsis 

            '_url_=['a','b','c','d','e','f']'

            a is 95 MB,b is 10 mb,c is 100 mb ,d is 1 GB ,e is 10 MB,f is 20 MB

            As a i.e process #1 reaches 95 % i.e 90.25 MB
             process #2 will start b,
             process #1 will terminate after reaching 100 % and completing the file


             Currently two process process are running  #1,#2 

             As process #2 reaches 95 % i.e 9.5 MB
              process #3 will start c

              Currently three process are running process #1,#2,#3

              Sooner or later #1,#2 reaches 100 % and both process exists



              So if I instead used the earlier design of 5.py

              - it would had process #1 had started 
              - at 95 % ,process #2 would have started
              - process #1 reaching 100% and finishing would start c
              - meanwhile process #2 would have also ended as the file size is small

              - so we see process #2 also starting c,if this happens c would surely get corrupted 
                alongside  both process reaching deadlock,

                so if anycase process #1 and process #2 would call the url, both will overwrite the same file.




                Means to break this :-

                -Implementing process kill or termination 

                - Breaking the list of '_url_' to two smaller list,chances are the same would happen too













	       
