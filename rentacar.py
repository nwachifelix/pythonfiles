# User input output
cars = input(f'\nWhat type of car do you want? ')
print(f'Lemme see if our {cars} 4Matic is still available. ')
print('...' *20)
table_reservation = input('How many people do you expect in your dinner group? ')
table_reservation = int(table_reservation)
if table_reservation >= 8:
    print('You will have to wait for a table. ')
else:
    print('Your table is ready! ')
print('...' *20)
# Using the Modulo operator % to determine if a number is a multiple of 10 or not.  
number = input('Please, give us a number: ')
number = int(number)
if number % 10 == 0:
    print(f'\nNumber {number} is a multiple of 10.\n ')
else:
    print(f'Number {number} is not a multiple of 10.\n ')