from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="/Users/smarikagyawali/PycharmProjects/selenium_python/drivers/chromedriver")

driver.get ("https://blackboard.nec.edu/")

user_ele = driver.find_element_by_name("user_id")
print (user_ele.is_displayed())
print (user_ele.is_enabled())

pwd_ele = driver.find_element_by_name("password")
print (pwd_ele.is_displayed())
print (pwd_ele.is_enabled())

driver.find_element_by_xpath("//*[@id='agree_button']").click()

user_ele.send_keys("Bupadhyay_gps")
pwd_ele.send_keys("buddha12")
driver.find_element_by_xpath('//*[@id="entry-login"]').click()

course_radio = driver.find_element_by_class_name("global-toggle").click()
#print ("status of button" , course_radio.is_selected())
