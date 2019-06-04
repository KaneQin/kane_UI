# -*- encoding:utf-8 -*-

from kane.utils.abs import Singleton
from kane.config import DRIVER
from selenium import webdriver

@Singleton
class WebDriver():

    __driver = None

    def __init__(self):
        if self.__driver == None:
            if self.__driver == "Chrome":
                self.__driver == webdriver.Chrome()

            else:
                self.__driver == webdriver.Firefox()

    def get_driver(self):
        return self.__driver