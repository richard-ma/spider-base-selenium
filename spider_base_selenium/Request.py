class Request():
    def __init__(self, url=None, callback=None):
        self.url = url
        self.callback = callback

    def get_url(self):
        return self.url

    def get_callback(self):
        return self.callback
