from .Spider import *
from .Helper import *

class Engine():
    def __init__(self):
        pass

    def run(self, spider: Spider):
        with create_driver('Chrome', headless=False) as driver:
            for request in spider.get_request():
                driver.get(request.get_url())
                if callable(request.callback):
                    request.callback(Response(driver))

