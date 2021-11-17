# The first block of code ask users to enter series of food orders.
geekas = '\nPlace your order: '
geekas += '\nEnter "quit" to end the order: '

order = ''
while order != "quit":
    order = input(geekas)
    
    if order != "quit":
        print(f'I will add {order.title()} to your order.')

age = 15

age_input = input('Please tell us your age: ')
age_input = int(age_input)

if age < 3:
    price = 0
if age >=3 and age < 12:
    price = 10
if age > 12:
    price = 20
else:
    print('Invalid age')

print(f'Your acceptance fee is ${price} only.')