from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "PATH"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles_number = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# print(articles_number.text)
# articles_number.click()

all_portal = driver.find_element_by_link_text("All portals")
# all_portal.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
# driver.quit()