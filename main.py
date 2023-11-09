import smtplib
import datetime as dt
import pandas
from random import choice

EMAIL = ""
PASSWORD = ""
BIRTHDAYS_FILE = "birthdays.csv"
letters = ['letter_1', 'letter_2', 'letter_3']
now = dt.datetime.now()
PLACEHOLDER = "[NAME]"

birthdays_data = pandas.read_csv(BIRTHDAYS_FILE)
#birthdays = birthdays_data.to_dict(orient="records")
birthdays = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays_data.iterrows()}
today = (now.month, now.day)


def get_letter():
    letter_template = f"letter_templates/{choice(letters)}.txt"
    with open(letter_template) as letter_file:
        letter = letter_file.read()

    return letter




if today in birthdays:
    birthday = birthdays[today]
    letter = get_letter()
    letter = letter.replace(PLACEHOLDER, birthday['name'].strip())
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="davidthe@myyahoo.com",
            msg=f"Subject:Happy Birthday\n\n{letter}"
        )


#if now.weekday() == 0:

    # quotes = pandas.read_csv("quotes.txt", header=None)
    # quotes = quotes.to_dict()
    # quote = choice(quotes[0])

    # with open("quotes.txt") as quotes:
    #     all_quotes = quotes.readlines()
    #     quote = choice(all_quotes)
    #
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=EMAIL, password=PASSWORD)
    #     connection.sendmail(
    #         from_addr=EMAIL,
    #         to_addrs="davidthe@myyahoo.com",
    #         msg=f"Subject:Quote of the day\n\n{quote}"
    #     )
