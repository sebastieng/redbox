import requests
from lxml import etree
import hmac
import hashlib

class SfrBox:

	def __init__(self,hashLogin, hashPassword):
		self.baseurl="http://192.168.1.1/api/1.0/"
		self.token = self.createToken(hashLogin, hashPassword)

	def createToken(self,hashLogin, hashPassword):

		getTokenRsp = requests.get(self.baseurl + "?method=auth.getToken").text.encode('utf-8')
		getTokenXml = etree.fromstring(getTokenRsp)
		token=getTokenXml.xpath("/rsp/auth/@token")[0]

		hashLogin2 = hmac.new( token,hashLogin, hashlib.sha256).hexdigest()
		hashPassword2 = hmac.new(token, hashPassword, hashlib.sha256).hexdigest()

		requests.get("http://192.168.1.1/api/1.0/?method=auth.checkToken&token="+token+"&hash=" +hashLogin2+hashPassword2)

		return token

	def enableWifi(self):
                rsp=requests.post(self.baseurl + "?method=wlan.enable&token="+self.token)
                print(rsp.text)

		rsp=requests.post(self.baseurl + "?method=wlan.start&token="+self.token)
		print(rsp.text)
		rsp=requests.get(self.baseurl + "?method=wlan.getInfo&token="+self.token)
                print(rsp.text)

        def disableWifi(self):
                rsp=requests.post(self.baseurl + "?method=wlan.stop&token="+self.token)
                print(rsp.text)
		
		rsp=requests.post(self.baseurl + "?method=wlan.disable&token="+self.token)
                print(rsp.text)

                rsp=requests.get(self.baseurl + "?method=wlan.getInfo&token="+self.token)
                print(rsp.text)

