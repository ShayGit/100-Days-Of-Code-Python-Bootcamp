from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "PATH"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
submit = driver.find_element_by_css_selector("form button")

first_name.send_keys("Moshe")
last_name.send_keys("cohen")
email.send_keys("asdads@gmail.com")
submit.click()