import json
from Service import Service


class UserMessageService(Service):

    def __init__(self, auth):
        super().__init__('individual', 'message', auth)

    def getInboxMessages(self, startOffset=0, rowCount=100, unread=False, lang: str = 'en') -> json:
        if rowCount > 100:
            rowCount = 100
        url = "{}&startOffSet={}&rowCount={}&unread={}".format(
            self.requestURL('getInboxMessages', 'json', 'json', lang), startOffset, rowCount, unread)
        return self.session.get(url=url).json()

    def sendNewMessage(self, to, title, content, sendCopy=False, lang: str = 'en'):
        req = {
            "to": to,
            "title": title,
            "messageContent": content,
            "sendCopy": sendCopy
        }
        url = self.requestURL('sendNewMessage', 'json', 'json', lang)
        return self.session.post(url=url, json=req).json()

    def getSendedMessages(self, startOffset=0, rowCount=100, lang: str = 'en') -> json:
        if rowCount > 100:
            rowCount = 100
        url = "{}&startOffSet={}&rowCount={}".format(self.requestURL('getSendedMessages', 'json', 'json', lang),
                                                     startOffset, rowCount)
        return self.session.get(url=url).json()
