from DataEntryAutomationBot import DataEntryAutomationBot

chrome_driver_path = "PATH"

bot = DataEntryAutomationBot(chrome_driver_path)
bot.scrape_listings()
bot.fill_form()
