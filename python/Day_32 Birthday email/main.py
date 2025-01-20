import datetime as dt
import random
import smtplib
import pandas

my_email = "yanendrajha37@gmail.com"
password = "wdtincdzgqsktjuu"

# 1. Update the birthdays.csv with your friends & family's details.
# Done

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
today = dt.datetime.now()
today_tuple = (today.month, today.day)


# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {
#     (month, day): data_row
# }
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    letter_no = random.randint(1, 3)
    file_path = f"letter_templates/letter_{letter_no}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        z = contents.replace("[NAME]", birthdays_person["name"])
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    # HINT: https://www.w3schools.com/python/ref_string_replace.asp

    # 4. Send the letter generated in step 3 to that person's email address.
    # HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()

        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthdays_person["email"],
                            msg=f"subject: Happy Birthday \n\n{contents}")
