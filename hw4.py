from datetime import datetime, timedelta 

users = [  
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smith1", "birthday": "1990.03.17"},
    {"name": "Jane Smith2", "birthday": "1990.03.14"},
    {"name": "Jane Smith3", "birthday": "1990.04.10"},
]

def get_upcoming_birthdays(users):

    today = datetime.today().date()

    upcoming_birthdays = []

    for user in users:

        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:

            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days   
        if days_until_birthday <= 7:

            congratulation_date = birthday_this_year

            if congratulation_date.weekday() >= 5:  

               congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))

            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays

print(get_upcoming_birthdays(users))