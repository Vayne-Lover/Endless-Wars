import urllib5

request=urllib5.Request("www.baidu.com")
response=urllib5.urlopen(request)
print reponse.read()
