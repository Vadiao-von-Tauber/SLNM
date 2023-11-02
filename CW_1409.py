import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

class YandexAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.initialSetUp()
        self.webDriverSetUp()
        self.preSteps()

    def tearDown(self) -> None:
        self.driver.quit()

    def initialSetUp(self) -> None:
        self.page_url = "https://passport.yandex.by/auth"
        self.expected_url = self.page_url
        self.webElementSetUp()
        self.testDataSetUp()


    def testDataSetUp(self) -> None:
        self.invalid_login_semicolon = "babababaab;"
        self.invalid_login_empty = ""
        self.invalid_login_too_long = "wrhwihrfsiofhusfhfshilhrrrrrrrrrrrrrrrrrrrrbbbbbbbbbbbbbbbbbbbbbbbbbbbbdojrtjfjjf"


    def webElementSetUp(self) -> None:
        self.invalid_login_semicolon_hint_text = "Такой логин не подойдет"
        self.invalid_login_too_long_hint_text = "Такой логин не подойдет"
        self.invalid_login_empty_hint_text = "Логин не указан"

        self.login_field_id = "passp-field-login"
        self.submit_button_id = "passp:sign-in"
        self.invalid_login_hint_id = "field:input-login:hint"

    def webDriverSetUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.page_url)

    def preSteps(self) -> None:
        pass

    def test_yandex_invalid_login_with_semicolon(self) -> None:
        self.login(self.invalid_login_semicolon)
        self.assert_login(self.invalid_login_semicolon_hint_text)

        #self.invalid_login_hint = self.driver.find_element(By.ID, self.invalid_login_hint_id)
        #self.invalid_login_hint = self.driver.find_element(By.ID, self.invalid_login_semicolon)
        #self.assertEqual(self.invalid_login_hint.is_enabled(), True)
        #self.assertEqual(self.invalid_login_hint.text, self.invalid_login_with_semicolon_hint_text)


    def test_yandex_invalid_login_with_empty(self) -> None:
        self.login(self.invalid_login_empty)
        self.assert_login(self.invalid_login_empty_hint_text)
        #self.assertEqual(self.expected_url, self.driver.current_url)

        #self.assertEqual(self.expected_url, self.driver.current_url)
        #self.invalid_login_hint = self.driver.find_element(By.ID, self.invalid_login_hint_id)
        #self.assertEqual(self.invalid_login_hint.is_enabled(), True)
        #self.assertEqual(self.invalid_login_hint.text, self.invalid_login_with_empty_hint_text)


    def test_yandex_invalid_login_with_too_long(self) -> None:
        self.login(self.invalid_login_too_long)
        self.assert_login(self.invalid_login_too_long_hint_text)

        #self.assertEqual(self.expected_url, self.driver.current_url)
        #self.invalid_login_hint = self.driver.find_element(By.ID, self.invalid_login_hint_id)
        #self.assertEqual(self.invalid_login_hint.is_enabled(), True)
        #self.assertEqual(self.invalid_login_hint.text, self.invalid_login_with_too_long_hint_text)


    def login(self, login) -> None:
        self.login_field = self.driver.find_element(By.ID, self.login_field_id)
        self.login_field.send_keys(login)

        default_sleep_time = 1
        time.sleep(default_sleep_time)

        self.submit_button = self.driver.find_element(By.ID, self.submit_button_id)
        self.submit_button.click()

        time.sleep(default_sleep_time)

    def assert_login(self, hint_text) -> None:
        self.assertEqual(self.expected_url, self.driver.current_url)
        self.invalid_login_hint = self.driver.find_element(By.ID, self.invalid_login_hint_id)
        self.assertEqual(self.invalid_login_hint.is_enabled(), True)
        self.assertEqual(self.invalid_login_hint.text, hint_text)

#        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of(self.wrong_message_empty_login_element))

#        wait = WebDriverWait(self.driver, self.timeout + 1)
#        wait.until(EC.visibility_of(self.wrong_message_empty_login_element))