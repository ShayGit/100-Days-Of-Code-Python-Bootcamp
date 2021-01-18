from selenium import webdriver

REQUEST_URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"

chrome_driver_path = "PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get(REQUEST_URL)
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)


driver.get("https://www.python.org/")

# search = driver.find_element_by_name("q")
# searchbar = search.get_attribute("placeholder")
# print(searchbar)

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# link = driver.find_element_by_css_selector(".documentation-widget a")
# print(link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times = driver.find_elements_by_css_selector(".event-widget time")
# for time in event_times:
#     print(time.get_attribute("datetime").split('T')[0])

event_titles = driver.find_elements_by_css_selector(".event-widget li a")

dict = {index: {"time": event_times[index].get_attribute("datetime").split('T')[0], "event": event_titles[index].text}
        for index in range(len(event_times))}

# or

# for idx in range(len(event_times)):
#     time = event_times[idx].get_attribute("datetime").split('T')[0]
#     event = event_titles[idx].text
#     dict[idx] = {"time": time, "event": event}

print(dict)
# driver.close()
driver.quit()
