from Service import Service
import json


class ProductService(Service):

    def __init__(self, auth):
        super().__init__('individual', 'product', auth)

    def insertProduct(self, item_id: str, forceToSpecEntry: bool, nextDateOption: bool, request: dict,
                      lang: str = 'en') -> json:
        url = "{}&itemId={}&forceToSpecEntry={}&nextDateOption={}".format(
            self.requestURL('insertProduct', 'json', 'json', lang), item_id, forceToSpecEntry, nextDateOption)
        return self.session.post(url=url, json=request).json()

    def getProduct(self, lang: str, product_id: object) -> json:
        url = "{}&id=productId&value={}".format(self.requestURL('getProduct', 'json', 'json', lang), product_id)
        return self.session.get(url).json()

    def getProducts(self, startOffSet=0, rowCount=100, status='A', withData=False, lang: str = 'en') -> json:
        if rowCount > 100:
            rowCount = 100
        url = "{}&startOffSet={}&rowCount={}&status={}&withData={}".format(
            self.requestURL('getProducts', 'json', 'json', lang), startOffSet, rowCount, status, withData)
        return self.session.get(url=url).json()
