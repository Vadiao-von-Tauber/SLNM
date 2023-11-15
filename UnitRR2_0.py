from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

if __name__ == '__main__':

    custom_firefox_options = Options()
    custom_firefox_options.add_argument("--disable-exstensions")
    browser = webdriver.Firefox(options=custom_firefox_options)

    browser.get("https://www.google.by/")
    browser.maximize_window()
    search_edit_id = "APjFqb"
    search_edit = browser.find_element(By.ID, search_edit_id)

    search_edit.send_keys("Radio Record")
    search_edit.send_keys(Keys.RETURN)

    default_sleep_time = 5
    time.sleep(default_sleep_time)

    # A2_
    first_result_link = browser.find_element(By.PARTIAL_LINK_TEXT, "Record")
    first_result_link.click()

    time.sleep(default_sleep_time)
 # A3
    print(browser.current_url)
    assert browser.current_url == "https://www.radiorecord.ru/"

browser.quit()
