from pprint import pprint

import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

EMAIL="TEST@EMAIL.COM"
PASSWORD="TESTPASS"

TARGET_PRICE = 100

REQUEST_URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language": "he,en-US;q=0.9,en;q=0.8,he-IL;q=0.7"
}

response = requests.get(REQUEST_URL, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
title_element = soup.find(id="productTitle")
price_element = soup.find(id="priceblock_ourprice")
price = float(price_element.getText().split()[0])
title = title_element.getText().strip()

message = f"The product's {title} price has been reduced below target price: {TARGET_PRICE},\n " \
          f"current price is:{price},\n link: {REQUEST_URL}"

if price < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Price Drop Alert\n\n{message}".encode("utf8")
        )
