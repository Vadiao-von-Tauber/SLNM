# https://litecart.stqa.ru/en/

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class ChromeDriverSingleton(webdriver.Chrome):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ChromeDriverSingleton, cls).__new__(cls)
        return cls.instance


class TestClassHellDucksWebPage(unittest.TestCase):

    def setUp(self) -> None:
        self.setWebdriver()
        self.webdriverSetUp()
        self.pageSetUp()
        self.setTestParameters()

    def setWebdriver(self) -> None:
        self.driver = ChromeDriverSingleton()

    def webdriverSetUp(self) -> None:
        self.timeout = 12
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.timeout)

    def pageSetUp(self) -> None:
        self.page_url = 'http://litecart.stqa.ru/en/'
        self.driver.get(self.page_url)

    def setTestParameters(self) -> None:
        self.setLocators()
        self.setVariables()

    def setLocators(self) -> None:
        self.title_of_login_box_css_selector = '#box-account-login .title'
        self.input_login_element_name = 'email'
        self.input_password_element_name = 'password'
        self.button_login_element_name = 'login'
        self.text_after_login_css_selector ='.notice.success'
        self.rubber_ducks_menu_item_element_css_selector = '#site-menu .category-1 > a'
        self.text_after_click_to_menu_item_element_css_selector = 'h1.title'
        self.duck_class = 'name'
        self.button_sort_by_name_element_css_selector = 'nav.filter>a:first-child'
        self.sticker_sale_element_css_selector = 'div.sticker.sale'
        self.search_field = 'input.search.query'
        self.blue_duck_search_word = 'blue duck'

    def setVariables(self) -> None:
        self.expected_title_of_login_box = 'Login'
        self.login = 'darkvadish@gmail.com'
        self.password = 'hell_o_vata!'
        self.expected_part_of_text_after_login = 'Lucius Tauber'
        self.expected_text_after_click_to_rubber_ducks_menu_item = 'Rubber Ducks'
        self.expected_text_after_click_to_subcategory_menu_item = 'Subcategory'
        self.expected_text_sale = 'SALE'
        self.expected_text_search = 'Search Results for "blue duck"'

    def tearDown(self) -> None:
        self.driver.quit()

    def test_zero_open_login_page(self) -> None:
        self.title_of_login_box = self.driver.find_element(By.CSS_SELECTOR, self.title_of_login_box_css_selector).text
        self.assertEqual(self.expected_title_of_login_box, self.title_of_login_box)


    def test_one_login_as_a_customer(self) -> None:
        self.input_login_element = self.driver.find_element(By.NAME, self.input_login_element_name)
        self.input_login_element.send_keys(self.login)
        self.input_password_element = self.driver.find_element(By.NAME, self.input_password_element_name)
        self.input_password_element.send_keys(self.password)
        self.button_login_element = self.driver.find_element(By.NAME, self.button_login_element_name)
        self.button_login_element.click()
        self.text_after_login_element = self.driver.find_element(By.CSS_SELECTOR, self.text_after_login_css_selector)
        self.assertTrue(self.text_after_login_element.text.__contains__(self.expected_part_of_text_after_login))

    def test_two_open_fokken_ducks_page(self) -> None:
        self.rubber_ducks_menu_item_element = self.driver \
            .find_element(By.CSS_SELECTOR, self.rubber_ducks_menu_item_element_css_selector)
        self.rubber_ducks_menu_item_element.click()
        self.text_after_click_to_rubber_ducks_menu_item = self.driver \
            .find_element(By.CSS_SELECTOR, self.text_after_click_to_menu_item_element_css_selector).text
        self.assertEqual(self.expected_text_after_click_to_rubber_ducks_menu_item,
                         self.text_after_click_to_rubber_ducks_menu_item)

    def test_tree_sort_rubber_ducks_by_name(self) -> None:
        self.rubber_ducks_menu_item_element = self.driver \
            .find_element(By.CSS_SELECTOR, self.rubber_ducks_menu_item_element_css_selector)
        self.rubber_ducks_menu_item_element.click()
        self.all_ducks_before_sort = self.driver.find_elements(By.CLASS_NAME, self.duck_class)
        self.ducks_names_before_sort = []
        for duck in self.all_ducks_before_sort:
            self.ducks_names_before_sort.append(duck.text)
        self.ducks_names_before_sort.sort()
        self.button_sort_by_name = self.driver \
            .find_element(By.CSS_SELECTOR, self.button_sort_by_name_element_css_selector)
        self.button_sort_by_name.click()
        self.all_ducks_after_sort = self.driver.find_elements(By.CLASS_NAME, self.duck_class)
        self.ducks_names_after_sort = []
        for duck in self.all_ducks_after_sort:
            self.ducks_names_after_sort.append(duck.text)
        self.assertEqual(self.ducks_names_after_sort, self.ducks_names_before_sort)

    def test_four_check_sticker_sale(self) -> None:
        self.rubber_ducks_menu_item_element = self.driver \
            .find_element(By.CSS_SELECTOR, self.rubber_ducks_menu_item_element_css_selector)
        self.rubber_ducks_menu_item_element.click()
        self.text_sale = self.driver.find_element(By.CSS_SELECTOR, self.sticker_sale_element_css_selector).text
        self.assertEqual(self.expected_text_sale, self.text_sale)

    def test_five_search_blue_duck(self) -> None:
        self.search_field = self.driver.find_element(By.CSS_SELECTOR, self.search_field)
        self.blue_duck_search_word = self.driver.find_element(By.CSS_SELECTOR, self.blue_duck_search_word).text
        self.search_field.get()
        self.assertEqual(self.expected_text_search)
