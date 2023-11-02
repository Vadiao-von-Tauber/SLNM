""""https://github.com/alex-beaverg/PythonQA_Lessons/blob/main/HW_18_Alerts_Frames_Windows_etc/Test_HW_18_1_Homework.py"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChromeDriverSingleton(webdriver.Chrome):


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ChromeDriverSingleton, cls).__new__(cls)
        return cls.instance


class TestClass(unittest.TestCase):

    def setUp(self) -> None:
        self.setWebdriver()
        self.webdriverSetUp()
        self.pageUrls()
        self.setTestsParameters()


    def setWebriver(self) -> None:
        self.driver = ChromeDriverSingleton()


    def webDriverSetUp(self) -> None:
        self.timeout = 5
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.timeout)


    def pageUrls(self) -> None:
        self.page_url = 'https://the-internet.herokuapp.com/'


    def setTestParameters(self) -> None:
        self.setLocators()
        self.setVariables()


    def setLocators(self) -> None:
        self.alerts_link_text = 'JavaScript Alerts'
        self.alert_css_selector = '#content>div>ul>li:nth-child(1)>button'
        self.confirm_css_selector = '#content>div>ul>li:nth-child(2)>button'
        self.promt_css_selector = '#content>div>ul>li:nth-child(3)>button'
        self.result_id = 'result'


    def setVariables(self) -> None:
        self.expected_alert_text = 'I AM A JS ALERT'
        self.expected_alert_result = 'YOU SUCCEFULLY CLICKED AN ALERT'
        self.expected_confirm_text = 'I AM A JS CONFIRM'
        self.expected_confirm_result = 'YOU CLICKED [OK]'


    def tearDown(self) -> None:
        self.driver.quit()


    def following_the_link(self, link_text: str) -> None:
        self.driver.find_element(By.LINK_TEXT, link_text).click()


    def test01_alert_simple(self) -> None:
        self.driver.get(self.page_url)
        self.following_the_link(self.alerts_link_text)
        self.alert_button = self.driver.find_element(By.CSS_SELECTOR, self.alert_css_selector)
        self.alert_button.click()
        self.assertEqual(self.expected_alert_text, Alert(self.driver).text)
        Alert(self.driver).accept()
        self.alert_result_text = self.driver.find_element(By.ID, self.result_id).text
        self.assertEqual(self.expected_alert_result, self.alert_result_text)


    def test02_alert_confirm(self) -> None:
        self.driver.get(self.page_url)
        self.following_the_link(self.alerts_link_text)
        self.confirm_button = self.driver.find_element(By.CSS_SELECTOR, self.confirm_css_selector)
        self.confirm_button.click()
        self.assertEqual(self.expected_confirm_text, Alert(self.driver).text)
        Alert(self.driver).accept()
        self.confirm_result_text = self.driver.find_element(By.ID, self.result_id).text
        self.assertEqual(self.expected_confirm_result, self.confirm_result_text)