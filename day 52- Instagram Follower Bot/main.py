
from InstagramBot import InstagramBot
chrome_driver_path = "PATH"

if __name__ == '__main__':
    bot = InstagramBot(chrome_driver_path)
    bot.login()
    bot.find_followers()
    bot.follow()

