class Auth(object):

    """
     This class represents Authentication/API credentials..
    API key and API secret must be optional because there are
    some services such as Application Service, does not
    need API credentials. Instead, it creates API credentials..
    """
    def __init__(self, username, password, api_key, api_secret):
        """
        :param username: GittiGidiyor Developer Username
        :param password: GittiGidiyor Developer Password
        :param api_key: Application API Key
        :param api_secret: Application Secret Key
        """
        self.username = username
        self.password = password
        self.api_key = api_key
        self.api_secret = api_secret
