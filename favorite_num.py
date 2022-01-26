import json

usersnum = input('What is your favourite number? ')

filename = 'usersnum.json'

with open(filename, 'w') as f:
    json.dump(usersnum, f)

print(f'I know your favourite number. It\'s: {usersnum}! ')

with open(filename) as f:
    usersnum = json.load(f)
    print(f'Your favourite number is {usersnum}, Mr. Nwachi Felix!')


