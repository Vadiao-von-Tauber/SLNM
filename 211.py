import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Testing(pytest.TestCase):
   def test00(self):
       driver = webdriver.Chrome()
       driver.get("https://www.saucedemo.com/")
       input_username = driver.find_element(By.NAME, "user-name")
       self.assertIsNotNone(input_username)
       assert input_username is not True

   def test01(self):
       driver = webdriver.Chrome()
       driver.get("https://www.saucedemo.com/")
       input_username = None
       try:
        input_username = driver.find_element(By.NAME, "not name")
       except NoSuchElementException:
        assert True
       finally:
           assert (input_username is None)


if __name__ == '__main__':
   pytest.main()
