from datetime import datetime

def get_days_from_today():
        try:
                date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
                date_today = datetime.today()
                user_date = datetime.strptime(date, "%Y-%m-%d")
                difference = date_today - user_date
        
                print(f"Разница между датами состовляет {difference.days} дней")

                get_days_from_today()

        except ValueError as e:

            print("Неправильный формат даты! Используйте формат ГГГГ-ММ-ДД.", e)

            get_days_from_today()

get_days_from_today() 