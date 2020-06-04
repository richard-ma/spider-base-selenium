#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from typing import Optional, Any

import os, time, random
from contextlib import contextmanager # with statement
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep
from random import randint

class NoSuchDriverException(Exception):
    pass

@contextmanager
def create_driver(driver):
    # start with
    driver_list = {
        'Chrome': 'chromedriver',
        'Firefox': 'geckodriver',
    }

    if driver not in driver_list.keys():
        raise NoSuchDriverException('Cannot find webdriver named %s' % (driver))

    driver_path = os.path.join(os.getcwd(), 'driver', driver_list[driver])
    print(driver_path) # TODO: add to log

    create_func = getattr(webdriver, driver) #Call webdriver.Chrome or webdriver.Firefox etc.
    driver = create_func(driver_path)
    # return driver
    yield driver

    # end with
    driver.close()

def random_sleep(low_bound, high_bound):
    interval = random.randint(low_bound, high_bound)
    time.sleep(interval)
    return interval

def load_urls_file(filename):
    urls = list()
    with open(filename, 'r') as f:
        urls = f.readlines()
    return urls

def main():
    urls_filename = './urls.txt'
    interval_low_bound, interval_high_bound = 3, 13

    with create_driver('Chrome') as driver:
        for url in load_urls_file(urls_filename):
            interval = random_sleep(interval_low_bound, interval_high_bound)
            driver.get(url)
            # TODO: log url and sleep time
            print('[Get: %s] - [Sleep: %d]' % (url, interval))

if __name__ == '__main__':
    main()