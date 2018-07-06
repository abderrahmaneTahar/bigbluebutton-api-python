
from hashlib import sha1
from re import match
from exceptions import BBBException
import sys
if sys.version_info[0] == 2:
	from urllib import quote
else:
	from urllib.request import quote


class UrlBuilder:
	def __init__(self, bbbServerBaseUrl, securitySalt):
		if not match('/[http|https]:\/\/[a-zA-Z1-9.]*\/bigbluebutton\/api\//', bbbServerBaseUrl):
			if not bbbServerBaseUrl.startswith("http://") and not bbbServerBaseUrl.startswith("https://"):
				bbbServerBaseUrl = "http://" + bbbServerBaseUrl
			if not bbbServerBaseUrl.endswith("/bigbluebutton/api/"):
				bbbServerBaseUrl = bbbServerBaseUrl[:bbbServerBaseUrl.index("/", 8)] + "/bigbluebutton/api/"

		self.securitySalt 		= securitySalt
		self.bbbServerBaseUrl 	= bbbServerBaseUrl

	def buildUrl(self, api_call, params={}):
		url = self.bbbServerBaseUrl
		url += api_call + "?"
		for key, value in params.items():
			url += key + "=" + quote(value) + "&"

		url += "checksum=" + self.__get_checksum(api_call, params)
		return url

	def __get_checksum(self, api_call, params={}):
		secret_str = api_call
		for key, value in params.items():
			secret_str += key + "=" + value + "&"
		if secret_str.endswith("&"):
			secret_str = secret_str[:-1]
		secret_str += self.securitySalt
		return sha1(secret_str.encode('utf-8')).hexdigest()
