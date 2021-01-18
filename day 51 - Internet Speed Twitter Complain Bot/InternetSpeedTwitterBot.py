from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

PROMISED_DOWN = 100
PROMISED_UP = 5
TWITTER_EMAIL = "EMAIL"
TWITTER_PASS = "PASSWORD"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.down: float
        self.up: float

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(3)
        go_btn = self.driver.find_element_by_css_selector(".start-button a")
        go_btn.click()
        sleep(40)
        self.down = float(self.driver.find_element_by_css_selector(".result-data .download-speed").text)
        self.up = float(self.driver.find_element_by_css_selector(".result-data .upload-speed").text)
        print(self.down, '\n', self.up)

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.driver.get("https://twitter.com/")
            sleep(3)
            login = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]')
            login.click()
            username = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
            password = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
            username.send_keys(TWITTER_EMAIL)
            password.send_keys(TWITTER_PASS)
            sleep(2)
            password.send_keys(Keys.ENTER)
            sleep(5)
            content = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
            msg = f"Hey Internet Provider, why is my internet speed is\n" \
                  f"{self.down}down/{self.up}up, when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up"
            content.send_keys(msg)
            sleep(3)
            tweet = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
            tweet.click()

            sleep(2)
            self.driver.quit()
