from .Request import Request
from .Response import Response

class Spider():
    def __init__(self):
        self.urls = list()

    def get_request(self):
        for url in self.urls:
            if isinstance(url, Request):
                req = url
            else:
                req = Request(url, callback=self.parse)
            yield req


    def parse(self, response: Response):
        raise NotImplementedError('Not implemented parse method.')