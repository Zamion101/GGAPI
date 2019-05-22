from Service import Service
import json


class CargoService(Service):

    def __init__(self, auth):
        super().__init__('individual', 'cargo', auth)

    def getCargoInformation(self, saleCode: str, lang: str = 'en') -> json:
        url = "{}&saleCode={}".format(self.requestURL('getCargoInformation', 'json', 'json', lang), saleCode)
        return self.session.get(url=url).json()

    def sendCargoInformation(self, saleCode: str, cargoCode: str, cargoCompany: str, cargoBranch: str, followUpUrl: str,
                             userType: str = 'S', lang: str = 'en') -> json:
        req = {
            "saleCode": saleCode,
            "cargoPostCode": cargoCode,
            "cargoCompany": cargoCompany,
            "cargoBranch": cargoBranch,
            "followUpUrl": followUpUrl,
            "userType": userType
        }

        url = self.requestURL('sendCargoInformation', 'json', 'json', lang)
        return self.session.post(url=url, json=req).json()
