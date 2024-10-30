from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

FB_EMAIL = YOUR FACEBOOK LOGIN EMAIL
FB_PASSWORD = YOUR FACEBOOK PASSWORD

driver = webdriver.Chrome()

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)

allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value=
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://tinder.com/")
#
# time.sleep(3)
#
#
# # push i decline button
#
#
#
#
#
#
# # choose_language_exit = driver.find_element(By.CSS_SELECTOR, value="#Pos(a) T(0) P(20px) P(12px)--xs End(0) D(b) button")
# # choose_language_exit.click()
#
# time.sleep(1)
#
# login = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
# login.click()
#
# time.sleep(1)
#
# phone_number_button = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button")
# phone_number_button.click()
#
# time.sleep(1)
#
# enter_phone_number = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/input')
# enter_phone_number.send_keys("4358491116")
# time.sleep(3)
# decline_cookies=driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/button")
# decline_cookies.click()
# time.sleep(2)
# next_button = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[1]/div/div[3]/button")
# next_button.click()

