from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "PATH"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
store = driver.find_elements_by_css_selector("#store div")

items_ids = [item.get_attribute("id") for item in store]
print(items_ids)

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes

final_dict = {}
while True:
    cookie.click()
    if time.time() > timeout:
        items_prices_elem = driver.find_elements_by_css_selector("#store b")
        items_prices = [int(price.text.split('-')[1].strip().replace(",", "")) for price in items_prices_elem if
                        price.text != ""]

        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        for index in range(len(items_prices)):
            price = items_prices[index]
            if cookie_count > price:
                final_dict[price] = items_ids[index]
        if len(final_dict):
            max_price = max(final_dict)
            id = final_dict[max_price]
            driver.find_element_by_id(id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break

driver.quit()
