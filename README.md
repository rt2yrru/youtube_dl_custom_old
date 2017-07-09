
<br> Want to embed youtube-dl,this is some of the ways I do it </br>

<table align="center" border="1" cellpadding="1" cellspacing="1" style="width:500px">
	<thead>
		<tr>
			<th scope="row">1.py</th>
		</tr>
	</thead>
	
</table>

<table align="center" border="1" ">
	<tbody>
		<tr>
			<td> It starts to download the video mentioned in _url_,with ydl_opts as the parameter.</td>
			
		</tr>
		<tr>
			<td>It will create a json file a.json which gets re written every time,you can use it to create a custom logger and display it as realtime progress</td>
			
		</tr>
		<tr>
			<td>The json is also printed in the terminal and cleared every time,so that you can see the realtime progress</td>
		</tr>
		<tr>
			<td>It will send a custom notification at 80 percent progress so that you can prepare the code, at 100 % or finished,a notification of 'file download ' will appear to notify you that the file has been downloaded </td>
			
		</tr>
		<tr>
		
		</tr>
	</tbody>
</table>
![alt-tag](https://travis-ci.org/siddht1/youtube-dl.svg?branch=master)


