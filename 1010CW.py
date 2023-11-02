import unittest
from typing import Self

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class BasePageLocators:
    PAGE_TITLE = (By.CSS_SELECTOR, 'h1.title')


class LoginPageLocators:
    TITLE_OF_LOGIN_BOX = (By.CSS_SELECTOR, '#box-account-login .title')
    INPUT_LOGIN = (By.NAME, 'email')
    INPUT_PASSWORD = (By.NAME, 'password')
    BUTTON_LOGIN = (By.NAME, 'login')
    TEXT_AFTER_LOGIN = (By.CSS_SELECTOR, '.notice.success')


class MainMenuElementLocators:
    MAIN_MENU_ITEM_ELEMENT = (By.CSS_SELECTOR, '#site-menu .category-1 > a')


class RubberDucksPageLocators:
    DUCK = (By.CLASS_NAME, 'name')
    BUTTON_SORT_BY_NAME = (By.CSS_SELECTOR, 'nav.filter>a:first-child')
    STICKER_SALE = (By.CSS_SELECTOR, 'div.sticker.sale')


class SystemVariables:
    TIMEOUT = 5

class BasePage:
   def __init__(self, driver) -> None:
       self.driver = driver
       self.main_menu = MainMenuElement(self.driver)

   def __get_title(self) -> str:
       return self.driver.find_element(*BasePageLocators.PAGE_TITLE).text

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__expected_title_of_login_box = 'Login'
        self.__login = 'darkvadish@gmail.com'
        self.__password = 'hell_o_vata!'
        self.__expected_part_of_text = 'Lucius Tauber'

    def __get_title_of_login_box(self) -> str:
        return self.driver.find_element(*LoginPageLocators.TITLE_OF_LOGIN_BOX).text

    def assert_title(self) -> None:
        assert self.__expected_title_of_login_box, self.__get_title_of_login_box()

    def login_action(self) -> None:
        self.driver.find_element(*LoginPageLocators.INPUT_LOGIN).send_keys(self.__login)
        self.driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(self.__password)
        self.driver.find_element(*LoginPageLocators.BUTTON_LOGIN).click()

    def __get_message(self) -> str:
        return self.driver.find_element(*LoginPageLocators.TEXT_AFTER_LOGIN).text

    def assert_login(self) -> None:
        assert self.__expected_part_of_text_after_login in self.__get_message()


class MainMenuElement:
    def __init__(self, driver) -> None:
        self.driver = driver

    def click_to_rubber_ducks_item(self) -> None:
        self.driver.find_element(*MainMenuElementLocators.MAIN_MENU_ITEM_ELEMENT).click()

    def click_to_subcategory_item(self) -> None:
        ActionChains(self.driver)\
            .move_to_element(self.driver.find_element(*MainMenuElementLocators.MAIN_MENU_ITEM_ELEMENT))\
            .move_by_offset(0, 45)\
            .click()\
            .perform()


class RubberDucksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__rubber_ducks_title = 'Rubber Ducks'
        self.__all_ducks_before_sort = []
        self.__ducks_names_before_sort = []
        self.__all_ducks_after_sort = []
        self.__ducks_names_after_sort = []
        self.__expected_text_sale = 'SALE'

    def assert_title(self) -> None:
        assert self.__rubber_ducks_title, self.__get_title()

    def sort_ducks_by_name(self) -> None:
        self.driver.find_element(*RubberDucksPageLocators.BUTTON_SORT_BY_NAME).click()

    def assert_sorting_by_name(self) -> None:
        self.__all_ducks_before_sort = self.driver.find_element(*RubberDucksPageLocators.DUCK)
        for duck in self.__all_ducks_before_sort:
            self.__all_ducks_before_sort.append(duck.text)
        self.__ducks_names_before_sort.sort()
        self.__all_ducks_after_sort = self.driver.find_elements(*RubberDucksPageLocators.DUCK)
        for duck in self.__all_ducks_after_sort:
            self.__ducks_names_after_sort.append(duck.text)
        assert self.__ducks_names_after_sort, self.__ducks_names_before_sort

    def __get_sale(self) -> str:
        return self.driver.find_element(*RubberDucksPageLocators.STICKER_SALE).text

    def assert_getting_sale(self) -> None:
        assert self.__expected_text_sale, self.__get_sale()


class SubCategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__subcategory_title = 'Subcategory'

    def assert_title(self) -> None:
        assert self.__subcategory_title, self.__get_title()


class ChromeDriverSingleton(webdriver.Chrome):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ChromeDriverSingleton, cls).__new__(cls)
        return cls.instance

    def webdriver_setup(self) -> Self:
        self.maximize_window()
        self.implicitly_wait(SystemVariables.TIMEOUT)
        return self


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = ChromeDriverSingleton().webdriver_setup()
        self.pageSetUp()

    def pageSetUp(self) -> None:
        self.page_url = 'http://litecart.stqa.ru/en/'
        self.driver.get(self.page_url)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_00_open_login_page(self) -> None:
        self.login_page = LoginPage(self.driver)
        self.login_page.assert_title()

    def test_01_login_as_a_customer(self) -> None:
        self.login_page = LoginPage(self.driver)
        self.login_page.login_action()
        self.login_page.assert_login()

    def test_02_open_rubber_duck_page(self) -> None:
        self.rubber_duck_page = RubberDucksPage(self.driver)
        self.rubber_duck_page.main_menu.click_to_rubber_ducks_item()
        self.rubber_duck_page.assert_title()

    def test_03_open_subcategory_page(self) -> None:
        self.subcategory_page = SubCategoryPage(self.driver)
        self.subcategory_page.main_menu.click_to_rubber_ducks_item()
        self.subcategory_page.assert_title()

    def test_04_sort_rubber_ducks_by_name(self) -> None:
        self.rubber_duck_page = RubberDucksPage(self.driver)
        self.rubber_duck_page.main_menu.click_to_rubber_ducks_item()
        self.rubber_duck_page.sort_ducks_by_name()
        self.rubber_duck_page.assert_sorting_by_name()

    def test_05_check_sticker_sale(self) -> None:
        self.rubber_duck_page = RubberDucksPage(self.driver)
        self.rubber_duck_page.main_menu.click_to_rubber_ducks_item()
        self.rubber_duck_page.assert_getting_sale()
