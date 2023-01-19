;iphone.txt and ipad.txt has to be located at the same directory
+d::
FileRead, iphoneurl, iphone.txt
FileRead, ipadurl, ipad.txt
clipboard = %clipboard%
iphoneURL = %iphoneurl%%clipboard%
ipadURL = %ipadurl%%clipboard%
iphonereq := ComObjCreate("WinHttp.WinHttpRequest.5.1")
iphonereq.Open("POST", iphoneURL)
iphonereq.Send()
ipadreq := ComObjCreate("WinHttp.WinHttpRequest.5.1")
ipadreq.Open("POST", ipadURL)
ipadreq.Send()