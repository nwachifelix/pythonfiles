# def get_formatted_name(first, last):
#     '''Generate a neatly formatted full name.'''
#     full_name = f'{first} {last}'
#     return full_name.title()

# get_formatted_name('nwachi', 'felix')

def get_formatted_name(first, last, middle=''):
    '''Generate a neatly formatted full name.'''
    if middle:
        full_name = f'{first} {last} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()
