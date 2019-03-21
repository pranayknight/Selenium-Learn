from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="/home/trickster/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("http://newtours.demoaut.com/")
ele = driver.find_element_by_name("userName")   # to verify if that field exists or not
print(ele.is_displayed())                       # print the true or false if it exists
print(ele.is_enabled())                         # prints true/false based on the status of the element

pwd = driver.find_element_by_name("password")
print(pwd.is_displayed())
print(pwd.is_enabled())

ele.send_keys("mercury")
pwd.send_keys("mercury")

driver.find_element_by_name("login").click()
roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print("Status of Round Trip radio button: ", roundtrip_radio.is_selected())    # print status of radio button

onetrip_radio = driver.find_element_by_css_selector("input[value=oneway]")
print("Status of One Way Trip radio button: ", onetrip_radio.is_selected())

driver.close()
