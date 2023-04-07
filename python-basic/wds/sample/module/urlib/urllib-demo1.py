import urllib.request
file=urllib.request.urlopen("https://www.baidu.com")
data=file.read()
dataline=file.readline();
print(dataline)
print(data)