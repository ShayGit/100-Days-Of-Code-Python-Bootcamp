##################### Extra Hard Starting Project ######################
import random

import pandas
from datetime import datetime
import smtplib


today = datetime.now()
today_tuple = (today.month, today.day)

my_email = "testmail@gmail.com"
password = "testpass"
df = pandas.read_csv("birthdays.csv")

birthday_dict = {(row["month"], row["day"]): row for (index, row) in df.iterrows()}
print(birthday_dict)
if today_tuple in birthday_dict:
    person = birthday_dict[today_tuple]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt")as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]",person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}")






