guest_register = input('Enter your name: ')

guest = 'guest.txt'
with open(guest, 'w') as file_object:
    file_object.write(guest_register.title())


guest = 'guest_book.txt'
print('Enter "exit" when you\'re done. ')

while True:
    guest_name = input('\nEnter your name: ')
    if guest_name == 'exit':
        break
    else:
        with open(guest, 'a') as file_object:
            file_object.write(f'{guest_name}\n')
        print(f'Hello {guest_name}, you have been added to the guest book. ')


filename = 'programming_poll.txt'

responses = []
while True:
    response = input('\nWhy do you like programming? ')
    responses.append(response)

    continue_poll = input('Would you mind to let another person to respond? (y/n) ')
    if continue_poll != 'y':
        break

with open(filename, 'a') as file_object:
    for response in responses:
        file_object.write('responses') 