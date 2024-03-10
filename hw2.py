import random



def get_number_ticket(min, max, quantity):
    
    if type(min) != int or type(max) != int or type(quantity) != int:
        
        return None
    
    if min > max:
        
        return None
    
    if quantity < 0:
        
        return None

    if quantity > max - min + 1:
        
        return None
    
    numbers = set()

    while len(numbers) < quantity:
        
        numbers.add(random.randint(min, max))
    
    return sorted(list(numbers))

ticket_num = get_number_ticket(1, 49, 6)

print(ticket_num)