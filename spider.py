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
            print('%s [sleep: %d]' % (url, interval))

    '''
    url = 'http://www.yogaoutlet.com'

    driver.get(url)

    li_elems = driver.find_elements_by_class_name('HorizontalList__Item')
    ret = set()
    for li_elem in li_elems:
        try:
            url = li_elem.find_element_by_tag_name('a').get_attribute('href')
            if 'collection' in url:
                ret.add(url)
        except:
            pass

    all_urls = set()
    for module in ret:
        driver.get(module)
        while(True):
            print(driver.current_url)
            elems = driver.find_elements_by_class_name('ProductItem__ImageWrapper')
            for elem in elems:
                try:
                    link = elem.get_attribute('href')
                    if link not in all_urls:
                        all_urls.add(link)
                except:
                    pass

            #page
            try:
                next_elem = driver.find_element_by_class_name('page-next')
            except:
                break

            try:
                next_elem.click()
            except:
                sleep(randint(5, 9))
                driver.get(driver.current_url)
                continue
            url = driver.current_url
            driver.get(url)

    driver.close()

    with open('result.txt', 'w') as f:
        for url in all_urls:
            f.write(url + '\n')
'''

if __name__ == '__main__':
    main()