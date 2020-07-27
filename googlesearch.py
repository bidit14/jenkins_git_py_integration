from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod


    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/Users/smarikagyawali/PycharmProjects/selenium_python/drivers/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_kathmandu(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Kathmandu")
        self.driver.find_element_by_class_name("gNO89b").click()
        #self.driver.find_element_by_name("btnk").click()

    def test_search_bidit(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("bidit upadhyay")
        self.driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")
if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='/Users/smarikagyawali/PycharmProjects/selenium_python/reports'))










