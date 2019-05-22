import json
from Service import Service


class SaleService(Service):

    def __init__(self, auth):
        super().__init__('individual', 'activity', auth)

    def getSoldItems(self, startOffset=0, rowCount=100, withData=False, byStatus='S', lang: str = 'en') -> json:
        if rowCount > 100:
            rowCount = 100
        url = "{}&startOffSet={}&rowCount={}&withData={}&byStatus={}".format(
            self.requestURL('getSoldItems', 'json', 'json', lang),startOffset,rowCount,withData,byStatus)
        return self.session.get(url=url).json()

    def getActiveSales(self, startOffset=0, rowCount=100, withData=False, lang: str = 'en') -> json:
        if rowCount > 100:
            rowCount = 100
        url = "{}&startOffSet={}&rowCount={}&withData={}".format(
            self.requestURL('getActiveSales', 'json', 'json', lang), startOffset, rowCount, withData)
        return self.session.get(url=url).json()

    def getUnsoldItems(self, startOffset=0, rowCount=100, withData=False, lang: str = 'en') -> json:
        if rowCount > 100:
            rowCount = 100
        url = "{}&startOffSet={}&rowCount={}&withData={}".format(
            self.requestURL('getUnsoldItems', 'json', 'json', lang), startOffset, rowCount, withData)
        return self.session.get(url=url).json()

    def getWonItems(self, startOffset=0, rowCount=100, withData=False, lang: str = 'en') -> json:
        if rowCount > 100:
            rowCount = 100
        url = "{}&startOffSet={}&rowCount={}&withData={}".format(
            self.requestURL('getWonItems', 'json', 'json', lang), startOffset, rowCount, withData)
        return self.session.get(url=url).json()

    def getBidItems(self, startOffset=0, rowCount=100, withData=False, lang: str = 'en') -> json:
        if rowCount > 100:
            rowCount = 100
        url = "{}&startOffSet={}&rowCount={}&withData={}".format(
            self.requestURL('getBidItems', 'json', 'json', lang), startOffset, rowCount, withData)
        return self.session.get(url=url).json()

    def getWatchItems(self, startOffset=0, rowCount=100, withData=False, lang: str = 'en') -> json:
        if rowCount > 100:
            rowCount = 100
        url = "{}&startOffSet={}&rowCount={}&withData={}".format(
            self.requestURL('getWatchItems', 'json', 'json', lang), startOffset, rowCount, withData)
        return self.session.get(url=url).json()

    def getDidntWinItems(self, startOffset=0, rowCount=100, withData=False, lang: str = 'en') -> json:
        if rowCount > 100:
            rowCount = 100
        url = "{}&startOffSet={}&rowCount={}&withData={}".format(
            self.requestURL('getDidntWinItems', 'json', 'json', lang), startOffset, rowCount, withData)
        return self.session.get(url=url).json()
