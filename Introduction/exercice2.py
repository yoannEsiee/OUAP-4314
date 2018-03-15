
import requests
import re

class req:
    def __init__(self):
        self.timeout=10
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 	  (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def Connected(self,url):
        response = requests.get(url, headers=self.headers, timeout=self.timeout)

        x = self.delete_space(response.text)
        x = self.delete_caractere(x)
        return x
	
    def delete_space(self,code):
        code = " ".join(code.split())
        return code
	
    def delete_caractere(self,code):
	#regex = [^A-Za-Z0-9]+
        code = re.sub( "[^a-zA-Z0-9_\s]", "", code);
        return code
	

result=req()
print(result.Connected(url="http://www.esiee.fr/"))

