# Start with users that needs to be verified,
# and an empty list to hold confirmed users. 
unconfirmed_users = ['single', 'james', 'nas']
confirmed_users = []

# Verify each user untill there re no more unconfirmed users. 
# Move each verified user into the list of confirmed users. 
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f'Verifying user: {current_user.title()} ')
    confirmed_users.append(current_user)
# Display all confirmed users. 
print(f'\nThe following users have been confirmed: ')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
print('')
# Removing all instances of specific value. 
pets =['dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

responses = {}

# Set a flag to rindicate that polling is active. 
polling_active = True

while polling_active:
    #Prompt for the person's name and response.polling_active
    name = input('\nWhat is your name? ')
    response = input('Which mountain would you like to climb? ')

    #Store the response in the dictionary. 
    responses[name] = response 

    # Find out if anyone else is going to take the poll. 
    repeat = input('Would you like to let another person respond? (yes/ no) ')
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results. 
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(f'{name} would like to climb {response}. ')
