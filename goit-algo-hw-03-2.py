import random

def random_unique_numbers():
    try:
    
        min = int(input("Введите минимальное значение: "))
        max = int(input("Введите максимальное значение: "))
        quantity = int(input("Введите количество уникальных чисел: "))
        if quantity > max -min + 1:
            print ("количество выведенных чисел не может быть больше количества заданного диапазоном")
            return  [] 
    
        numbers = list(range(min, max + 1))
        random.shuffle(numbers)
        return numbers[:quantity]
    
    except ValueError as e:
        print ("Неправильный формат ввода данных, введите целое число", e)
        random_unique_numbers()
print(random_unique_numbers())