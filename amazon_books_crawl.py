#!/usr/bin/env python
# -*- coding=utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException

import json
import logging
import traceback
import ConfigParser
import urllib

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class BooksPreviewCrawl:

    def __init__(self):
        self.parse_config()
        logging.basicConfig(format='%(asctime)s %(message)s', level=self.log_level)

        if self.log_level == 'DEBUG':
            self.bpc = webdriver.Firefox()
        else:
            self.bpc = webdriver.PhantomJS()

    def __del__(self):
        self.bpc.quit()

    def parse_config(self):
        config = ConfigParser.ConfigParser()

        config.read(".config")
        self.timeout = config.get('load', 'timeout')
        self.log_level = config.get('logger', 'level')

    def load_page(self, url, show = False):
        logging.info("loading page, url: %s\n\n", url)
        self.bpc.get(url)
        if show:
            logging.info("%s", self.bpc.find_element_by_xpath("/html").text)
        else:
            logging.debug("%s", self.bpc.find_element_by_xpath("/html").text)

def main(argv):
    bpc = BooksPreviewCrawl()
    res = bpc.load_page("http://www.amazon.co.jp", True)
    print res

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
