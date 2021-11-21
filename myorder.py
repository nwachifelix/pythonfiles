foods = ['jellof rice', 'spag', 'white rice', 'fried plantain', 'spag', 'porrage beans', 'white beans', 'spag']
finished_foods = []

while foods:
    recent_orders = foods.pop()
    print(f'I have made your {recent_orders} ')
    finished_foods.append(recent_orders)
    print(' ')
    for finished_food in finished_foods:
        print(f'Your food is ready! ')


print(f'There is no more spag in {foods}. ')
while foods:
    finished_foods.remove('spag')
print(foods)
print(finished_foods)


