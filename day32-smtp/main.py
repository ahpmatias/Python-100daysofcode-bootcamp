import smtplib
import datetime as dt
import random
import pandas as pd

my_email = "ahpmatias@gmail.com"
password = "mdkb ylwn zacn nsqq"

letters_list = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

df = pd.read_csv('birthdays.csv')

today = dt.datetime.now()
today_tuple = (today.month, today.day)
birthdays_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in df.iterrows()}

if today_tuple in birthdays_dict:
    letter = random.choice(letters_list)
    with open(f'./letter_templates/{letter}') as letter_text:
        letter_text = letter_text.read()
        custom_text = letter_text.replace('[NAME]', birthdays_dict[today_tuple]['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="ahpmatias@gmail.com",
                            msg="Subject: Cuidado com a Skynet pai!!"



# with open('quotes.txt') as quotes_file:
#     quotes_file_list = quotes_file.readlines()
#     quotes_list = []
#     for num in range(0, len(quotes_file_list)):
#         quotes_list.append(quotes_file_list[num].strip())

# if day_of_week == 3:
#     with open('quotes.txt') as quotes_file:
#         quotes_file_list = quotes_file.readlines()
#         quote = random.choice(quotes_file_list)
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs="ahpmatias@gmail.com",
#                             msg=f"Subject:Motivation Day\n\n{quote}"
#                             )

