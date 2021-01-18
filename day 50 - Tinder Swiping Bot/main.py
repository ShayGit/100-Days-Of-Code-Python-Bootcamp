from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

FBEMAIL = "EMAIL"
FBPASS = "PASSWORD"
chrome_driver_path = "path"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://www.tinder.com")


sleep(2)
login_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_button.click()

sleep(2)

fb_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
fb_button.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

sleep(2)
fb_email = driver.find_element_by_id("email")
fb_email.send_keys(FBEMAIL)
fb_pass = driver.find_element_by_id("pass")
fb_pass.send_keys(FBPASS)
fb_pass.send_keys(Keys.ENTER)

sleep(2)
driver.switch_to.window(base_window)
print(driver.title)

sleep(5)

allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

sleep(2)


for n in range(100):
    sleep(1)
    try:
        like_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_btn.click()
        print("like clicked")

    except ElementClickInterceptedException:
        try:
            print("Blocking Window")
            sleep(2)
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
            print("Its a match")


        except NoSuchElementException:
            sleep(2)
            try:
                premium = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]/span')
                premium.click()
            except NoSuchElementException:
                try:
                    add_to_homescreen = driver.find_element_by_xpath(
                        '//*[@id="modal-manager"]/div/div/div[2]/button[2]/span')
                    add_to_homescreen.click()
                except NoSuchElementException:
                    break
    except NoSuchElementException:
        try:
            print("super like alert")
            sleep(2)
            dismiss_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')
            dismiss_btn.click()
        except NoSuchElementException:
            sleep(2)


print("bot ended")
driver.quit()