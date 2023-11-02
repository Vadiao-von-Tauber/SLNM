import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class SuperTesting(unittest.TestCase):
    def test00(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.applitools.com/")
        time.sleep(3)
        self.about_us = self.driver.find_element(By.ID, "username")


        time.sleep(3)






if __name__ == '__main__':
   unittest.main()