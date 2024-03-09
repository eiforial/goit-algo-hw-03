from datetime import datetime

date = '2024-04-15'

def get_days_from_today(date):
    try:
        user_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return "Ошибка: Неправильный формат даты. Используйте формат YYYY-MM-DD."

    date_today = datetime.today()
    delta = date_today - user_date
    
    return delta.days

days_difference = get_days_from_today(date)
print("Разница в днях:", days_difference)