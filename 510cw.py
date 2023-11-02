import unittest
from typing import Self

from parametrized import parametrized
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class YandexLoginPageLocators:
    """Docstring: Class YandexLoginPageLocators"""
    LOGIN_FIELD = (By.ID, 'passp-field-login')
    SUBMIT_BUTTON = (By.ID, 'passp:sign-in')
    WRONG_MESSAGE = (By.ID, 'field:input-login:hint')


class SystemVariables:
    """Docstring: Class SystemVariables"""
    TIMEOUT = 5


class Waiters:
    """Docstring: Test Waiters"""
    @staticmethod
    def visibility_element(driver, element):
        """Docstring: Static method to run WebDriverWait with EC.visibility_of"""
        WebDriverWait(driver, SystemVariables.TIMEOUT).until(EC.visibility_of(element))


class YandexBasePage:
    """Docstring: Parent class BasePage"""
    def __init__(self, driver) -> None:
        """Docstring: Constructor for class YandexBasePage"""
        self.driver = driver


class YandexLoginPage(YandexBasePage):
    """Docstring: Class YandexLoginPage extends YandexBasePage"""
    def __init__(self, driver):
        """Docstring: Constructor for class YandexLoginPage"""
        super().__init__(driver)
        self.wrong_message_element = None

    def login(self, login_name: str) -> None:
        """Docstring: Method to login"""
        self.driver.find_element(*YandexLoginPageLocators.LOGIN_FIELD).send_keys(login_name)
        self.driver.find_element(*YandexLoginPageLocators.SUBMIT_BUTTON).click()

    def get_message(self) -> str:
        """Docstring: Method to get message after login"""
        self.wrong_message_element = self.driver.find_element(*YandexLoginPageLocators.WRONG_MESSAGE)
        Waiters.visibility_element(self.driver, self.wrong_message_element)
        return self.wrong_message_element.text

    def assert_login(self, expected_text) -> None:
        assert expected_text in self.get_message()


class ChromeDriverSingleton(webdriver.Chrome):
    """Docstring: Class singleton ChromeWebDriver"""
    def __new__(cls):
        """Docstring: Special constructor for singleton class ChromeWebDriver"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(ChromeDriverSingleton, cls).__new__(cls)
        return cls.instance

    def webdriver_setup(self) -> Self:
        """Docstring: Method to set up webdriver"""
        self.maximize_window()
        self.implicitly_wait(SystemVariables.TIMEOUT)
        return self


class TestClass(unittest.TestCase):
    """Docstring: Test class"""
    def setUp(self) -> None:
        """Docstring: Setup method before every test"""
        self.driver = ChromeDriverSingleton().webdriver_setup()
        self.pageSetUp()

    def pageSetUp(self) -> None:
        """Docstring: Page set up method"""
        self.page_url = 'https://passport.yandex.by/auth'
        self.driver.get(self.page_url)
        self.login_page = YandexLoginPage(self.driver)
        self.invalid_login = 'invalid-account-123-123'
        self.expected_invalid_login_text = 'Нет такого аккаунта'
        self.empty_login = ''
        self.expected_empty_login_text = 'Логин не указан'
        self.correct_symbol = 'q'
        self.long_login = 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq'
        self.expected_not_suitable_login_text = 'Такой логин не подойдет'

    @staticmethod
    def get_wrong_symbols() -> list:
        """Docstring: Static method to get list of wrong symbols for parametrize test methods"""
        return [';', ':', '!', '(', ')']

    def tearDown(self) -> None:
        """Docstring: Teardown method after every test"""
        self.driver.quit()

    def test_01_yandex_account_invalid_login(self) -> None:
        self.login_page.login(self.invalid_login)
        self.login_page.assert_login(self.expected_invalid_login_text)

    def test_02_yandex_account_empty_login(self) -> None:
        """Docstring: Test 02 (Yandex account empty log in)"""
        self.login_page.login(self.empty_login)
        self.login_page.assert_login(self.expected_empty_login_text)

    @parameterized.expand(get_wrong_symbols())
    def test_03_yandex_account_wrong_symbol_login(self, wrong_symbol: str) -> None:
        """Docstring: Test 03 (Yandex account wrong symbol log in)"""
        self.login_page.login(wrong_symbol)
        self.login_page.assert_login(self.expected_not_suitable_login_text)

    @parameterized.expand(get_wrong_symbols())
    def test_04_yandex_account_login_with_wrong_symbol(self, wrong_symbol: str) -> None:
        """Docstring: Test 04 (Yandex account log in with wrong symbol)"""
        self.login_page.login(self.correct_symbol + wrong_symbol)
        self.login_page.assert_login(self.expected_not_suitable_login_text)

    def test_05_yandex_account_long_login(self) -> None:
        """Docstring: Test 05 (Yandex account long log in)"""
        self.login_page.login(self.long_login)
        self.login_page.assert_login(self.expected_not_suitable_login_text)