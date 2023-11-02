import unittest

from parametrized import parametrized
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DBConnectionSingleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBConnectionSingleton, cls).__new__(cls)
            # Add connection Impl and setting up
        return cls.instance


connection = DBConnectionSingleton()
another_connection = DBConnectionSingleton()

print(connection is another_connection)

connection.status = "\n                     +         +         +        I       N       T       E       R       R       U       P       T       E       D        +         +         +"
print(another_connection.status)


class PageObject:
    pass


class YMLoginPage:
    pass


class StdFlatBuilder(object):
   def __init__(self):
       self.rooms = "some std generated rooms"
       self.floor = None
       self.window = None
       self.sum = None

   def with_floor(self, floor_type):
      self.floor = floor_type
      return self

   def with_window(self, window_type):
      self.window = window_type
      return self

   def build(self):
       self.sum = 1000000000000000000000000000
       return self


my_future_khata = StdFlatBuilder().\
    with_floor("          плиты из темного нефрита").\
    with_window("          дубовая рама с золотым напылением")
print(my_future_khata.floor)
print(my_future_khata.window)
print("                                  А НЕ ЖИРНО ЛИ БУТЕРБРОД ВЫШЕЛ, АЛООООО")
print(my_future_khata.sum)