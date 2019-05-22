import hashlib, time, requests
from requests.auth import HTTPBasicAuth


class Service(object):

    def __init__(self, usertype: str, request_type: str, auth):
        self.type = usertype
        self.base_url = "https://dev.gittigidiyor.com:8443/listingapi/rlws"
        self.auth = auth
        self.session = requests.session()
        self.session.auth = HTTPBasicAuth(self.auth.username, self.auth.password)
        self.request_type = request_type

    def requestURL(self, method: str, outputCT: str, inputCT: str, lang: str):
        return "{}/{}/{}?method={}&outputCT={}&inputCT={}&apiKey={}&sign={}&time={}&lang={}".format(self.base_url,
                                                                                                    self.type,
                                                                                                    self.request_type,
                                                                                                    method,
                                                                                                    outputCT, inputCT,
                                                                                                    self.auth.api_key,
                                                                                                    self.signature(),
                                                                                                    self.timestamp(),
                                                                                                    lang)

    @staticmethod
    def timestamp():
        return round(time.time()) * 1000

    def signature(self):
        return hashlib.md5(
            "{}{}{}".format(self.auth.api_key, self.auth.api_secret, self.timestamp()).encode("utf-8")).hexdigest()

    def auth(self):
        return self.auth
