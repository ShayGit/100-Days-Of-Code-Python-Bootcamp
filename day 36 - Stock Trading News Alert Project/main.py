import requests
from datetime import datetime, timedelta
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API = "NEWS_API"

ALPHAVANTAGE_API = "ALPHAVANTAGE_API"
ALPHAVANTAGE_BASE_URL = "https://www.alphavantage.co/query"

twilio_account_sid = 'twilio_account_sid'
twilio_auth_token = 'twilio_auth_token'

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
params= {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API
}
response = requests.get(ALPHAVANTAGE_BASE_URL,params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
yesterday = datetime.strftime(datetime.now() - timedelta(3),'%Y-%m-%d')
two_days_ago = datetime.strftime(datetime.now() - timedelta(4),'%Y-%m-%d')
yesterday_data = data[yesterday]
two_days_ago_data = data[two_days_ago]

yesterday_closing = yesterday_data["4. close"]
two_days_ago_closing = two_days_ago_data["4. close"]

diff = float(yesterday_closing) - float(two_days_ago_closing)
up_down = None
if diff > 0 :
    up_down="Up!"
else:
    up_down="Down!"
diff_percent = round((diff / float(yesterday_closing)) * 100)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if abs(diff_percent) > 0.5:
    new_params = {
        "apiKey": "apiKey",
        "qInTitle": COMPANY_NAME
    }
    NEWS_BASE_URL = "https://newsapi.org/v2/everything"
    response_news = requests.get(NEWS_BASE_URL, new_params)
    response_news.raise_for_status()
    data = response_news.json()
    articles = data["articles"][:3]
    print(articles)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline:{article['title']} \nBrief:{article['description']}" for article in articles]
    client = Client(twilio_account_sid,twilio_auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='phonenumber',
            to='phonenumber'
        )
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

