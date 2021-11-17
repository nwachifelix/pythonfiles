message = input('Tell me something and I will repeat it back to you: ')
print(message)

name = input('Please enter your name:')
print(f'\nHello {name}!')

prompt = 'If you tell me how you feel, i can personalize the messages you see. '
prompt += '\nwhat is your first name? '
name = input(prompt)
print(f'\nHello {name}! ')

#Using the int() in actual program
height = input('How tall are you, in inches? ')
height = int(height)
if height >= 48:
    print('\nYou re tall enough to ride! ' )
else:
    print('\nYou ll be able to ride when you re much older. ')

number = input('Enter a number, and I will tell you if it\'s even or odd: ')
number = int(number)

if number % 2 == 0:
    print(f'The number {number} i even. ')
else:
    print(f'The number {number} is odd. ')

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = '\nTell me something, and I will repeat it back to you: '
prompt += '\nEnter quit" to end the program: '
message = ''
while message != 'quit' :
    message = input(prompt)
    if message != 'quit':
        print(message)

prompt = '\nTell me something, and I will repeat it back to you: '
prompt += '\nEnter "quit" to end the program: '

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

prompt = '\nPlease enter the name of the city you have visited: '
prompt += '\n(Enter "quit" when you are finished.) '

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f'I\'d love to go to {city.title()}. ')

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)