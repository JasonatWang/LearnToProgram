import urllib.request


web_url = 'http://www.baidu.com'
web_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
request = urllib.request.Request(url=web_url, headers=web_header)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))