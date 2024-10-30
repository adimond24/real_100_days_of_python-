from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Instant-Pot-Duo-Mini-Programmable/dp/B06Y1YD5W7/ref=sr_1_1?crid=27ZRXQ6M6VO17&dib=eyJ2IjoiMSJ9.tvjNZBK2YHNSvH2ajXoDr6w5hgE6pDftTY6R6oQVAlzYWSa1I-vHtWfvRVYaNltk8ewMOm5s-ptqSKJiBE90Uftk68IixHbOZUZ1N0r_de-dV9oL-seAZ6arbEKYD-z5gnAAoNGSDbv79FexRGSdn__adYMtxbYGdzXyjX0wrbb9hBc668TzAkL2tioxE7J3QOM3TKWT_o73yphbx2WKQ9vPnE3N4dUMiTj6VCeYpXo.K4LelwWEXWrX9et6m1ic1iBlmXqCZUgSruFyXbS36V0&dib_tag=se&keywords=instant+pot&qid=1730150422&sprefix=instant+pot%2Caps%2C136&sr=8-1")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cents.text}")

# driver.close()
#driver.quit()

driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
for time in event_times:
    print(time.text)