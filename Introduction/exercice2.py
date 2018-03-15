
import requests

class req:
    def __init__(self):
	self.timeout=10
	self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 		(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def Connected(self,url):
	response = requests.get(url, headers=self.headers, timeout=self.timeout)

	x =response.delate_space(response.text)
	x = response.delete_caractere(response.text)
	return x
	
    def delete_space(self,code):
	code = " ".join(code.split())
	return code
	
    def delete_caractere(self,code):
	#regex = [^A-Za-Z0-9]+
	code = Regex.Replace(code, "[^a-zA-Z0-9_]", "");
	return code
	

result=req()
result.Connected(url="http://www.esiee.fr/")

