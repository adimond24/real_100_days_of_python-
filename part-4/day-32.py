import smtplib
import datetime as dt
import random
from pandas import read_csv

MY_EMAIL = "ameliaschoolcoding@gmail.com"
MY_PASSWORD = "tankrosknqtsaisv"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}" )


# my_email = "ameliaschoolcoding@gmail.com"
# password = "tank rosk nqts aisv"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="ameliatesting2@yahoo.com", msg=f"Subject:Monday Quote\n\n {quote}")
#
# # import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2007, month=12, day=15, hour=4)
# print(date_of_birth)