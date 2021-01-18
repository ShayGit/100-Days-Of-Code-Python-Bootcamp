import requests
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

RENTAL_LISTING = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"


class DataEntryAutomationBot():
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "Accept-Language": "he,en-US;q=0.9,en;q=0.8,he-IL;q=0.7"
        }
        response = requests.get(RENTAL_LISTING, headers=headers)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.text, "html.parser")
        self.prices = []
        self.addresses = []
        self.links = []

    def scrape_listings(self):
        details = self.soup.select(".list-card-info .list-card-link")
        self.addresses = [item.getText().split(" | ")[-1] for item in details]
        self.links = [item['href'] if item['href'].startswith("http") else f"https://www.zillow.com{item['href']}"
                      for item in details]
        all_prices = self.soup.select(".list-card-heading")

        for item in all_prices:
            price = ""
            try:
                price = item.select(".list-card-price")[0].contents[0]

            except IndexError:
                print('Multiple listings for the card')
                # Price with multiple listings
                price = item.select(".list-card-details li")[0].contents[0]
            finally:
                self.prices.append(price)

    def fill_form(self):
        for index in range(len(self.addresses)):
            self.driver.get(
                "GOOGLE_FORM_PATH")
            sleep(3)
            address_input = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_input.send_keys(self.addresses[index])
            price_input = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input.send_keys(self.prices[index])
            link_input = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input.send_keys(self.links[index])
            send_btn = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
            send_btn.click()
