def make_shirt(shirt_size, shirt_message):
    '''This function takes the size of a shirt and a message written on it'''
    print(f'\nThe size of my shirt is: {shirt_size}')
    print(f'The following will be printed on my shirt: {shirt_message} ')

make_shirt(43, 'Today is a blessing!')
make_shirt(shirt_size=43, shirt_message='Next year will be better than this year in all ramifications for me!')

make_shirt(38, 'I love Python!')

def describe_city(city, country='nigeria'):
    '''This function describes a city'''
    print(f'Lagos is in {city.title()}')
    print(f'Enohia Itim is in {country.title()}')
    

describe_city(city='lagos')

def get_formatted_name(first_name, last_name):
    '''Return a full name, neatly formatted in Nigerian style.'''
    full_name = f'{first_name} {last_name}'
    return full_name.title()

ceo_NOMAD = get_formatted_name('nwachi', 'felix')
print(ceo_NOMAD)
print('...........................................................')

def get_formatted_name(first_name, last_name, middle_name=''):
    '''Given option for middle name in the function'''
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()

ceo_NOMAD = get_formatted_name('nwachi', 'felix')
print(ceo_NOMAD)

ceo_NOMAD = get_formatted_name('nwachi', 'ogbonna', 'felix')
print(ceo_NOMAD)


def whole_being(first_name, last_name, age=None):
    '''Returns a dictionary of information about a person'''
    being = {'first': first_name, 'last': last_name}
    if age:
        being['age'] = age
    return being

ceo_NOMAD = whole_being('nwachi', 'felix', age=32)
print(ceo_NOMAD)

# An infinite loop
while True:
    print('\nplease tell me your name: ')
    print("(enter 'q' at anytime to quit)")

    f_name = input('First name: ')
    if f_name == 'q':
        break

    l_name = input('Last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f'\nHello, {formatted_name}! ')

