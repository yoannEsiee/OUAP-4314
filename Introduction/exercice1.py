
import requests

class req:
    def __init__(self):
	self.timeout=10
	self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 		(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def Connected(self,url):
	response = requests.get(url, headers=self.headers, timeout=self.timeout)
	print(response.content[0:1000])
	print(response.headers)
	print(response.text)
	#result.Connected()

result=req()
result.Connected(url="http://www.esiee.fr/")







