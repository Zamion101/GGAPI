from Service import Service
import json


class StoreService(Service):

    def __init__(self, auth):
        super().__init__('individual', 'store', auth)

    def getStore(self, lang: str = 'en') -> json:
        url = self.requestURL('getStore', 'json', 'json', lang)
        return self.session.get(url=url).json()
