from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)

#Find element by Link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

#find the "search" <input> by Name
search = driver.find_element(By.NAME, value="search")

#sending a key that is not a letter or number
search.send_keys("Python")
search.send_keys(Keys.ENTER)