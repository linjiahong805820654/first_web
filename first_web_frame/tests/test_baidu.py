#!/user/bin/python3
#coding=utf-8

from selenium import webdriver
import unittest
import time
import pytest

class Baidu(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"

    def test_01_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("iTesting")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        search_result = driver.find_element_by_xpath('//*[@id="1"]/h3/a').get_attribute('innerHTML')
        self.assertEqual('iTesting' in search_result, True)

    @unittest.skip("i want to skip")
    def test_baidu_set(self):
        driver = self.driver
        driver.get(self.base_url + "/gaoji/preferences.html")
        m = driver.find_element_by_xpath('.//*[@id="nr"]')
        m.find_element_by_xpath("//option[@value='10']").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    #pytest.main()
    unittest.main(verbosity=2)