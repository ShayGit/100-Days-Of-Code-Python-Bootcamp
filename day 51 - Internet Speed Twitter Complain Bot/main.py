from InternetSpeedTwitterBot import InternetSpeedTwitterBot
chrome_driver_path = "PATH"

if __name__ == '__main__':
    bot = InternetSpeedTwitterBot(chrome_driver_path)
    bot.get_internet_speed()
    bot.tweet_at_provider()




