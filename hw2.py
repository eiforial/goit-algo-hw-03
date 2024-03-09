import random

min = 1
max = 100
quantity = 10

def get_number_ticket(min, max, quantity):
    
    if type(min) != int or type(max) != int or type(quantity) != int:
        print("min, max, quantity должны бить целым числом")
        return None
    
    if min > max:
        print("min должно быть меньше чем max")
        return None
    
    if quantity < 0:
        print("quantity не может быть отрицательным")
        return None

    if quantity > max - min + 1:
        print("количество выведенных чисел не может быть больше количества заданного диапазоном")
        return None
    
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))
    
    return sorted(list(numbers))

ticket_num = get_number_ticket(min, max, quantity)

print(ticket_num)