import os
from contextlib import contextmanager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class NoSuchDriverException(Exception):
    pass


@contextmanager
def create_driver(driver, headless=False):
    # start with
    driver_list = {
        'Chrome': 'chromedriver',
        'Firefox': 'geckodriver',
    }

    if driver not in driver_list.keys():
        raise NoSuchDriverException('Cannot find webdriver named %s' % (driver))

    driver_path = os.path.join(os.getcwd(), 'driver', driver_list[driver])
    print(driver_path)  # TODO: add to log

    chrome_options = Options()
    if headless:
        if driver is 'Chrome':
            chrome_options.add_argument("--headless")

    create_func = getattr(webdriver, driver)  # Call webdriver.Chrome or webdriver.Firefox etc.
    driver = create_func(driver_path, options=chrome_options)
    # return driver
    yield driver

    # end with
    if callable(getattr(driver, "close")):
        driver.close()
