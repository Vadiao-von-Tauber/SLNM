#firsttest
import unittest

from parametrized import parametrized
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestYandexAccountNegativeLogins(unittest.TestCase):
    """Docstring: Test class"""

    def setUp(self) -> None:
        """Docstring: Setup method before every test"""
        self.setWebdriver()
        self.webdriverSetUp()
        self.pageSetUp()
        self.setTestsParameters()

    def setWebdriver(self) -> None:
        """Docstring: Set webdriver setup method"""
        self.driver = webdriver.Chrome()

    def webdriverSetUp(self) -> None:
        """Docstring: Webdriver setup method"""
        self.timeout = 5
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.timeout)

    def pageSetUp(self) -> None:
        """Docstring: Page setup method"""
        self.page_url = 'https://passport.yandex.by/auth'
        self.driver.get(self.page_url)

    def setTestsParameters(self) -> None:
        """Docstring: Method to set parameters to all tests"""
        self.setLocators()
        self.setVariables()

    def setLocators(self) -> None:
        """Docstring: Set locators method"""
        self.login_field_id = 'passp-field-login'
        self.submit_button_id = 'passp:sign-in'
        self.wrong_message_id = 'field:input-login:hint'

    def setVariables(self) -> None:
        """Docstring: Set variables method"""
        self.expected_url = 'https://passport.yandex.by/auth'
        self.invalid_login = 'invalid-account-123-123'
        self.empty_login = ''
        self.correct_symbol = 'q'
        self.long_login = 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq'
        self.expected_invalid_login_text = 'Нет такого аккаунта'
        self.expected_empty_login_text = 'Логин не указан'
        self.expected_not_suitable_login_text = 'Такой логин не подойдет'

    @staticmethod
    def get_wrong_symbols() -> list:
        """Docstring: Static method to get list of wrong symbols for parametrize test methods"""
        return [';', ':', '!', '(', ')']

    def tearDown(self) -> None:
        """Docstring: Teardown method after every test"""
        self.driver.quit()

    def login_action(self, login_name: str) -> None:
        """Docstring: Log in method"""
        self.login_field_element = self.driver.find_element(By.ID, self.login_field_id)
        self.login_field_element.send_keys(login_name)
        self.submit_button_element = self.driver.find_element(By.ID, self.submit_button_id)
        self.submit_button_element.click()

    def assert_login(self, expected_text: str) -> None:
        """Docstring: Assert log in method"""
        self.wrong_message_element = self.driver.find_element(By.ID, self.wrong_message_id)
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of(self.wrong_message_element))
        self.assertEqual(self.expected_url, self.driver.current_url)
        self.assertIn(expected_text, self.wrong_message_element.text)

    def test_01_yandex_account_invalid_login(self) -> None:
        """Docstring: Test 01 (Yandex account invalid log in)"""
        self.login_action(self.invalid_login)
        self.assert_login(self.expected_invalid_login_text)

    def test_02_yandex_account_empty_login(self) -> None:
        """Docstring: Test 02 (Yandex account empty log in)"""
        self.login_action(self.empty_login)
        self.assert_login(self.expected_empty_login_text)

    @parametrized.expand(get_wrong_symbols())
    def test_03_yandex_account_wrong_symbol_login(self, wrong_symbol: str) -> None:
        """Docstring: Test 03 (Yandex account wrong symbol log in)"""
        self.login_action(wrong_symbol)
        self.assert_login(self.expected_not_suitable_login_text)

    @parametrized.expand(get_wrong_symbols())
    def test_04_yandex_account_login_with_wrong_symbol(self, wrong_symbol: str) -> None:
        """Docstring: Test 04 (Yandex account log in with wrong symbol)"""
        self.login_action(self.correct_symbol + wrong_symbol)
        self.assert_login(self.expected_not_suitable_login_text)

    def test_05_yandex_account_long_login(self) -> None:
        """Docstring: Test 05 (Yandex account long log in)"""
        self.login_action(self.long_login)
        self.assert_login(self.expected_not_suitable_login_text)


#    builder = ActionChains(self.driver)
