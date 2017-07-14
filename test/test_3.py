_url_=[]
_url_.append('a1')
_url_.append('a2') 
_url_.append('a3')

_i=len(_url_)
_aa=[]
_bb=[]
_k=0
print(" _url_ is ")
print(_url_)
print("  ") 
print(" list #1 is :")	 
print(_aa)   
print("  ") 
print(" list #2 is :")	 
print(_bb)  
print("  ") 
if _i%2 == 0 :
    print(" Even 2 two list will be formed")

elif _i%2 != 0 :
    print(" list #1 will have 1 extra value than list #2")
else :
    print(" This should not have happen FATAL error")   
for item in _url_:
	_k+=1
	if _k%2 == 0:
		_bb.append(item)
		
	elif _k%2 != 0: 	
		_aa.append(item)
		
	else :
	    print("FATAL ERROR")	
print(" list #1 is :")	 
print(_aa)  
print("  ") 
print(" list #2 is :")	 
print(_bb)  
print("  ") 
print(" _url_ is ")
print(_url_)
