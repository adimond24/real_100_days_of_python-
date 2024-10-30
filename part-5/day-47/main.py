import smtplib
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9",
}

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(url=practice_url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
# print(price)

price_without_currency = price.split("$")[1]
# print(price_without_currency)

price_as_float = float(price_without_currency)
print(price_as_float)

# ====================== Send an Email ===========================
load_dotenv()
YOUR_SMTP_ADDRESS = os.getenv("YOUR_SMTP_ADDRESS")
YOUR_EMAIL = os.getenv("YOUR_EMAIL")
YOUR_PASSWORD = os.getenv("YOUR_PASSWORD")

title = soup.find(id="productTitle").get_text().strip()
print(title)

#price you want to get notification about
BUY_PRICE = 100

if price_as_float < BUY_PRICE:

    message = f"{title} is for sale for less {price}!"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{practice_url}".encode("utf-8")
        )
