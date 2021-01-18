from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

ACCOUNT_EMAIL = "email"
ACCOUNT_PASSWORD = "password"
PHONE = "Phone_number"

chrome_driver_path = "PATH"

driver = webdriver.Chrome(chrome_driver_path)

driver.get(
    "https://www.linkedin.com/jobs/search/?geoId=104243116&keywords=junior%20python%20developer&location=Tel%20Aviv%2C%20Israel")

signin = driver.find_element_by_link_text("Sign in")
signin.click()

time.sleep(5)

email = driver.find_element_by_id("username")
email.send_keys(ACCOUNT_EMAIL)
password = driver.find_element_by_id("password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()